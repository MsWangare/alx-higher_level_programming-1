#!/usr/bin/node

const argv = require('process').argv;

const nums = [];

for (let i = 2; i < argv.length; i++) {
  nums.push(parseInt(argv[i]));
}

nums.sort((a, b) => a - b);

if (nums.length < 2) {
  console.log('0');
} else {
  console.log(nums[nums.length - 2]);
}
