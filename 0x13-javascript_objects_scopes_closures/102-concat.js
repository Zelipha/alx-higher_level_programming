#!/usr/bin/node

const fs = require('fs');

// Read from each file
const a = fs.readFileSync(process.argv[2], 'utf8');
const b = fs.readFileSync(process.argv[3], 'utf8');

// Write the concatenated content
fs.writeFileSync(process.argv[4], a + b);
