#!/usr/bin/env python3
import csv, json, subprocess, datetime, pathlib, sys

base = pathlib.Path('/home/thewindstorm/.openclaw/workspace/usage')
base.mkdir(parents=True, exist_ok=True)
log_csv = base / 'usage-log.csv'
status_json = base / 'last-status-usage.json'

try:
    out = subprocess.check_output(['openclaw', 'status', '--usage', '--json'], text=True)
except Exception as e:
    print(f'ERROR: failed to run openclaw status --usage --json: {e}')
    sys.exit(1)

data = json.loads(out)
status_json.write_text(json.dumps(data, indent=2))

now = datetime.datetime.now().astimezone()
ts = now.isoformat()

# Defaults
model = ''
context_total = ''
context_used = ''
context_used_pct = ''
context_remaining = ''
quota_5h_pct = ''
quota_5h_reset = ''
quota_day_pct = ''
quota_day_reset = ''

recent = data.get('sessions', {}).get('recent', [])
main = None
for s in recent:
    if s.get('key') == 'agent:main:main':
        main = s
        break
if main is None and recent:
    main = recent[0]

if main:
    model = main.get('model', '')
    context_total = main.get('contextTokens', '')
    context_used_pct = main.get('percentUsed', '')
    context_remaining = main.get('remainingTokens', '')
    if isinstance(context_total, int) and isinstance(context_remaining, int):
        context_used = context_total - context_remaining

for p in data.get('usage', {}).get('providers', []):
    if p.get('provider') in ('openai-codex', 'anthropic', 'google'):
        for w in p.get('windows', []):
            if w.get('label') == '5h':
                quota_5h_pct = w.get('usedPercent', '')
                quota_5h_reset = w.get('resetAt', '')
            elif w.get('label') == 'Day':
                quota_day_pct = w.get('usedPercent', '')
                quota_day_reset = w.get('resetAt', '')

header = [
    'timestamp','model','context_total','context_used','context_used_pct','context_remaining',
    'quota_5h_used_pct','quota_5h_reset_at_ms','quota_day_used_pct','quota_day_reset_at_ms'
]
row = [
    ts, model, context_total, context_used, context_used_pct, context_remaining,
    quota_5h_pct, quota_5h_reset, quota_day_pct, quota_day_reset
]

write_header = not log_csv.exists()
with log_csv.open('a', newline='') as f:
    w = csv.writer(f)
    if write_header:
        w.writerow(header)
    w.writerow(row)

print('Logged usage snapshot to', log_csv)
