#!/usr/bin/node
// Creates a class Rectangle that defines a rectangle
// Initialize the widht and height
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
