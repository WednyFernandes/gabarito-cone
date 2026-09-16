# Gabarito de Cone – Gerador de Molde para Adesivo de Copo e Balde Cônico

Ferramenta gratuita em **Python** que calcula e gera o **gabarito (molde plano) em SVG** para aplicar adesivos, rótulos e etiquetas em **copos, baldes, vasos e embalagens cônicas**. Informe os diâmetros do topo e da base e a altura: o programa desenha a **planificação do tronco de cone** (setor de coroa circular) em escala real, pronta para imprimir ou abrir no CorelDRAW, Illustrator ou Inkscape.

![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![pywebview](https://img.shields.io/badge/GUI-pywebview-green) ![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-lightgrey)

## Para que serve

- Adesivos e rótulos para **copos de papel, copos plásticos, copos térmicos e long drinks cônicos**
- Etiquetas para **baldes de pipoca, baldes de gelo e vasos**
- **Sublimação e personalização** de canecas cônicas
- Gráficas rápidas, comunicação visual e designers que precisam do **molde correto sem cálculo manual**

## Funcionalidades

- Cálculo automático da **planificação do cone truncado** (raio maior, raio menor, ângulo do setor)
- Suporte a **cilindros** (topo = base) gerando retângulo
- **Margem de emenda** configurável (sobreposição para colagem)
- Exporta **SVG em escala real** (1 cm = 10 unidades, dimensões em mm)
- Exibe largura, altura e área do gabarito para orçamento de material
- Interface gráfica simples, funciona offline

## Instalação

```bash
pip install pywebview
python gabarito_cone.py
```

## Como usar

1. Preencha **Diâmetro Topo**, **Diâmetro Base** e **Altura** (em cm)
2. Ajuste a **Margem de emenda** se precisar de sobreposição
3. Clique em **Gerar Gabarito** e confira a prévia
4. Clique em **Salvar SVG** – o arquivo `gabarito.svg` vai para a Área de Trabalho

## Como o cálculo funciona

Para um tronco de cone com raios `r` (topo) e `R` (base) e altura `h`:

- Altura do cone completo: `H = h · D / (D − d)`
- Geratriz externa: `S₁ = √(R² + H²)`
- Geratriz interna: `S₂ = √(r² + (H − h)²)`
- Ângulo do setor: `θ = 2π · R / S₁`

O gabarito é a coroa circular entre `S₁` e `S₂` limitada pelo ângulo `θ`.

## Palavras-chave

gabarito cone, molde adesivo copo, planificação cone truncado, adesivo balde de pipoca, rótulo copo cônico, gerador svg gabarito, molde copo personalizado, sublimação caneca cônica, desenvolvimento de cone, calculadora tronco de cone

## Licença

MIT
