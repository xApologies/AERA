from pathlib import Path
import csv, json, hashlib, collections
r=Path(__file__).resolve().parent
manifest=json.loads((r/'MANIFEST.json').read_text())
for p,h in manifest.items():
 assert hashlib.sha256((r/p).read_bytes()).hexdigest()==h,p
with (r/'payload/L1/SHAPINGS/SHAPINGS_MASTER.csv').open(encoding='utf-8-sig',newline='') as f:
 reader=csv.DictReader(f); rows=list(reader); assert len(reader.fieldnames)==65
assert len(rows)==1245 and len({x['mk727_card_id'] for x in rows})==1245
assert collections.Counter(x['record_type'] for x in rows)=={'INDUSTRIAL_BINDING':1016,'SUMMON':229}
for x in rows:
 b=json.loads(x['required_basins']); assert b and len(b)==len(set(b)) and set(b)<=set('Red Orange Yellow Green Blue Violet'.split()),x['mk727_card_id']
assert collections.Counter(len(json.loads(x['required_basins'])) for x in rows)=={1:1,2:352,3:799,4:93}
assert json.loads(next(x for x in rows if x['source_id']=='DG-0031')['required_basins'])==['Orange','Yellow','Blue','Violet']
assert hashlib.sha256((r/'payload/L1/SHAPINGS/SHAPINGS_MASTER.csv').read_bytes()).hexdigest()=='4e7d13925b024f679aca369a08a8ca2b064b4794cde3654431e28bee531edab3'
assert len(list(r.rglob('*.csv')))==1
print('PASS: hashes, 1245 unique records, 65 columns, basin distribution, CSR, single master CSV, byte preservation')
