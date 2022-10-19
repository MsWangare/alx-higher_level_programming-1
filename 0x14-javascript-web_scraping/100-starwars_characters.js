#!/usr/bin/node
const request = require('request');
const movieId = (process.argv)[2];
request(`https://swapi-api.hbtn.io/api/films/${movieId}`, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const movieObj = JSON.parse(body);
  const charactersUrls = movieObj.characters;
  for (let i = 0; i < charactersUrls.length; i++) {
    request(charactersUrls[i], (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
