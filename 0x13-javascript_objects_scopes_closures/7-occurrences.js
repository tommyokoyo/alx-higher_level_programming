#!/usr/bin/node

/**
 * nbOccurences - Counts the number of occurences in a list
 * @list: Array of data
 * @searchElement: Element being counted
 *
 * Return: number of occurences
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let n = 0; n < list.length; n++) {
    if (list[1] === searchElement) {
      ++count;
    }
  }
  return count;
};
