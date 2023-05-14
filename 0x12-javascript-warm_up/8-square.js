#!/usr/bin/node

// Prints a square
if (isNaN(process.argv[2])) {
    console.log('Missing size');
} else { 
    for (let n = 0; n < parseInt(process.argv[2]); n++) {
        console.log('X'.repeat(parseInt(process.argv[2])));
    }
}
