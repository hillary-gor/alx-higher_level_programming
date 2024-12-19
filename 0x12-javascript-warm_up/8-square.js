#!/usr/bin/node

const entry = process.argv;

const size = Math.floor(entry[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
