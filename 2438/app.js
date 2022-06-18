const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

input = input[0];
solution(input);


function solution(input) {
    for (let i = 1 ; i <= input; i++){
			let star = '';
			for (let j = 1 ; j <= i ; j++){
				star += '*';
			}
			console.log(`${star}`);
    }
}