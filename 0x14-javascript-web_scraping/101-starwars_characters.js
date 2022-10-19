#!/usr/bin/node

const request = require('request');
const id = (process.argv)[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

function processRequest (reqArr, index) {
  if (index === reqArr.length) {
    return;
  }
  request(reqArr[index], (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const actor = JSON.parse(body);
    console.log(actor.name);
    processRequest(reqArr, index + 1);
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  processRequest(characters, 0);
});
