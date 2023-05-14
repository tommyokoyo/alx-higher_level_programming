#!/usr/bin/node

// Computes and prints the factorial
function factorial (number) {
  if ((isNaN(number)) || (number === 1)) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
