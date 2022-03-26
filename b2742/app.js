const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const N = +input[0]
let result = '';

for (let i = N ; i > 0 ; i-- ){
    result += i + '\n';
}
console.log(result);