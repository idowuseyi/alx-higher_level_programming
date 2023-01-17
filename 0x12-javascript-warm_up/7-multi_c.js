#!/usr/bin/node
/*
 * script that prints x times “C is fun”
 */
const arg = process.argv;
const x = Number(arg[2]);
console.log(typeof (x));
let i = 0;
while (i < x) {
  if (typeof (x) === 'number') {
    console.log('C is fun');
  } else {
    console.log('Missing number of occurrences');
    break;
  }
  i++;
}
