#!/usr/bin/node
/*
 * script that prints two arguments passed to it, in the following format: “ is ”
 */
const myArgs = process.argv;
// print process.argv
let count = 0;
let i = 0;
myArgs.forEach((val, index) => {
  // console.log(`${index}: ${val}`);
  count += 1;
});
console.log(myArgs[2] + ' is ' + myArgs    [3]);
