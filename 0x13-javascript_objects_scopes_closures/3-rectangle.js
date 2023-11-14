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
		  let sum = "";
		  for (let j = 0; j < this.width; j++) sum += "X";

		  console.log(sum);
	  } 
  }
}

module.exports = Rectangle;
