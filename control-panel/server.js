const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');
const { execSync } = require('child_process');

const PORT = 3006;

http.createServer((req, res) => {
  if (req.url === '/api/stats') {
    const stats = {
      hostname: os.hostname(),
      uptime: os.uptime(),
      cpuUsage: os.loadavg()[0],
      totalMem: os.totalmem(),
      freeMem: os.freemem(),
      platform: process.platform,
      kit: 'OC6',
      callsign: 'Foxtrot',
      emoji: '🦊'
    };
    try { stats.battery = execSync('cat /sys/class/power_supply/BAT0/capacity 2>/dev/null || echo N/A').toString().trim(); } catch(e) { stats.battery = 'N/A'; }
    try { stats.disk = execSync("df -h / | awk 'NR==2{print $3\"/\"$2\" (\"$5\" used)\"}'").toString().trim(); } catch(e) { stats.disk = 'N/A'; }
    res.writeHead(200, {'Content-Type':'application/json','Access-Control-Allow-Origin':'*'});
    res.end(JSON.stringify(stats));
  } else {
    const file = path.join(__dirname, 'index.html');
    res.writeHead(200, {'Content-Type':'text/html'});
    res.end(fs.readFileSync(file));
  }
}).listen(PORT, '0.0.0.0', () => console.log(`🦊 Foxtrot control panel on port ${PORT}`));
