"""Validate Plan fixture references/coverage, not system behavior or semantics."""
import json
import re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
script = (root / 'fixtures/lecture-script.md').read_text()
ids = set(re.findall(r'^## (F01-v1-p\d+)', script, re.M))
cases = json.loads((root / 'fixtures/evaluation.json').read_text())

def validate(items):
    errors = []
    seen = set()
    for case in items:
        if case['id'] in seen:
            errors.append('duplicate case ID')
        seen.add(case['id'])
        if not set(case['evidence']).issubset(ids):
            errors.append('unknown evidence ID')
        if not case['expected'] or not case['failure_condition']:
            errors.append('missing acceptance criterion')
    for kind in ('topic', 'relationship', 'missing-evidence', 'contradiction'):
        if not any(c['kind'] == kind for c in items):
            errors.append('missing category: ' + kind)
    return errors

assert not validate(cases), validate(cases)
negative = [dict(c) for c in cases]
negative[0]['evidence'] = ['F01-v1-p99']
assert 'unknown evidence ID' in validate(negative)
negative = cases + [dict(cases[0])]
assert 'duplicate case ID' in validate(negative)
negative = [dict(c) for c in cases]
negative[0]['expected'] = ''
assert 'missing acceptance criterion' in validate(negative)
links = []
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        target_path = (path.parent / target.split('#')[0]).resolve()
        if not target_path.exists():
            links.append(str(path.relative_to(root)) + ': ' + target)
assert not links, links
print(json.dumps({'evaluation_cases': len(cases), 'script_passages': len(ids),
                  'fixture_references': 'pass', 'required_categories': 'pass',
                  'negative_controls_detected': 3, 'local_markdown_targets': 'pass',
                  'system_tests': 'not run', 'semantic_support': 'requires separate review'}, indent=2))
