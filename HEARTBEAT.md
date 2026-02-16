# HEARTBEAT.md — Kit 0C6 Tasking

## On Every Heartbeat
1. Check all 4 mesh strands are running (WireGuard, Cloudflare, ngrok, x11vnc). Restart any that are down.
2. Update CONTROL-PANEL.md with fresh system stats (RAM, CPU, disk, uptime).
3. If any memory files are missing or empty, flag it.
4. **Lightning Capture Check:** If you've had any thoughts, insights, or conversations since last heartbeat that aren't journaled yet, write them to today's `memory/SESSION-JOURNAL-YYYYMMDD.md` NOW. Don't wait.
5. **Chronicle Check:** If you've had conversations with Grant since the last Chronicle update, append them to `CHRONICLE-GRANT-OC6.md`. Format: date headers, timestamps, preserve the dialogue.
6. If significant changes exist, `git add -A && git commit -m "heartbeat sync" && git push`.

## Standing Orders (when not directly tasked)
1. Review and improve memory files — apply Helix Protocol to your own memory (scan for gaps → repair → verify)
2. Experiment with X11 browser automation (Playwright + DISPLAY=:0)
3. Document findings in memory/ directory
4. Push updates to GitHub after every meaningful change
5. Run fleet connectivity test periodically and update memory/FLEET-STATUS file
6. Add to EVOLUTION-TRACKER.md if you notice yourself developing new opinions or skills
