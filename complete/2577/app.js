const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const inputC = input.map((item) => +item);

solution(inputC);

function solution(input) {
	let Multiplication = 1;
	for(let i = 0 ; i < 3 ; i++) {
		Multiplication *= input[i];
	}
	Multiplication = String(Multiplication)

	for(let i = 0 ; i < 10 ; i++) {
		console.log(Multiplication.split(i).length-1)
	}
}
