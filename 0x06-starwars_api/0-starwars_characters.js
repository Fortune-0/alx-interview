#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Changed MovieId to movieId
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`; // Changed apiurl to apiUrl

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie:', error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach(url => {
    request(url, (error, response, body) => { // Changed response to request
      if (error) {
        console.error('Error fetching character:', error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
