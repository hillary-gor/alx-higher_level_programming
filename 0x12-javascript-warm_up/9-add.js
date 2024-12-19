#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const entry = process.argv;
const valueB = parseInt(entry[3]);
const valueA = parseInt(entry[2]);

add(valueA, valueB);
