const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stbin' : './input.txt/'
const input = fs.readFileSync(filePath).toString().split('\n');


for (let i = 0 ; i < input.length; i++){
    const arr = input[i].split(' ').map((item) => +item);
    solution(arr[0], arr[1]);
}

function solution(A,B) {
    console.log(A+B);
    console.log(A-B);
    console.log(A*B);
    console.log(Math.floor(A/B));
    console.log(A%B);
}