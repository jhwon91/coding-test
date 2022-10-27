const fs = require('fs')
const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const inputC = input[0].split(' ').map((item) => +item);
const inputTestCase = [];
for(i = 0; i<inputC[0]; i++){
	const arr = input[i+1].split(' ').map((item) => +item);
	inputTestCase.push(arr);
}

solution(inputC, inputTestCase);

function solution (inputC, inputTestCase) {
	let min = 0;
	let temp = 0;
	
	for(i = 0; i < inputC[0]; i++) {
		min = Math.min(...inputTestCase[i]);
		if (min > temp) { temp = min }
	}
	console.log(temp);
} 