const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const inputC = +input[0];
const inputTestCase = input[1].split(' ').map((item) => +item);

solution(inputC,inputTestCase);

function solution(inputC,inputTestCase) {
	let  min = inputTestCase[0], max = inputTestCase[0]; 
	for(let i = 0 ; i <= inputC-1 ; i++) {
		
		if ( inputTestCase[i] < min ) { 
			min = inputTestCase[i]
		};

		if ( inputTestCase[i] > max ) { 
			max = inputTestCase[i]
		};

	}
	console.log(`${min} ${max}`);
}