#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor(size) {
    // Call the constructor of Rectangle using super()
    super(size, size);
  }

  charPrint(c) {
    // If c is undefined, use the character X
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
