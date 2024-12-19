#!/usr/bin/node

const entry = process.argv;
const xValue = parseInt(entry[2]);

function factorial (xValue) {
  if (xValue <= 1) {
    return 1;
  } else {
    return xValue * factorial(xValue - 1);
  }
}

if (isNaN(xValue)) {
  console.log(1);
} else {
  console.log(factorial(xValue));
}
