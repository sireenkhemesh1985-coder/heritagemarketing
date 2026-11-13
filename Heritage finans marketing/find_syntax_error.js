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
    console.log(`Total lines in script #2: ${lines.length}`);
    
    // Binary search or line-by-line test to find the exact invalid token
    for (let i = 1; i <= lines.length; i++) {
      const partial = lines.slice(0, i).join('\n');
      try {
        // We wrap in a dummy function or parse
        // Since an incomplete function might throw Unexpected end of input,
        // we check for 'Invalid or unexpected token' specifically!
      } catch (e) {
      }
    }

    // Let's use vm.runInContext or babel or acorn or standard eval on small chunks
    const vm = require('vm');
    try {
      new vm.Script(code);
    } catch (err) {
      console.log('Error stack:', err.stack);
      console.log('Line info:', err.lineNumber, err.columnNumber);
    }
  }
}
