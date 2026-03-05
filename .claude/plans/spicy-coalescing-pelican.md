# Plan: Translate project to English + Create comprehensive README

## Context
The project is a CLI tool that fetches Google PageSpeed Insights (Lighthouse) reports and exports them as Markdown files. Currently all code strings, output messages, comments, and report content are in Portuguese. The user wants to translate everything to English and create a comprehensive README.md for a public repository.

## Files to modify

### 1. `lighthouse_exporter.py` — Translate to English
All Portuguese strings → English:

- **Docstring** (line 2): `"Lighthouse Exporter — extrai relatórios..."` → `"Lighthouse Exporter — exports PageSpeed Insights reports as Markdown."`
- **API locale** (line 88): `"locale": "pt-br"` → `"locale": "en"` (so the API returns audit titles/descriptions in English)
- **Console messages**:
  - Line 93: `"Analisando {strategy}..."` → `"Analyzing {strategy}..."`
  - Line 247: `"Lighthouse Exporter — {url}"` → keep as-is (already fine)
  - Line 253: `"Erro na API para"` → `"API error for"`
  - Line 256: `"Erro de conexão para"` → `"Connection error for"`
  - Line 264: `"Relatório salvo em:"` → `"Report saved to:"`
- **Report section headers** (format_strategy):
  - `"Pontuações"` → `"Scores"`
  - `"Categoria" / "Pontuação"` → `"Category" / "Score"`
  - `"Métricas de Performance"` → `"Performance Metrics"`
  - `"Métrica" / "Valor" / "Pontuação"` → `"Metric" / "Value" / "Score"`
  - `"Oportunidades de Melhoria"` → `"Improvement Opportunities"`
  - `"Nenhuma oportunidade identificada."` → `"No opportunities identified."`
  - `"Diagnósticos"` → `"Diagnostics"`
  - `"Nenhum diagnóstico relevante."` → `"No relevant diagnostics."`
  - `"Auditorias Reprovadas"` → `"Failed Audits"`
  - `"Elementos com falha:"` → `"Failing elements:"`
  - `"Nenhuma auditoria reprovada."` → `"No failed audits."`
  - `"Auditorias Aprovadas"` → `"Passed Audits"`
  - `"Nenhuma auditoria aprovada encontrada."` → `"No passed audits found."`
- **Report title** (generate_report):
  - `"Relatório Lighthouse"` → `"Lighthouse Report"`
  - `"Data:"` → `"Date:"`
- **Argparse** (main):
  - description: `"Exporta relatório Lighthouse em Markdown"` → `"Export Lighthouse report as Markdown"`
  - help strings: translate to English

### 2. `main.py` — No changes needed (already English)

### 3. `pyproject.toml` — Update description
- `"Add your description here"` → `"CLI tool to export Google Lighthouse reports as Markdown via PageSpeed Insights API"`

### 4. `README.md` — Complete rewrite in English
Structure:
- **Title + badge/description**: Lighthouse Exporter — one-line description
- **Features**: bullet list (Markdown export, desktop+mobile, Core Web Vitals, opportunities, diagnostics, failed/passed audits)
- **Requirements**: Python 3.13+, optional Google API key
- **Installation**: clone + `uv sync` or `pip install -r requirements.txt`
- **Usage**: CLI examples with flags (`-o`, `-k`), `.env` setup for API key
- **Output**: describe the Markdown report structure, show a sample snippet
- **License**: MIT (or ask user)

## Verification
1. Run `python lighthouse_exporter.py https://example.com` and verify all output/report content is in English
2. Verify the generated `.md` report has English section headers and English audit descriptions (from the API with `locale: "en"`)
3. Review README.md for completeness
