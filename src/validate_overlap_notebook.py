import json, ast
from pathlib import Path
p=Path('/home/ubuntu/work/KneE_PAD_Overlap_Error1_Final_SelfContained.ipynb')
nb=json.loads(p.read_text(encoding='utf-8'))
assert nb.get('nbformat')==4
errs=[]
for i,c in enumerate(nb['cells']):
    if c.get('cell_type')=='code':
        src=''.join(c.get('source',[]))
        try: ast.parse(src)
        except Exception as e: errs.append((i,str(e)))
print('cells',len(nb['cells']),'code_cells',sum(c.get('cell_type')=='code' for c in nb['cells']))
if errs:
    print('ERRORS',errs); raise SystemExit(1)
print('JSON and all code-cell syntax: OK')
print('external_script_imports:', [line for c in nb['cells'] if c.get('cell_type')=='code' for line in ''.join(c.get('source',[])).splitlines() if 'import ' in line and not line.startswith(('import os','import json','import random','import warnings','from pathlib','from scipy','from sklearn','import numpy','import pandas','import matplotlib','import seaborn'))])
