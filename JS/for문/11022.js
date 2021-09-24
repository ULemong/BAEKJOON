const fs = require('fs');
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let answer = '';

for (let i=1; i<=input[0]; i++) {
  const num = input[i].split(' ').map(Number);
  answer += (`Case #${i}: ${num[0]} + ${num[1]} = ${num[0]+num[1]}`+ '\n');
}
console.log(answer);
