#!/usr/bin/node

// - Rotate and Double the width and height of the Rectangle

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print (c) {
    c = 'X';
    for (let y = 0; y < this.height; y++) {
      console.log(c.repeat(this.width));
    }
  }
};
