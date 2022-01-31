const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const N = +input[0]
let result = '';

for (let i  = 1 ; i <= N ; i++){
    const arr = input[i].split(' ').map((item) => +item);
    result += arr[0] + arr[1] + '\n';
}
console.log(result);