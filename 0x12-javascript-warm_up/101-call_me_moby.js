#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  x = parseInt(x);
  if (x < 0) { return; }

  if (!isNaN(x)) {
    while (x--) {
      theFunction();
    }
  }
};
