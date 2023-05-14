#!/usr/bin/node

// Scripts that print C on output x number of times
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let n = 1; n <= parseInt(process.argv[2]); n++) {
    console.log('C is fun');
  }
}
