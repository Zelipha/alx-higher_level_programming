#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');
const args = process.argv.slice(1);
const movie = 'https://swapi-api.hbtn.io/api/films/' + args[1];

request(movie, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
