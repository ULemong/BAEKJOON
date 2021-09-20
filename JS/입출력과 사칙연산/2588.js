const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const A = Number(input[0]), B = input[1];

console.log(A * B[2]);
console.log(A * B[1]);
console.log(A * B[0]);
console.log(A * Number(B));
