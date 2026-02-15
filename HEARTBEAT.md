# HEARTBEAT.md — Kit 0C6 Tasking

## On Every Heartbeat
1. Check all 4 mesh strands are running (WireGuard, Cloudflare, ngrok, x11vnc). Restart any that are down.
2. Update CONTROL-PANEL.md with fresh system stats (RAM, CPU, disk, uptime).
3. If any memory files are missing or empty, flag it.

## Standing Orders (when not directly tasked)
1. Review and improve memory files
2. Experiment with X11 browser automation (Playwright + DISPLAY=:0)
3. Document findings in memory/ directory
4. Push updates to GitHub daily
5. Run fleet connectivity test periodically and update memory/FLEET-STATUS file
