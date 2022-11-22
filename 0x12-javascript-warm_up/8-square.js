#!/usr/bin/node
const { argv } = require('process');
if (!parseInt(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    let square = '';
    for (let y = 0; y < parseInt(argv[2]); y++) {
      square += 'X';
    }
    console.log(square);
  }
}
