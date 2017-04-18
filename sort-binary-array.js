var sortBinary = function(a, reverse=false) {
  var fronts = 0;
  var front = reverse ? 1 : 0;
  var rear = reverse ? 0 : 1;
  for (var i = 0; i < a.length; ++i) {
    if (a[i] === front) {
      a[i] = rear;
      a[fronts++] = front;
    }
  }
  return a;
}

console.log(sortBinary([1, 0, 1, 0, 1, 0, 0, 1]));
console.log(sortBinary([1, 0, 1, 0, 1, 0, 0, 1], true));
