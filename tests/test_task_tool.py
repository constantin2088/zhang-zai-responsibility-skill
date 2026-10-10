import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_capacity import analyze
class TaskToolTests(unittest.TestCase):
 def sample(self):return json.loads((ROOT/'examples/tool-input.json').read_text(encoding='utf-8'))
 def test_overload_visible(self):self.assertEqual(analyze(self.sample())['shortfall']['A'],1)
 def test_distributing_work_changes_gap(self):
  p=self.sample();p['tasks'][1]['owner']='B';self.assertEqual(sum(analyze(p)['shortfall'].values()),0)
 def test_no_assumed_capacity(self):
  p=self.sample();p['tasks'][0]['owner']='unknown'
  with self.assertRaises(ValueError):analyze(p)
 def test_negative_resource_not_a_credit(self):
  p=self.sample();p['tasks'][0]['amount']=-3
  with self.assertRaises(ValueError):analyze(p)
 def test_unit_not_silent(self):
  p=self.sample();p['unit']=''
  with self.assertRaises(ValueError):analyze(p)

if __name__=='__main__':unittest.main()
