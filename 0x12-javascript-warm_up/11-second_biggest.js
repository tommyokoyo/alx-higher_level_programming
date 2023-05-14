#!/usr/bin/node

// Parses for the second biggest interger in a list
if (process.argv.length <= 3) {
    console.log(0);
} else {
    const args_list = process.argv.sort();
    console.log(args_list.reverse()[1]);
}
