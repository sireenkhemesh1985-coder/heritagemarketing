const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const regex = /<script(?:\s+[^>]*)?>([\s\S]*?)<\/script>/gi;
let match;
let scriptIdx = 0;

while ((match = regex.exec(html)) !== null) {
  const code = match[1].trim();
  if (!code) continue;
  scriptIdx++;
  if (scriptIdx === 2) {
    const lines = code.split('\n');
    for (let i = 820; i <= 835 && i < lines.length; i++) {
      console.log(`${i+1}: ${lines[i]}`);
    }
  }
}
