#!/usr/bin/node
// Rectangle class that has a constructor with height and width
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
	  cons temp = this.height;
	  this.height = this.width;
	  this.width = temp;
  }

  double () {
	  this.width *= 2;
	  this.height *= 2;
  }
}

module.exports = Rectangle;
