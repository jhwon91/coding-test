const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const N = +input[0]
const testCase = [];

for (let i  = 1 ; i <= N ; i++){
    const arr = input[i].split(' ').map((item) => +item);
    testCase.push(arr);
}

solution(testCase);

function solution(input) {
    for (let i = 0 ; i < N ; i++){
        console.log(input[i][0] + input[i][1])
    }
}