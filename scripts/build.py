"""Arma data/perfumes.json y la página final index.html.

Uso:  python -I scripts/build.py <ruta a fra_cleaned.csv> [cantidad]

Fuente del CSV: conjunto de datos público de Fragrantica (copia en GitHub:
https://github.com/lyudmil-apostolov/Fragrance-project/blob/main/data/fra_cleaned.csv).
Popularidad = cantidad de votos ("Rating Count") en Fragrantica.
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from es import ACCORDS, ACCORD_GROUP, NOTES  # noqa: E402
from names import brand_name, perfume_name  # noqa: E402

GENDER = {'women': 'M', 'men': 'H', 'unisex': 'U'}  # Mujer, Hombre, Unisex
WEIGHTS = [5, 4, 3, 2, 1]


def to_int(x):
    x = (x or '').replace(',', '').replace('.', '').strip()
    return int(x) if x.isdigit() else 0


def notes(field):
    out = []
    for t in (field or '').split(','):
        t = t.strip()
        if t and t != 'unknown':
            es = NOTES.get(t, t)
            if es not in out:
                out.append(es)
    return out


def family(accords):
    score = {'F': 0.0, 'L': 0.0, 'M': 0.0, 'O': 0.0}
    for w, a in zip(WEIGHTS, accords):
        for g, share in ACCORD_GROUP.get(a, {}).items():
            score[g] += w * share
    return max(score, key=lambda g: (score[g], g == 'L'))


def main():
    csv_path = Path(sys.argv[1])
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    text = csv_path.read_bytes().decode('cp1252')
    rows = list(csv.DictReader(text.splitlines(), delimiter=';'))
    rows.sort(key=lambda r: -to_int(r['Rating Count']))
    data = []
    for i, r in enumerate(rows[:limit]):
        accords = [r[f'mainaccord{k}'].strip() for k in range(1, 6) if r[f'mainaccord{k}'].strip()]
        rating = r['Rating Value'].replace(',', '.')
        data.append({
            'r': i + 1,
            'n': perfume_name(r['Brand'], r['Perfume']),
            'b': brand_name(r['Brand']),
            'g': GENDER.get(r['Gender'], 'U'),
            'y': int(r['Year']) if r['Year'].isdigit() else None,
            'f': family(accords),
            'a': [ACCORDS.get(a, a) for a in accords],
            't': notes(r['Top']),
            'm': notes(r['Middle']),
            's': notes(r['Base']),
            'v': to_int(r['Rating Count']),
            'p': float(rating) if rating else None,
            'u': r['url'].split('/perfume/', 1)[-1],
        })
    (ROOT / 'data').mkdir(exist_ok=True)
    js = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    (ROOT / 'data' / 'perfumes.json').write_text(js, encoding='utf-8')
    tpl = (ROOT / 'src' / 'template.html').read_text(encoding='utf-8')
    marker = '/*__DATA__*/[]'
    assert marker in tpl, 'falta el marcador de datos en src/template.html'
    html = tpl.replace(marker, js.replace('</', '<\\/'))
    (ROOT / 'index.html').write_text(html, encoding='utf-8')
    fams = {}
    for d in data:
        fams[d['f']] = fams.get(d['f'], 0) + 1
    print(f'{len(data)} perfumes; familias {fams}; html {len(html) // 1024} KB')


if __name__ == '__main__':
    main()
