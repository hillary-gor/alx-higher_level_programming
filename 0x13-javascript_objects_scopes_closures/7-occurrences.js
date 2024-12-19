#!/usr/bin/node
// Returns the number of occurrences of an element in a list

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  list.forEach(count);
  function count (item) {
    if (item === searchElement) {
      n++;
    }
  }
  return n;
};
