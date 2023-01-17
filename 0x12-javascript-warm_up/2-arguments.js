#!/usr/bin/node
/*
 * script that prints a message depending of the number of arguments passed
 */
const myArgs = process.argv.length;

if (myArgs < 3) {
  console.log('No argument');
} else if (myArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
