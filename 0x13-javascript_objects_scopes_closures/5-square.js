#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/*
 * Square class that defines a square and
 * Inherits from rectangle class of 4-rectangle
 */
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
