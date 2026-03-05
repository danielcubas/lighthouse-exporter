# Lighthouse Analysis Exporter

CLI tool that fetches [Google PageSpeed Insights](https://pagespeed.web.dev/) (Lighthouse) reports and exports them as Markdown files.

## Features

- Exports full Lighthouse reports as readable Markdown
- Analyzes both **desktop** and **mobile** strategies
- Includes Core Web Vitals (FCP, LCP, TBT, CLS, Speed Index)
- Lists improvement opportunities with estimated savings
- Shows diagnostics, failed audits (with failing elements), and passed audits
- Supports Google API key via CLI flag or `.env` file

## Requirements

- Python 3.13+
- A Google PageSpeed Insights API key (optional but recommended to avoid rate limits)

## Installation

```bash
git clone https://github.com/your-user/lighthouse-exporter.git
cd lighthouse-exporter

# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python lighthouse_exporter.py https://example.com

# Specify output directory
python lighthouse_exporter.py https://example.com -o reports/

# Pass API key directly
python lighthouse_exporter.py https://example.com -k YOUR_API_KEY
```

### API Key via `.env`

Create a `.env` file in the project root:

```
PAGESPEED_API_KEY=your_api_key_here
```

The tool will automatically load it. You can get a free API key from the [Google Cloud Console](https://console.cloud.google.com/apis/credentials).

## Output

Reports are saved as `<timestamp>_lighthouse_<domain>.md` with the following sections for each strategy (desktop/mobile):

- **Scores** — Category scores for Performance, Accessibility, Best Practices, and SEO
- **Performance Metrics** — Core Web Vitals with values and score indicators
- **Improvement Opportunities** — Actionable suggestions with estimated time savings
- **Diagnostics** — Additional performance insights
- **Failed Audits** — Binary audits that did not pass, with failing elements
- **Passed Audits** — Binary audits that passed

### Sample output

```markdown
# Lighthouse Report — https://example.com
**Date:** 2026-03-05 14:30:00

## Desktop

### Scores
| Category | Score |
|----------|-------|
| Performance | 🟢 95 |
| Accessibility | 🟢 100 |
| Best Practices | 🟢 92 |
| SEO | 🟢 90 |
```

## License

MIT
