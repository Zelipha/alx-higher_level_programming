#!/usr/bin/node

exports.converter = function (base) {
  return num => parseInt(num).toString(base);
};
