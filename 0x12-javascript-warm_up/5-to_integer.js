#!/usr/bin/node
const firstArgument = process.argv[2];
const convertedNumber = parseInt(firstArgument, 10);
if (!isNaN(convertedNumber)) {
  console.log(`My number: ${convertedNumber}`);
} else {
  console.log('Not a number');
}
