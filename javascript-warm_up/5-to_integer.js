#!/usr/bin/node

const firstArg = process.argv[2];
const num = parseInt(firstArg, 10);

if (!isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
