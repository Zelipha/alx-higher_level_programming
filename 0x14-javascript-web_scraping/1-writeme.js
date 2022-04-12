#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(file, string, 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
