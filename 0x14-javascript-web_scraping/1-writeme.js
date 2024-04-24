#!/usr/bin/node
// Write to file

const fs = require('fs');

// Check if the correct number of arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file path> "<string to write>"');
  process.exit(1);
}

// Extract the file path and string to write from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write to the file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
