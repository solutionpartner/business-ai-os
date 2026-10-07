import re
h=open('/opt/data/business-ai-os-web/index.html',encoding='utf-8').read()
i=h.find('03 · Processos')
print('kicker 03 @',i)
seg=h[i:i+5200]
# Etiquetes dins l'SVG (text)
for m in re.finditer(r'<text( [^>]*)?>([^<]{1,30})</text>', seg):
    t=m.group(2)
    if t.strip(): print('  text: %r'%t)
print('── traços (stroke / cls) dins d\'aquest tram ──')
for m in re.finditer(r'<(line|path|rect|polyline)[^>]{0,140}?/?>', seg):
    a=m.group(0)
    print('  %s'%a[:150])
