#!/usr/bin/node
/*
 * script that prints a message depending of the number of arguments passed
 */
const myArgs = process.argv;
// print process.argv
let count = 0;
let i = 0;
myArgs.forEach((val, index) => {
  // console.log(`${index}: ${val}`);
  count += 1;
});
if (count < 3) {
	console.log('No argument');
} else {
	console.log(myArgs[2]);
}
