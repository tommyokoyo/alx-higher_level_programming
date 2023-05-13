#!/usr/bin/node

// Scripts that print C on output x number of times
if (isNaN(process.argv[2])) {
  for (let n = 1; n <= parseInt(process.argv[2]); n++) {
    console.log('C is fun”');
  }
} else {
  console.log('Missing number of occurrences');
}
