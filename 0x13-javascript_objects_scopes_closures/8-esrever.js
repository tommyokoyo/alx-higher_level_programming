#!/usr/bin/node

/**
 * esrever - Reverses a list
 * @list: Array being reversed
 *
 * Return: Reversed array
 */
exports.esrever = function (list) {
  let temp;

  for (let m = 0, n = list.length - 1; m < n; ++m, --n) {
    temp = list[m];
    list[m] = list[n];
    list[n] = temp;
  }
  return list;
};
