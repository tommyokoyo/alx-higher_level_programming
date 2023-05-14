#!/usr/bin/node

// Parses for the second biggest interger in a list
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argList = process.argv.sort();
  console.log(argList.reverse()[1]);
}
