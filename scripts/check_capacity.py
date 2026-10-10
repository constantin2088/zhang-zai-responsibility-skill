"""Local deterministic aid; never a factual or model behavior certificate."""
import math
def number(x):
 if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<0:raise ValueError('nonnegative finite amount required')
 return x
def analyze(p):
 if not isinstance(p.get('unit'),str) or not p['unit'].strip():raise ValueError('explicit unit required')
 capacity={k:number(v) for k,v in p['capacity'].items()};used={k:0 for k in capacity};ids=set()
 for t in p['tasks']:
  if t['id'] in ids:raise ValueError('duplicate task')
  ids.add(t['id']);owner=t['owner']
  if owner not in used:raise ValueError('owner capacity unknown')
  used[owner]+=number(t['amount'])
 return {'unit':p['unit'],'used':used,'shortfall':{k:max(0,used[k]-capacity[k]) for k in used},'note':'Capacity must be volunteered or otherwise validly established; numbers do not create an obligation.'}

if __name__=='__main__':
 import json,sys
 print(json.dumps(analyze(json.loads(open(sys.argv[1],encoding='utf-8').read())),ensure_ascii=False,indent=2))
