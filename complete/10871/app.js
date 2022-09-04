let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const arr = [];

for (let i = 0; i <= 1; i++){
    arr.push(input[i].split(' ').map((item) => +item));
}

const newArr = [];
for (let i = 0; i <= arr[0][0]-1; i++){
		newArr.push(arr[1][i]);
}

const testCase = {
		N: arr[0][0],
		X: arr[0][1],
		arr: newArr,
};

solution(testCase);

function solution(testCase) {
	let compareNumber = ''
	
	for( i = 0 ; i <= testCase.N ; i ++) {
		if (testCase.X > testCase.arr[i]) {
			compareNumber += testCase.arr[i] + ' ';
		}
	}
	console.log(compareNumber);
};