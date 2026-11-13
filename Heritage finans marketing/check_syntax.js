const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

const regex = /<script(?:\s+[^>]*)?>([\s\S]*?)<\/script>/gi;
let match;
let scriptIdx = 0;

while ((match = regex.exec(html)) !== null) {
  const code = match[1].trim();
  if (!code) continue;
  scriptIdx++;
  console.log(`Checking script #${scriptIdx} (length: ${code.length})...`);
  try {
    new Function(code);
    console.log(`Script #${scriptIdx} syntax OK!`);
  } catch (err) {
    console.error(`Script #${scriptIdx} SYNTAX ERROR:`, err.message);
  }
}
