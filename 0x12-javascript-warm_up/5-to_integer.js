#!/usr/bin/node
/*
 * script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
 */
const arg = process.argv;
let usedArg = parseInt(arg[2]);
if (isNaN(usedArg)) {
	console.log('Not a number');
} else { 
	console.log('My number: ', usedArg);
}
