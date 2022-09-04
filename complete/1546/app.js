const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const inputC = +input[0];
const testCase = input[1].split(' ').map((item) => +item);

solution(inputC,testCase);

function solution(inputC, testCase) {
	let max = testCase[0];
	for(let i = 0 ; i < inputC ; i++){
		if(max < testCase[i]){ max = testCase[i];}
	}
	
	const liarArr = testCase.map((item) => item/max*100);

	let sum = 0;
	for(let i = 0 ; i < liarArr.length; i++){
		sum += liarArr[i];
	}

	console.log((sum/liarArr.length).toFixed(2));
}