const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');


const inputTestCase = [];

for (let i = 0; i <= input.length-1; ++i){
  inputTestCase.push(input[i].split(' ').map((item) => +item));
}

solution(inputTestCase);

function solution(testCase) {
	for(i=0 ; i <= testCase.length - 1; i++){
		if(testCase[i][0] === 0 &&  testCase[i][0] === 0) { break;}
		console.log(testCase[i][0] + testCase[i][1]);
	}
}