const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);

const h = input[0] , m = input[1];

if (m >= 45) {
  console.log(h, m - 45);
}
else {
  if (h === 0) {
    console.log(23, m + 60 - 45);
  }
  else {
    console.log(h - 1, m + 60 - 45);
  }
}
