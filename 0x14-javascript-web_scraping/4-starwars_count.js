#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const nb = JSON.parse(body).results.filter((elem) => {
    return elem.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(nb);
});
