#!/usr/bin/env python3
"""Lighthouse Exporter — exports PageSpeed Insights reports as Markdown."""

import argparse
import os
import sys
from datetime import datetime
from urllib.parse import urlparse

from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
CATEGORIES = ["performance", "accessibility", "best-practices", "seo"]
STRATEGIES = ["desktop", "mobile"]
CORE_WEB_VITALS = [
    ("first-contentful-paint", "FCP"),
    ("largest-contentful-paint", "LCP"),
    ("total-blocking-time", "TBT"),
    ("cumulative-layout-shift", "CLS"),
    ("speed-index", "Speed Index"),
]


def format_audit_details(audit):
    """Extract detailed items (failing elements, etc.) from the audit details field."""
    details = audit.get("details", {})
    items = details.get("items", [])
    if not items:
        return []

    detail_lines = []
    headings = details.get("headings", [])
    heading_keys = [(h.get("key"), h.get("label", "")) for h in headings if h.get("key")]

    for item in items:
        # DOM element (node snippet)
        node = item.get("node", {})
        if node:
            label = node.get("nodeLabel", "")
            snippet = node.get("snippet", "")
            if label or snippet:
                line = f"  - `{label}`" if label else ""
                if snippet:
                    line += f" — `{snippet}`" if line else f"  - `{snippet}`"
                detail_lines.append(line)
            continue

        # Tabular rows (e.g. resources, sizes)
        parts = []
        for key, heading_label in heading_keys:
            val = item.get(key)
            if val is None:
                continue
            if isinstance(val, dict):
                # Could be an embedded node or url
                if val.get("type") == "node":
                    parts.append(val.get("snippet") or val.get("nodeLabel", ""))
                elif val.get("type") == "url":
                    parts.append(val.get("url", str(val)))
                else:
                    parts.append(str(val))
            else:
                parts.append(str(val))
        if parts:
            detail_lines.append(f"  - {' | '.join(parts)}")

    return detail_lines


def score_emoji(score):
    if score is None:
        return "⚪"
    if score >= 0.9:
        return "🟢"
    if score >= 0.5:
        return "🟠"
    return "🔴"


def fetch_pagespeed(url, strategy, api_key=None):
    params = {
        "url": url,
        "strategy": strategy,
        "category": CATEGORIES,
        "locale": "en",
    }
    if api_key:
        params["key"] = api_key

    print(f"  Analyzing {strategy}...", end=" ", flush=True)
    resp = requests.get(API_URL, params=params, timeout=120)
    resp.raise_for_status()
    print("OK")
    return resp.json()


def format_strategy(data):
    lines = []
    lr = data.get("lighthouseResult", {})
    categories = lr.get("categories", {})
    audits = lr.get("audits", {})

    # Scores
    lines.append("### Scores")
    lines.append("| Category | Score |")
    lines.append("|----------|-------|")
    for cat_id in CATEGORIES:
        cat = categories.get(cat_id, {})
        score = cat.get("score")
        title = cat.get("title", cat_id)
        display = int(score * 100) if score is not None else "N/A"
        lines.append(f"| {title} | {score_emoji(score)} {display} |")
    lines.append("")

    # Performance Metrics
    lines.append("### Performance Metrics")
    lines.append("| Metric | Value | Score |")
    lines.append("|--------|-------|-------|")
    for audit_id, label in CORE_WEB_VITALS:
        audit = audits.get(audit_id, {})
        value = audit.get("displayValue", "N/A")
        score = audit.get("score")
        lines.append(f"| {label} | {value} | {score_emoji(score)} |")
    lines.append("")

    # Improvement Opportunities
    opps = []
    for audit_ref in categories.get("performance", {}).get("auditRefs", []):
        if audit_ref.get("group") == "load-opportunities":
            audit = audits.get(audit_ref["id"], {})
            if audit.get("score") is not None and audit["score"] < 1:
                savings = audit.get("numericValue")
                savings_str = f" (~{savings/1000:.1f}s)" if savings else ""
                detail_lines = format_audit_details(audit)
                opps.append((audit.get("title", ""), savings_str, audit.get("description", ""), detail_lines))

    lines.append("### Improvement Opportunities")
    if opps:
        for title, savings, desc, detail_lines in opps:
            lines.append(f"- **{title}**{savings}")
            if desc:
                lines.append(f"  {desc}")
            if detail_lines:
                lines.extend(detail_lines)
    else:
        lines.append("No opportunities identified.")
    lines.append("")

    # Diagnostics
    diags = []
    for audit_ref in categories.get("performance", {}).get("auditRefs", []):
        if audit_ref.get("group") == "diagnostics":
            audit = audits.get(audit_ref["id"], {})
            if audit.get("score") is not None and audit["score"] < 1:
                detail_lines = format_audit_details(audit)
                diags.append((audit.get("title", ""), audit.get("displayValue", ""), detail_lines))

    lines.append("### Diagnostics")
    if diags:
        for title, display_val, detail_lines in diags:
            detail_str = f" — {display_val}" if display_val else ""
            lines.append(f"- **{title}**{detail_str}")
            if detail_lines:
                lines.extend(detail_lines)
    else:
        lines.append("No relevant diagnostics.")
    lines.append("")

    # Failed Audits
    failed = []
    for audit_id, audit in audits.items():
        if audit.get("score") == 0 and audit.get("scoreDisplayMode") == "binary":
            title = audit.get("title", audit_id)
            desc = audit.get("description", "")
            detail_lines = format_audit_details(audit)
            failed.append((title, desc, detail_lines))

    lines.append("### Failed Audits")
    if failed:
        for title, desc, detail_lines in sorted(failed, key=lambda x: x[0]):
            lines.append(f"- **{title}**")
            if desc:
                lines.append(f"  {desc}")
            if detail_lines:
                lines.append("  **Failing elements:**")
                lines.extend(detail_lines)
    else:
        lines.append("No failed audits.")
    lines.append("")

    # Passed Audits
    passed = []
    for audit_id, audit in audits.items():
        if audit.get("score") == 1 and audit.get("scoreDisplayMode") == "binary":
            passed.append(audit.get("title", audit_id))

    lines.append("### Passed Audits")
    if passed:
        for title in sorted(passed):
            lines.append(f"- {title}")
    else:
        lines.append("No passed audits found.")
    lines.append("")

    return "\n".join(lines)


def generate_report(url, results):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts = [
        f"# Lighthouse Report — {url}",
        f"**Date:** {now}",
        "",
    ]

    for strategy in STRATEGIES:
        parts.append("---")
        parts.append("")
        parts.append(f"## {strategy.capitalize()}")
        parts.append("")
        parts.append(format_strategy(results[strategy]))

    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Export Lighthouse report as Markdown")
    parser.add_argument("url", help="URL of the site to analyze")
    parser.add_argument("-o", "--output", default=".", help="Output directory (default: .)")
    parser.add_argument("-k", "--api-key", default=None, help="Google API key (optional, default: PAGESPEED_API_KEY from .env)")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("PAGESPEED_API_KEY")

    url = args.url
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    domain = urlparse(url).netloc.replace(".", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_lighthouse_{domain}.md"
    filepath = f"{args.output}/{filename}"

    print(f"Lighthouse Exporter — {url}")
    results = {}
    for strategy in STRATEGIES:
        try:
            results[strategy] = fetch_pagespeed(url, strategy, api_key)
        except requests.exceptions.HTTPError as e:
            print(f"\nAPI error for {strategy}: {e}", file=sys.stderr)
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            print(f"\nConnection error for {strategy}: {e}", file=sys.stderr)
            sys.exit(1)

    report = generate_report(url, results)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nReport saved to: {filepath}")


if __name__ == "__main__":
    main()
