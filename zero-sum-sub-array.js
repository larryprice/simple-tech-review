var subarrays = function(arr) {
  for (var i = 0; i < arr.length-1; ++i) {
    var sum = arr[i], sub = [arr[i]];
    if (sum === 0) {
      console.log(sub);
    }
    for (var j = i+1; j < arr.length; ++j) {
      sum += arr[j];
      sub.push(arr[j])
      if (sum === 0) {
        console.log(sub);
      }
    }
  }
};

console.log("Results for [4, 2, -3, -1, 0, 4]");
subarrays([4, 2, -3, -1, 0, 4])
console.log("Results for [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]");
subarrays([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])
