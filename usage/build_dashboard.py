#!/usr/bin/env python3
import csv, pathlib, html, datetime

base = pathlib.Path('/home/thewindstorm/.openclaw/workspace/usage')
csv_path = base / 'usage-log.csv'
out_path = base / 'usage-dashboard.html'

rows = []
if csv_path.exists():
    with csv_path.open() as f:
        rows = list(csv.DictReader(f))

if not rows:
    out_path.write_text('<h1>No usage data yet</h1><p>Run collect_usage.py first.</p>')
    print('No rows, wrote placeholder dashboard.')
    raise SystemExit(0)

# Keep last 200 points for chart clarity
rows = rows[-200:]

# Extract series
ctx = []
q5 = []
qd = []
labels = []
for r in rows:
    labels.append(r.get('timestamp',''))
    def to_num(v):
        try:
            return float(v)
        except:
            return None
    ctx.append(to_num(r.get('context_used_pct')))
    q5.append(to_num(r.get('quota_5h_used_pct')))
    qd.append(to_num(r.get('quota_day_used_pct')))

def polyline_points(vals, width=960, height=260, pad=24):
    pts = []
    n = len(vals)
    if n <= 1:
        return ''
    for i,v in enumerate(vals):
        if v is None:
            continue
        x = pad + (i*(width-2*pad)/(n-1))
        y = pad + ((100-v)*(height-2*pad)/100)
        pts.append(f"{x:.1f},{y:.1f}")
    return ' '.join(pts)

ctx_pts = polyline_points(ctx)
q5_pts = polyline_points(q5)
qd_pts = polyline_points(qd)

latest = rows[-1]
now = datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')

html_doc = f'''<!doctype html>
<html><head><meta charset="utf-8"><title>Anti-Gravity Usage Dashboard</title>
<style>
body{{font-family:system-ui,Segoe UI,Arial;margin:24px;background:#0b1020;color:#e6edf3}}
.card{{background:#11182c;border:1px solid #26324a;border-radius:12px;padding:16px;margin:12px 0}}
.kpi{{display:grid;grid-template-columns:repeat(3,minmax(160px,1fr));gap:12px}}
.k{{background:#0f1527;border:1px solid #26324a;border-radius:10px;padding:12px}}
small{{color:#9fb0c8}}
a{{color:#7cc5ff}}
</style></head><body>
<h1>Anti-Gravity / OpenClaw Usage Dashboard</h1>
<small>Updated {html.escape(now)} · source: openclaw status --usage --json</small>
<div class="card kpi">
  <div class="k"><div><small>Model</small></div><div>{html.escape(str(latest.get('model','')))}</div></div>
  <div class="k"><div><small>Context Used</small></div><div>{latest.get('context_used_pct','?')}%</div></div>
  <div class="k"><div><small>Context Remaining</small></div><div>{latest.get('context_remaining','?')} tokens</div></div>
  <div class="k"><div><small>5h Quota Used</small></div><div>{latest.get('quota_5h_used_pct','?')}%</div></div>
  <div class="k"><div><small>Day Quota Used</small></div><div>{latest.get('quota_day_used_pct','?')}%</div></div>
  <div class="k"><div><small>Samples</small></div><div>{len(rows)}</div></div>
</div>
<div class="card">
<h3>Usage Trend (last {len(rows)} samples)</h3>
<svg viewBox="0 0 960 260" width="100%" height="260" style="background:#0a0f1f;border-radius:8px;border:1px solid #26324a">
  <line x1="24" y1="24" x2="24" y2="236" stroke="#445"/>
  <line x1="24" y1="236" x2="936" y2="236" stroke="#445"/>
  <text x="930" y="20" fill="#8aa" font-size="12">100%</text>
  <text x="930" y="240" fill="#8aa" font-size="12">0%</text>
  <polyline points="{ctx_pts}" fill="none" stroke="#6ee7b7" stroke-width="2"/>
  <polyline points="{q5_pts}" fill="none" stroke="#60a5fa" stroke-width="2"/>
  <polyline points="{qd_pts}" fill="none" stroke="#f59e0b" stroke-width="2"/>
</svg>
<p><small>Green = context used %, Blue = 5h quota used %, Orange = day quota used %</small></p>
</div>
<div class="card">
<h3>Files</h3>
<ul>
<li><code>{csv_path}</code></li>
<li><code>{base / 'last-status-usage.json'}</code></li>
</ul>
</div>
</body></html>'''

out_path.write_text(html_doc)
print('Wrote', out_path)
