"""
gabarito_cone.py - Gerador de gabarito para adesivo de copo/balde
Gera SVG do desenvolvimento plano de cone truncado (setor de coroa circular)
"""
import math, json, os, sys

try:
    import webview
except ImportError:
    print("Instale o pywebview: pip install pywebview")
    sys.exit(1)

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-sky-50 to-blue-100 min-h-screen p-3 md:p-6 font-sans">
<div class="max-w-2xl mx-auto">
  <div class="bg-white rounded-2xl shadow-lg p-5 mb-5">
    <h1 class="text-xl md:text-2xl font-bold text-slate-800">Gabarito para Adesivo</h1>
    <p class="text-xs md:text-sm text-slate-400 mb-5">Molde plano para aderir corretamente em copos e baldes cônicos</p>

    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-5">
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1">Diâmetro Topo</label>
        <div class="relative">
          <input type="number" id="d_topo" step="0.1" min="0.1" value="8" class="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-sky-500 focus:border-sky-500 outline-none">
          <span class="absolute right-2.5 top-2 text-slate-400 text-xs">cm</span>
        </div>
      </div>
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1">Diâmetro Base</label>
        <div class="relative">
          <input type="number" id="d_base" step="0.1" min="0.1" value="12" class="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-sky-500 focus:border-sky-500 outline-none">
          <span class="absolute right-2.5 top-2 text-slate-400 text-xs">cm</span>
        </div>
      </div>
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1">Altura</label>
        <div class="relative">
          <input type="number" id="altura" step="0.1" min="0.1" value="15" class="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-sky-500 focus:border-sky-500 outline-none">
          <span class="absolute right-2.5 top-2 text-slate-400 text-xs">cm</span>
        </div>
      </div>
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1">Margem de emenda</label>
        <div class="relative">
          <input type="number" id="margem" step="0.1" min="0" value="0.5" class="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-sky-500 focus:border-sky-500 outline-none">
          <span class="absolute right-2.5 top-2 text-slate-400 text-xs">cm</span>
        </div>
      </div>
    </div>

    <div class="flex gap-2">
      <button onclick="gerar()" class="flex-1 bg-sky-600 hover:bg-sky-700 text-white font-medium py-2.5 px-4 rounded-lg text-sm transition-colors">Gerar Gabarito</button>
      <button onclick="salvar()" class="bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 font-medium py-2.5 px-4 rounded-lg text-sm transition-colors">Salvar SVG</button>
    </div>
  </div>

  <div id="resultado" class="bg-white rounded-2xl shadow-lg p-5">
    <div id="preview" class="flex justify-center items-center min-h-[260px] text-slate-300 text-sm" style="overflow:hidden">Preencha os valores e clique em "Gerar Gabarito"</div>
    <style>
      #preview svg { max-width: 100%; max-height: 65vh; width: auto; height: auto; }
    </style>
    <div id="info" class="mt-4 grid grid-cols-3 md:grid-cols-6 gap-2 text-xs"></div>
  </div>
</div>

<script>
let currentSvg = '';
async function gerar() {
  const d_topo = document.getElementById('d_topo').value;
  const d_base = document.getElementById('d_base').value;
  const altura = document.getElementById('altura').value;
  const margem = document.getElementById('margem').value || '0';
  const result = JSON.parse(await pywebview.api.gerar_gabarito(d_topo, d_base, altura, margem));
  if (result.erro) {
    document.getElementById('preview').innerHTML = '<div class="text-red-500 font-medium">' + result.erro + '</div>';
    document.getElementById('info').innerHTML = '';
    return;
  }
  currentSvg = result.svg;
  document.getElementById('preview').innerHTML = currentSvg;
  const i = result.info;
  document.getElementById('info').innerHTML =
    '<div class="bg-sky-50 rounded-lg p-2"><span class="text-slate-400">Raio maior</span><br><b class="text-base">'+i.R_maior+' cm</b></div>' +
    '<div class="bg-sky-50 rounded-lg p-2"><span class="text-slate-400">Raio menor</span><br><b class="text-base">'+i.R_menor+' cm</b></div>' +
    '<div class="bg-sky-50 rounded-lg p-2"><span class="text-slate-400">Ângulo</span><br><b class="text-base">'+i.angulo+'°</b></div>' +
    '<div class="bg-sky-50 rounded-lg p-2"><span class="text-slate-400">Largura</span><br><b class="text-base">'+i.largura+' cm</b></div>' +
    '<div class="bg-sky-50 rounded-lg p-2"><span class="text-slate-400">Altura</span><br><b class="text-base">'+i.altura+' cm</b></div>' +
    '<div class="bg-sky-50 rounded-lg p-2"><span class="text-slate-400">Área</span><br><b class="text-base">'+i.area+' cm²</b></div>';
}
async function salvar() {
  if (!currentSvg) { alert('Gere um gabarito primeiro'); return; }
  const path = await pywebview.api.salvar_svg(currentSvg);
  if (path) alert('Salvo em: ' + path);
}
</script>
</body>
</html>"""


class Api:
    def gerar_gabarito(self, d_topo_str, d_base_str, altura_str, margem_str="0"):
        try:
            d_topo = float(d_topo_str.replace(",", "."))
            d_base = float(d_base_str.replace(",", "."))
            altura = float(altura_str.replace(",", "."))
            margem = max(0, float(margem_str.replace(",", ".")) if margem_str else 0)
        except (ValueError, AttributeError):
            return json.dumps({"erro": "Valores inválidos"})
        if d_topo <= 0 or d_base <= 0 or altura <= 0:
            return json.dumps({"erro": "Valores devem ser positivos"})
        r_topo, r_base = d_topo / 2, d_base / 2
        d_maior = max(d_topo, d_base)
        d_menor = min(d_topo, d_base)

        if d_topo == d_base:
            # Cilindro: retangulo
            circ = math.pi * d_topo
            scale = 10
            pad = 40
            w_total = (circ + margem) * scale
            cw = w_total + 2 * pad
            ch = altura * scale + 2 * pad
            if margem > 0:
                cm_line = f'<line x1="{pad+circ*scale:.1f}" y1="{pad:.1f}" x2="{pad+circ*scale:.1f}" y2="{pad+altura*scale:.1f}" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5,3"/>'
                cm_lbl = f'<text x="{pad+circ*scale+pad/2:.1f}" y="{pad+altura*scale/2:.1f}" text-anchor="middle" font-size="9" font-family="sans-serif" fill="#d97706">Margem {margem:.1f}cm</text>'
            else:
                cm_line = ''
                cm_lbl = ''
            svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cw:.0f} {ch:.0f}" width="{cw:.0f}mm" height="{ch:.0f}mm">
<rect width="100%" height="100%" fill="#ffffff"/>
<rect x="{pad:.0f}" y="{pad:.0f}" width="{(circ+margem)*scale:.0f}" height="{altura*scale:.0f}" fill="#e0f2fe" fill-opacity="0.6" stroke="#0284c7" stroke-width="2.5" rx="4"/>
{cm_line}
{cm_lbl}
<text x="{pad+w_total/2:.1f}" y="{pad-12:.1f}" text-anchor="middle" font-size="12" font-family="sans-serif" fill="#0284c7" font-weight="bold">Circunferência = {circ:.1f} cm</text>
<text x="{pad+w_total/2:.1f}" y="{pad+altura*scale+20:.1f}" text-anchor="middle" font-size="12" font-family="sans-serif" fill="#0284c7" font-weight="bold">Altura = {altura:.1f} cm</text>
</svg>"""
            largura = circ + margem
            return json.dumps({
                "svg": svg,
                "info": {
                    "R_maior": "-",
                    "R_menor": "-",
                    "angulo": "-",
                    "largura": f"{largura:.1f}",
                    "altura": f"{altura:.1f}",
                    "area": f"{largura*altura:.1f}",
                },
            })

        H_full = altura * d_base / (d_base - d_topo)
        S_base = math.hypot(r_base, H_full)
        S_topo = math.hypot(r_topo, H_full - altura)
        theta_rad = math.pi * d_base / S_base
        theta_deg = theta_rad * 180 / math.pi

        # Sempre mapeia raio maior no arco externo
        if d_topo < d_base:
            S_outer, S_inner = S_base, S_topo
            lbl_outer, lbl_inner = f"BASE ({d_base:.1f} cm)", f"TOPO ({d_topo:.1f} cm)"
        else:
            S_outer, S_inner = S_topo, S_base
            lbl_outer, lbl_inner = f"TOPO ({d_topo:.1f} cm)", f"BASE ({d_base:.1f} cm)"

        sin_h = math.sin(theta_rad / 2)
        cos_h = math.cos(theta_rad / 2)

        # Margem de emenda
        theta_marg = margem / S_outer if margem > 0 and S_outer > 0 else 0
        sin_e = math.sin(theta_rad / 2 + theta_marg)
        cos_e = math.cos(theta_rad / 2 + theta_marg)

        scale = 10
        pad = 50

        So = S_outer * scale
        Si = S_inner * scale

        left_w = So * sin_h
        right_w = So * (sin_e if margem > 0 else sin_h)
        shape_w = left_w + right_w
        shape_h = So - Si * cos_h
        cw = shape_w + 2 * pad
        ch = shape_h + 2 * pad
        cx = pad + left_w
        cy = pad + So

        # Pontos originais
        x_ro = cx + So * sin_h
        y_ro = cy - So * cos_h
        x_lo = cx - So * sin_h
        y_lo = cy - So * cos_h
        x_ri = cx + Si * sin_h
        y_ri = cy - Si * cos_h
        x_li = cx - Si * sin_h
        y_li = cy - Si * cos_h

        la = 1 if (theta_rad + theta_marg) > math.pi else 0

        if margem > 0:
            x_re = cx + So * sin_e
            y_re = cy - So * cos_e
            x_rie = cx + Si * sin_e
            y_rie = cy - Si * cos_e
            full_path = f'M {x_re:.1f},{y_re:.1f} A {So:.1f},{So:.1f} 0 {la},{0} {x_lo:.1f},{y_lo:.1f} L {x_li:.1f},{y_li:.1f} A {Si:.1f},{Si:.1f} 0 {la},{1} {x_rie:.1f},{y_rie:.1f} Z'
            cut_line = f'<line x1="{x_ro:.1f}" y1="{y_ro:.1f}" x2="{x_ri:.1f}" y2="{y_ri:.1f}" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5,3"/>'
            m_label = f'<text x="{(x_ro+x_re)/2:.1f}" y="{(y_ro+y_re)/2:.1f}" text-anchor="middle" font-size="9" font-family="sans-serif" fill="#d97706">Margem {margem:.1f}cm</text>'
        else:
            full_path = f'M {x_ro:.1f},{y_ro:.1f} A {So:.1f},{So:.1f} 0 {la},{0} {x_lo:.1f},{y_lo:.1f} L {x_li:.1f},{y_li:.1f} A {Si:.1f},{Si:.1f} 0 {la},{1} {x_ri:.1f},{y_ri:.1f} Z'
            cut_line = ''
            m_label = ''

        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cw:.0f} {ch:.0f}" width="{cw:.0f}mm" height="{ch:.0f}mm">
<defs>
  <marker id="aS" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="5" markerHeight="5" orient="auto">
    <path d="M 10 0 L 0 5 L 10 10 z" fill="#64748b"/>
  </marker>
  <marker id="aE" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
  </marker>
</defs>
<rect width="100%" height="100%" fill="#ffffff"/>
<path d="{full_path}" fill="#e0f2fe" fill-opacity="0.6" stroke="#0284c7" stroke-width="2.5" stroke-linejoin="round"/>
{cut_line}
{m_label}
<line x1="{cx:.1f}" y1="{cy-So:.1f}" x2="{cx:.1f}" y2="{cy-Si:.1f}" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6,4"/>
<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="#ef4444"/>
<circle cx="{cx:.1f}" cy="{cy:.1f}" r="1.5" fill="#fff"/>
<text x="{cx:.1f}" y="{cy-So-12:.1f}" text-anchor="middle" font-size="12" font-family="sans-serif" fill="#0284c7" font-weight="bold">{lbl_outer}</text>
<text x="{cx:.1f}" y="{cy-Si+20:.1f}" text-anchor="middle" font-size="12" font-family="sans-serif" fill="#0284c7" font-weight="bold">{lbl_inner}</text>
<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x_ro:.1f}" y2="{y_ro:.1f}" stroke="#64748b" stroke-width="1.2" marker-start="url(#aS)" marker-end="url(#aE)"/>
<text x="{(cx+x_ro)/2:.1f}" y="{(cy+y_ro)/2-4:.1f}" text-anchor="middle" font-size="10" font-family="sans-serif" fill="#64748b">R1={S_outer:.1f}cm</text>
<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x_ri:.1f}" y2="{y_ri:.1f}" stroke="#64748b" stroke-width="1" stroke-dasharray="4,3" marker-start="url(#aS)" marker-end="url(#aE)"/>
<text x="{(cx+x_ri)/2:.1f}" y="{(cy+y_ri)/2-4:.1f}" text-anchor="middle" font-size="10" font-family="sans-serif" fill="#64748b">R2={S_inner:.1f}cm</text>
</svg>"""

        return json.dumps({
            "svg": svg,
            "info": {
                "R_maior": f"{S_outer:.1f}",
                "R_menor": f"{S_inner:.1f}",
                "angulo": f"{theta_deg:.1f}",
                "largura": f"{shape_w:.1f}",
                "altura": f"{shape_h:.1f}",
                "area": f"{theta_rad/2*(S_outer**2 - S_inner**2):.1f}",
            },
        })

    def salvar_svg(self, svg_content):
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        path = os.path.join(desktop, "gabarito.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(svg_content)
        return path


if __name__ == "__main__":
    api = Api()
    webview.create_window(
        "Gabarito para Adesivo - Copo/Balde",
        html=HTML,
        js_api=api,
        width=750,
        height=750,
        resizable=True,
    )
    webview.start()
