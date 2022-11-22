#!/usr/bin/node
const { argv } = require('process');
let num = parseInt(argv[2]);
if (isNaN(num)) {
  num = 0;
}

function factorial (n) {
  if (n === 0) { return 1; }
  return n * factorial(n - 1);
}

console.log(factorial(num));
