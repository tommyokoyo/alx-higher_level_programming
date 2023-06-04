#!/usr/bin/node
const rectangle = require('./4-rectangle');

/*
 * Square class that defines a square and
 * Inherits from rectangle class of 4-rectangle
 */
module.exports = class square extends rectangle {
  constructor (size) {
    super(size, size);
  }
};
