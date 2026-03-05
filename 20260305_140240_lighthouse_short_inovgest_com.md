# Relatório Lighthouse — https://short.inovgest.com/
**Data:** 2026-03-05 14:03:17

---

## Desktop

### Pontuações
| Categoria | Pontuação |
|-----------|-----------|
| Desempenho | 🟢 100 |
| Acessibilidade | 🟢 95 |
| Práticas recomendadas | 🟢 100 |
| SEO | 🟢 100 |

### Métricas de Performance
| Métrica | Valor | Pontuação |
|---------|-------|-----------|
| FCP | 0,2 s | 🟢 |
| LCP | 0,7 s | 🟢 |
| TBT | 10 ms | 🟢 |
| CLS | 0,002 | 🟢 |
| Speed Index | 0,6 s | 🟢 |

### Oportunidades de Melhoria
Nenhuma oportunidade identificada.

### Diagnósticos
- **Reduza o JavaScript não usado** — Economia estimada de 57 KiB
  - https://short.inovgest.com/_next/static/chunks/7f67e7115e995555.js?dpl=dpl_4Lwa4rDLNR2kDYnAQh5K2LXdM8RH | 32431 | 31903
  - https://short.inovgest.com/_next/static/chunks/59d3bac19b607854.js?dpl=dpl_4Lwa4rDLNR2kDYnAQh5K2LXdM8RH | 71084 | 26850

### Auditorias Reprovadas
- **As cores de primeiro e segundo plano não têm uma taxa de contraste suficiente.**
  Para muitos usuários, é difícil ou impossível ler textos com baixo contraste. [Aprenda a fornecer contraste de cor suficiente](https://dequeuniversity.com/rules/axe/4.11/color-contrast).
  **Elementos com falha:**
  - `Short` — `<span class="font-heading font-bold tracking-tight text-slate-400 text-xl">`
  - `short.inovgest.com` — `<span class="text-xs text-slate-400 font-mono">`
  - `DIFERENCIAIS TÉCNICOS` — `<span class="text-xs uppercase tracking-[0.2em] font-bold text-slate-400">`
  - `nada que não precisa` — `<span class="text-slate-400">`
  - `Short` — `<span class="font-heading font-bold tracking-tight text-slate-400 text-xl">`
  - `A plataforma mais completa para encurtar, gerenciar e analisar seus links.` — `<p class="text-[15px] text-slate-500 leading-relaxed max-w-xs">`
  - `PRODUTO` — `<h4 class="text-xs uppercase tracking-widest font-bold text-slate-400">`
  - `Funcionalidades` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/#funcionalidades">`
  - `Preços` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/precos">`
  - `Documentação API` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/documentacao">`
  - `Atualizações` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/atualizacoes">`
  - `EMPRESA` — `<h4 class="text-xs uppercase tracking-widest font-bold text-slate-400">`
  - `Sobre` — `<a href="https://inovgest.com.br" target="_blank" rel="noopener noreferrer" class="text-[15px] text-slate-500 transition-colors hover:text-slate-800">`
  - `Contato` — `<a href="https://inovgest.com.br/#contato" target="_blank" rel="noopener noreferrer" class="text-[15px] text-slate-500 transition-colors hover:text-slate-800">`
  - `LEGAL` — `<h4 class="text-xs uppercase tracking-widest font-bold text-slate-400">`
  - `Termos de Uso` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/termos">`
  - `Privacidade` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/privacidade">`
  - `© 2026 Inovgest Short. Todos os direitos reservados.` — `<p class="text-sm text-slate-400">`
  - `suporte@inovgest.com.br` — `<a href="mailto:suporte@inovgest.com.br" class="text-sm text-slate-400 transition-colors hover:text-slate-800">`
- **Os elementos de título não aparecem em uma ordem sequencial descendente**
  Títulos propriamente ordenados que não pulam níveis comunicam a estrutura semântica da página, facilitando a navegação e compreensão ao usar tecnologias adaptativas. [Saiba mais sobre ordem de títulos](https://dequeuniversity.com/rules/axe/4.11/heading-order).
  **Elementos com falha:**
  - `PRODUTO` — `<h4 class="text-xs uppercase tracking-widest font-bold text-slate-400">`

### Auditorias Aprovadas
- A página não está bloqueada para indexação
- A página tem mapas de origem válidos
- A página tem o doctype HTML
- A página tem um código de status HTTP bem-sucedido
- As funções ARIA descontinuadas não foram usadas
- As listas contêm somente elementos `<li>` e elementos compatíveis com script (`<script>` e `<template>`).
- As áreas de toque têm tamanho e espaçamento suficientes.
- Define corretamente o charset
- Evita APIs obsoletas
- Evita cookies de terceiros
- Evita o pedido da permissão de geolocalização no carregamento de página
- Evita o pedido da permissão de notificação no carregamento de página
- Exibe imagens com a proporção correta
- Exibe imagens em resolução adequada
- Itens de lista (`<li>`) estão contidos nos elementos pai `<ul>`, `<ol>` ou `<menu>`
- Nenhum elemento tem um valor de `[tabindex]` maior que 0
- Nenhum erro do navegador registrado no console
- Nenhum problema no painel `Issues` do Chrome Devtools
- O `[aria-hidden="true"]` não está presente no documento `<body>`
- O documento tem um `hreflang` válido
- O documento tem um `rel=canonical` válido
- O documento tem um elemento `<title>`
- O documento tem um ponto de referência principal.
- O documento tem uma metadescrição
- O elemento `<html>` tem um atributo `[lang]`
- O elemento `<html>` tem um valor válido para o atributo `[lang]`
- Os atributos ARIA são usados conforme especificado para a função do elemento
- Os atributos `[aria-*]` correspondem às próprias funções
- Os atributos `[aria-*]` são válidos e não contêm erros de ortografia
- Os atributos `[aria-*]` têm valores válidos
- Os botões têm um nome acessível
- Os elementos `[aria-hidden="true"]` não contêm descendentes focalizáveis
- Os elementos de formulário têm etiquetas associadas
- Os elementos de imagem têm atributos `[alt]`
- Os elementos usam apenas atributos ARIA permitidos
- Os links são rastreáveis
- Os links têm texto descritivo
- Os links têm um nome compreensível
- Os valores de `[role]` são válidos
- Permitir que os usuários colem dados nos campos de entrada
- Utiliza HTTPS
- `[role]`s têm todos os atributos `[aria-*]` obrigatórios
- `[user-scalable="no"]` não é usado no elemento `<meta name="viewport">`, e o atributo `[maximum-scale]` não é menor que 5.
- robots.txt é válido

---

## Mobile

### Pontuações
| Categoria | Pontuação |
|-----------|-----------|
| Desempenho | 🟠 89 |
| Acessibilidade | 🟢 95 |
| Práticas recomendadas | 🟢 100 |
| SEO | 🟢 100 |

### Métricas de Performance
| Métrica | Valor | Pontuação |
|---------|-------|-----------|
| FCP | 0,9 s | 🟢 |
| LCP | 3,3 s | 🟠 |
| TBT | 0 ms | 🟢 |
| CLS | 0,002 | 🟢 |
| Speed Index | 4,5 s | 🟠 |

### Oportunidades de Melhoria
Nenhuma oportunidade identificada.

### Diagnósticos
- **Reduza o JavaScript não usado** — Economia estimada de 26 KiB
  - https://short.inovgest.com/_next/static/chunks/59d3bac19b607854.js?dpl=dpl_4Lwa4rDLNR2kDYnAQh5K2LXdM8RH | 71093 | 26707

### Auditorias Reprovadas
- **As cores de primeiro e segundo plano não têm uma taxa de contraste suficiente.**
  Para muitos usuários, é difícil ou impossível ler textos com baixo contraste. [Aprenda a fornecer contraste de cor suficiente](https://dequeuniversity.com/rules/axe/4.11/color-contrast).
  **Elementos com falha:**
  - `Short` — `<span class="font-heading font-bold tracking-tight text-slate-400 text-xl">`
  - `short.inovgest.com` — `<span class="text-xs text-slate-400 font-mono">`
  - `Short` — `<span class="font-heading font-bold tracking-tight text-slate-400 text-xl">`
  - `A plataforma mais completa para encurtar, gerenciar e analisar seus links.` — `<p class="text-[15px] text-slate-500 leading-relaxed max-w-xs">`
  - `PRODUTO` — `<h4 class="text-xs uppercase tracking-widest font-bold text-slate-400">`
  - `Funcionalidades` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/#funcionalidades">`
  - `Preços` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/precos">`
  - `Documentação API` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/documentacao">`
  - `Atualizações` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/atualizacoes">`
  - `EMPRESA` — `<h4 class="text-xs uppercase tracking-widest font-bold text-slate-400">`
  - `Sobre` — `<a href="https://inovgest.com.br" target="_blank" rel="noopener noreferrer" class="text-[15px] text-slate-500 transition-colors hover:text-slate-800">`
  - `Contato` — `<a href="https://inovgest.com.br/#contato" target="_blank" rel="noopener noreferrer" class="text-[15px] text-slate-500 transition-colors hover:text-slate-800">`
  - `LEGAL` — `<h4 class="text-xs uppercase tracking-widest font-bold text-slate-400">`
  - `Termos de Uso` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/termos">`
  - `Privacidade` — `<a class="text-[15px] text-slate-500 transition-colors hover:text-slate-800" href="/privacidade">`
  - `© 2026 Inovgest Short. Todos os direitos reservados.` — `<p class="text-sm text-slate-400">`
  - `suporte@inovgest.com.br` — `<a href="mailto:suporte@inovgest.com.br" class="text-sm text-slate-400 transition-colors hover:text-slate-800">`
- **Os elementos de título não aparecem em uma ordem sequencial descendente**
  Títulos propriamente ordenados que não pulam níveis comunicam a estrutura semântica da página, facilitando a navegação e compreensão ao usar tecnologias adaptativas. [Saiba mais sobre ordem de títulos](https://dequeuniversity.com/rules/axe/4.11/heading-order).
  **Elementos com falha:**
  - `PRODUTO` — `<h4 class="text-xs uppercase tracking-widest font-bold text-slate-400">`

### Auditorias Aprovadas
- A página não está bloqueada para indexação
- A página tem mapas de origem válidos
- A página tem o doctype HTML
- A página tem um código de status HTTP bem-sucedido
- As funções ARIA descontinuadas não foram usadas
- As listas contêm somente elementos `<li>` e elementos compatíveis com script (`<script>` e `<template>`).
- As áreas de toque têm tamanho e espaçamento suficientes.
- Define corretamente o charset
- Evita APIs obsoletas
- Evita cookies de terceiros
- Evita o pedido da permissão de geolocalização no carregamento de página
- Evita o pedido da permissão de notificação no carregamento de página
- Exibe imagens com a proporção correta
- Exibe imagens em resolução adequada
- Itens de lista (`<li>`) estão contidos nos elementos pai `<ul>`, `<ol>` ou `<menu>`
- Nenhum elemento tem um valor de `[tabindex]` maior que 0
- Nenhum erro do navegador registrado no console
- Nenhum problema no painel `Issues` do Chrome Devtools
- O `[aria-hidden="true"]` não está presente no documento `<body>`
- O documento tem um `hreflang` válido
- O documento tem um `rel=canonical` válido
- O documento tem um elemento `<title>`
- O documento tem um ponto de referência principal.
- O documento tem uma metadescrição
- O elemento `<html>` tem um atributo `[lang]`
- O elemento `<html>` tem um valor válido para o atributo `[lang]`
- Os atributos ARIA são usados conforme especificado para a função do elemento
- Os atributos `[aria-*]` correspondem às próprias funções
- Os atributos `[aria-*]` são válidos e não contêm erros de ortografia
- Os atributos `[aria-*]` têm valores válidos
- Os botões têm um nome acessível
- Os elementos `[aria-hidden="true"]` não contêm descendentes focalizáveis
- Os elementos de formulário têm etiquetas associadas
- Os elementos de imagem têm atributos `[alt]`
- Os elementos usam apenas atributos ARIA permitidos
- Os links são rastreáveis
- Os links têm texto descritivo
- Os links têm um nome compreensível
- Os valores de `[role]` são válidos
- Permitir que os usuários colem dados nos campos de entrada
- Utiliza HTTPS
- `[role]`s têm todos os atributos `[aria-*]` obrigatórios
- `[user-scalable="no"]` não é usado no elemento `<meta name="viewport">`, e o atributo `[maximum-scale]` não é menor que 5.
- robots.txt é válido
