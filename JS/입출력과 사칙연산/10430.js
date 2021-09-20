const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);

const A = input[0], B = input[1], C = input[2];

console.log((A+B)%C);
console.log(((A%C) + (B%C))%C);
console.log((A*B)%C);
console.log(((A%C) * (B%C))%C);
