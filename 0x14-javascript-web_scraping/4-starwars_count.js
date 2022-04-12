#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const args = process.argv.slice(1);
request(args[1], (error, response, body) => {
  let total = 0;
  const actor = 'https://swapi-api.hbtn.io/api/people/18/';
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    for (const res of result) {
      const character = res.characters;
      for (const car of character) {
        if (car === actor) {
          total = total + 1;
        }
      }
    }
  }
  console.log(total);
});
