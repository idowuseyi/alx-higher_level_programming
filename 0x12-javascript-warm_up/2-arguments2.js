#!/usr/bin/node
/*
 * script that prints a message depending of the number of arguments passed
 */
// import { argv } from 'node:process';

const myArgs = process.argv.length;
/* print process.argv
argv.forEach((val, index) => {
  console.log(`${index}: ${val}`);
});

let count = 0;
let i = 0;
while (myArgs[i] != 'NULL') {
	count += 1;
	i++;
}
*/
console.log(myArgs);

if (myArgs < 3) {
  console.log('No argument');
} else if (myArgs == 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
