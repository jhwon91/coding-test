const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const inputC = input.map((item) => +item);

solution(inputC);

function solution(input) {
	let index = 0;
	let max = input[0]; 
	for(let i = 0 ; i < 9 ; i++) {
		if ( input[i] > max ) { 
			max = input[i];
			index = i;
		};
	}
	console.log(max);
	console.log(index+1);
}
