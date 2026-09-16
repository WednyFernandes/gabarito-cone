# Gabarito de Cone para Designers – Molde SVG de Adesivo para Copo, Balde e Caneca Cônica

Você é **designer gráfico** e precisa aplicar arte em copo, balde de pipoca ou caneca cônica? Esta ferramenta gera o **gabarito vetorial (SVG) do tronco de cone planificado** em escala real, pronto para abrir no **Illustrator, CorelDRAW, Inkscape, Affinity Designer ou Figma** e usar como máscara de recorte da sua arte. Chega de rótulo torto, emenda que não fecha e arte cortada.

![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![SVG](https://img.shields.io/badge/sa%C3%ADda-SVG%20vetorial-orange) ![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-lightgrey)

## Por que designers usam

- **Vetor em escala 1:1** – importa direto no seu software sem redimensionar
- **Molde correto na primeira tentativa** – a curvatura do adesivo é calculada, não estimada
- **Margem de emenda / sangria** configurável para colagem e acabamento
- **Área do gabarito** exibida para orçar vinil, papel adesivo ou sublimático
- Funciona **offline**, sem cadastro, sem marca d'água

## Casos de uso

| Produto | Aplicação |
|---|---|
| Copo de papel / plástico / long drink cônico | Rótulo envolvente, adesivo promocional |
| Balde de pipoca e balde de gelo | Arte de cinema, festas, brindes |
| Caneca e copo cônico para sublimação | Estampa 360° sem distorção |
| Vaso, cachepô, embalagem cônica | Etiqueta de marca, kit presente |
| Mockup e apresentação para cliente | Base geométrica precisa para a arte final |

## Fluxo de trabalho no seu editor

1. Rode a ferramenta, informe **diâmetro do topo, da base e altura** (cm)
2. Clique **Gerar Gabarito** → **Salvar SVG** (`gabarito.svg` na Área de Trabalho)
3. Importe o SVG no **Illustrator / CorelDRAW / Inkscape**
4. Use o caminho azul como **máscara de recorte (clipping mask / PowerClip)** sobre sua arte
5. A linha tracejada laranja marca a **emenda** – mantenha logos e textos fora dela
6. Exporte em PDF/X ou envie o SVG para corte em plotter

> Dica: para arte envolvente contínua, distorça o layout com *Envelope* / *Arc* seguindo o ângulo mostrado no gabarito.

## Instalação

```bash
pip install pywebview
python gabarito_cone.py
```

## O que a ferramenta calcula

Para diâmetros `D` (base), `d` (topo) e altura `h`:

- Altura do cone completo: `H = h · D / (D − d)`
- Raio externo do gabarito (geratriz maior): `S₁ = √((D/2)² + H²)`
- Raio interno (geratriz menor): `S₂ = √((d/2)² + (H − h)²)`
- Ângulo do setor: `θ = 360° · D / (2·S₁)`

Se topo = base, gera um retângulo (cilindro).

## Perguntas frequentes

**O SVG abre no Photoshop?** Abre como objeto inteligente, mas para recorte vetorial prefira Illustrator ou CorelDRAW.

**Qual medida usar, interna ou externa?** Use o **diâmetro externo** do produto, onde o adesivo vai colar.

**Posso usar em produção comercial?** Sim, licença MIT.

## Palavras-chave

gabarito cone designer, molde adesivo copo illustrator, gabarito balde de pipoca corel, planificação cone truncado svg, rótulo copo cônico vetor, template adesivo copo, molde caneca cônica sublimação, máscara de recorte copo, gabarito copo long drink, gerador de gabarito svg

## Licença

MIT
