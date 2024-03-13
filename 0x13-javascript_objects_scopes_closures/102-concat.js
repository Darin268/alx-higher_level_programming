#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileAPath = args[0];
const fileBPath = args[1];
const destFilePath = args[2];

try {
  const fileAContent = fs.readFileSync(fileAPath, 'utf8');
  const fileBContent = fs.readFileSync(fileBPath, 'utf8');

  const concatenatedContent = `${fileAContent}${fileBContent}`;

  fs.writeFileSync(destFilePath, concatenatedContent);

  console.log(`Files ${fileAPath} and ${fileBPath} concatenated to ${destFilePath}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exit(1);
}
