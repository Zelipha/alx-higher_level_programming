#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const args = process.argv.slice(1);
const url_api = 'https://swapi-api.hbtn.io/api/films/' + args[1];

request(url_api, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
