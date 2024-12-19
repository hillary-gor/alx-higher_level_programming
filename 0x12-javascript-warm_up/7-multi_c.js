#!/usr/bin/node

const entry = process.argv;

const xValue = Math.floor(entry[2]);
if (isNaN(xValue)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < xValue; i++) {
    console.log('C is fun');
  }
}
