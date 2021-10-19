const fs = require('fs');
const input = require('fs').readFileSync('/dev/stdin').toString().trim();

console.log(solution(input));

function solution(n) {
  const coin_list = [500, 100, 50, 10, 5, 1];
  
  let answer = 0;
  let coin = 1000 - n;
  
  for (let i of coin_list) {
    if (i > coin) continue;
  
    answer += parseInt(coin / i);
    coin %= i;
  }
  
  return answer;
}
