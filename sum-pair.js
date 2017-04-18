var arr = [8, 7, 2, 5, 3, 1]
var sum = 10

// for (var i = 0; i < arr.length-1; ++i) {
//   for (var j = 1; j < arr.length; ++j) {
//     if ((arr[i] + arr[j]) === sum) {
//       console.log(arr[i], arr[j]);
//       return 0;
//     }
//   }
// }

arr = arr.sort(function (a, b) {
  return a - b;
});

var low = 0, high = arr.length-1, calc;
while (low < high) {
  calc = arr[low] + arr[high];
  if (calc === sum) {
    console.log(arr[low], arr[high]);
    return 0;
  }
  if (calc < sum) {
    ++low;
  } else {
    --high;
  }
}

return 1;
