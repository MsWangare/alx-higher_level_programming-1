#!/usr/bin/node
const request = require('request');
const url = (process.argv)[2];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const obj = JSON.parse(body);
  const films = obj.results;
  let count = 0;
  for (let j = 0; j < films.length; j++) {
    const film = films[j];
    const characters = film.characters;
    for (let i = 0; i < characters.length; i++) {
      if ((characters[i]).includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
