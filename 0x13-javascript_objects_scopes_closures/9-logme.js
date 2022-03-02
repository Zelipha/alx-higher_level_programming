#!/usr/bin/node

// Prints the number of arguments already printed
// and the new argument value
const stack = [];
exports.logMe = function (item) {
  stack.push(item);
  console.log(stack.indexOf(item) + ': ' + item);
};
