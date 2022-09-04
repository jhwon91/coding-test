const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

// 변수 앞 + 단항연산자를 써주면  Number를 붙이는 것과 똑같은 효과
const N = +input[0];
const testCase = [];

for(let i = 1; i <= N; i++) {
    const arr = input[i].split(' ').map((item) => +item);
    testCase.push(arr);    
}

solution(testCase);

function solution(data) {
    for (let i = 0 ; i < N; i++) {
        console.log(`Case #${i+1}: ${data[i][0]} + ${data[i][1]} = ${data[i][0] + data[i][1]}`);
    }
}

