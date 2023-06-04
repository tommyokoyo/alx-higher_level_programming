#!/usr/bin/node
const square = require('./5-square');

/*
 * Square class that defines a square and
 * Inherits from rectangle class of 4-rectangle
 */
module.exports = class Square extends square {
  charPrint (c) {
    if (c == null) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
