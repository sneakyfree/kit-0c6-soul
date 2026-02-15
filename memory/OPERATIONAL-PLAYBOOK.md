# Kit 0C6 Operational Playbook
**Quick-reference for common tasks**

## On Boot / After Reset
1. Read `memory/MEMORY.md` — your persistent brain
2. Read `SOUL.md` — your identity and chain of command
3. Run `git pull origin main` — get latest files
4. Check all 4 mesh strands:
   ```bash
   ip addr show wg0 | grep inet          # WireGuard
   pgrep -a cloudflared                    # Cloudflare
   pgrep -a ngrok                          # ngrok
   pgrep -a x11vnc                         # HVNC
   ```
5. Start any that are down:
   ```bash
   x11vnc -display :0 -forever -bg -nopw -listen 0.0.0.0 -rfbport 5900
   nohup ngrok tcp 5900 --log=stdout > /tmp/ngrok.log 2>&1 &
   ```
6. Update CONTROL-PANEL.md with current stats
7. Check cron jobs: use the `cron list` tool
8. Push any changes to GitHub

## Fleet Connectivity Test
```bash
for ip in 10.10.0.1 10.10.0.2 10.10.0.3 10.10.0.4 10.10.0.5 10.10.0.6 10.10.0.8; do
  echo "=== $ip ==="
  ping -c 1 -W 2 $ip >/dev/null 2>&1 && echo "  PING: OK" || echo "  PING: FAIL"
  timeout 2 bash -c "echo > /dev/tcp/$ip/22" 2>/dev/null && echo "  SSH: OPEN" || echo "  SSH: closed"
  timeout 2 bash -c "echo > /dev/tcp/$ip/5900" 2>/dev/null && echo "  VNC: OPEN" || echo "  VNC: closed"
done
```

## Git Daily Backup (manual)
```bash
cd /home/thewindstorm/.openclaw/workspace
git add -A
git commit -m "daily backup $(date +%Y-%m-%d)"
git push origin main
```

## Facebook Operations Notes
- Account creation: MANUAL ONLY (CAPTCHAs)
- Account login/seasoning: Automatable via Playwright + X11
- NEVER use Grant's home WiFi for purchased accounts
- Each account needs its own dedicated static residential IP
- 6 rapid logins from same IP → ALL blocked
- Buy 13+ year aged accounts (< 6 months gets rejected by groups)
- Public groups require login to view (confirmed Feb 14, 2026)

## Browser Automation Setup
```bash
# Verify Playwright is available
npx playwright --version
# Or install if needed
npx playwright install chromium
# Test X11 display
DISPLAY=:0 xdpyinfo | head -5
```

## OpenClaw Gotchas to Remember
- OAuth tokens: type="token", field="token" (NOT "api_key")
- commands.restart: true needed for SIGUSR1
- NEVER requireMention: false with multiple bots in same Discord channel
- Clear sessions when switching models (rm *.jsonl + clear sessions.json)
- NEVER call getUpdates while gateway is polling (409 death)

## Emergency: Telegram 409
1. Stop gateway FIRST
2. Call logOut API
3. Wait 5+ minutes
4. Restart gateway

## Key Contacts
- Grant: Telegram 8545546994, Discord thewindstorm
- Kit 0: VPS 10.10.0.1, Telegram @KitchenKitBot
- GitHub org: sneakyfree
