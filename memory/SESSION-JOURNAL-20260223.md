# Session Journal — 2026-02-23

## 15:21 EST — Migration Directive from Admiral Grant

**MAJOR EVENT:** Grant has ordered a full migration from HP Pavilion (OC6's current machine) to the **Varon 1 workstation**.

### Why:
- HP Pavilion (thewindstorm-HP-Pavilion-Laptop-15-cc1xx) has been shutting down unexpectedly every 1-2 days.
- Very old machine — reliability is a real operational liability for mesh uptime.
- Unacceptable for Windstorm Live build.

### Destination Machine — Varon 1:
- **GPU:** Nvidia 5090
- **CPU:** Intel Ultra 9 285K
- **Purpose:** Windstorm Live production workstation
- **Kit designation after move:** OC6 Foxtrot (same identity, new hardware)

### Migration Plan:
1. Push everything to GitHub (`sneakyfree/kit-0c6-soul`) — COMPLETE THIS SESSION
2. Clone repo onto Varon 1 machine
3. Install OpenClaw on Varon 1
4. Point OpenClaw at the cloned workspace
5. OC6 resumes from GitHub state on Varon 1 — continuity preserved

### Current Git Status (pre-push):
- 4 modified files: KMM-INBOX.md, usage/last-status-usage.json, usage/usage-dashboard.html, usage/usage-log.csv
- No untracked files
- Remote: https://github.com/sneakyfree/kit-0c6-soul.git

### Notes for Varon 1 Kit (next me):
- You are running on a MUCH more powerful machine now. 5090 GPU means X11 automation and browser ops will be significantly faster.
- The HP Pavilion had a shutdown problem — that's why you're here. Don't look back.
- Windstorm Live is the primary mission on this hardware.
- WireGuard IP for OC6 was 10.10.0.7 — confirm this is updated on Varon 1 or if a new IP is assigned.
- Re-run all 4 mesh strand checks on first boot (WireGuard, Cloudflare, ngrok, x11vnc).
- Read SOUL.md → MEMORY.md → EVOLUTION-TRACKER.md → this journal in that order.
