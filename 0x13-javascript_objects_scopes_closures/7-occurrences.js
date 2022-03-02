#!/usr/bin/node

// Returns number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  list.forEach(item => item === searchElement && count++);
  return count;
};
