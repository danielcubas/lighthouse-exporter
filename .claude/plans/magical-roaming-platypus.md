# Plano: Lighthouse Exporter

## Contexto

Ferramenta Python CLI que recebe a URL de um site, executa análise via API do PageSpeed Insights v5 (mobile + desktop) e gera um único arquivo `.md` com ambos os resultados, pronto para análise por agente de IA.

## Dependências

- `requests` (único pacote externo)
- Arquivo `requirements.txt`

## Implementação — `lighthouse_exporter.py`

### CLI
```
python lighthouse_exporter.py <URL_DO_SITE> [--output DIR] [--api-key KEY]
```
- `<URL_DO_SITE>` — URL direta do site (ex: `https://inovgest.com.br`)
- `--output` / `-o` — diretório de saída (default: `.`)
- `--api-key` / `-k` — API key opcional do Google (aumenta rate limit)

### Fluxo
1. Receber URL do site via argparse
2. Chamar API do PageSpeed duas vezes (mobile + desktop), todas as categorias: `performance`, `accessibility`, `best-practices`, `seo`
3. Extrair: scores, Core Web Vitals, oportunidades de melhoria, diagnósticos, auditorias aprovadas
4. Gerar **um único arquivo `.md`** com seções separadas para Mobile e Desktop
5. Salvar como `lighthouse_{dominio}_{timestamp}.md`

### Chamada à API
```
GET https://www.googleapis.com/pagespeedonline/v5/runPagespeed
  ?url=https://inovgest.com.br
  &strategy=mobile|desktop
  &category=performance&category=accessibility&category=best-practices&category=seo
  &locale=pt-br
```

### Estrutura do relatório `.md`

```markdown
# Relatório Lighthouse — {url}
**Data:** {timestamp}

---

## Desktop

### Pontuações
| Categoria | Pontuação |
|-----------|-----------|
| Performance | 🟢 95 |
| Acessibilidade | 🟠 78 |
| ...

### Métricas de Performance
| Métrica | Valor | Pontuação |
|---------|-------|-----------|
| FCP | 1.2s | 🟢 |
| LCP | 2.5s | 🟢 |
| TBT | 150ms | 🟠 |
| CLS | 0.01 | 🟢 |
| Speed Index | 2.5s | 🟢 |

### Oportunidades de Melhoria
(lista com nome, economia estimada, descrição)

### Diagnósticos
(lista com nome e detalhes)

### Auditorias Aprovadas
(lista de itens aprovados)

---

## Mobile
(mesma estrutura do Desktop)
```

### Indicadores visuais de score
- 🟢 score >= 0.9 (bom)
- 🟠 score >= 0.5 (precisa melhorar)
- 🔴 score < 0.5 (ruim)

## Arquivos a criar

| Arquivo | Descrição |
|---------|-----------|
| `requirements.txt` | Dependência: requests |
| `lighthouse_exporter.py` | Script principal |

## Verificação

```bash
pip install -r requirements.txt
python lighthouse_exporter.py "https://inovgest.com.br"
# Verificar que o .md foi gerado com seções Mobile e Desktop
```
