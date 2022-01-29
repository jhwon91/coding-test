const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const N = +input[0]
console.log(solution(N));

function solution(input) {
    let sum = 0;
    if (input > 0){
        sum = input + solution(input  - 1);
    }
    return sum;
}