#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const urlApi = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(urlApi, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
