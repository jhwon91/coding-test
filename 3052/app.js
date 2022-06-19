const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

let testCase = [];
const inputC = input.map((item) => {	
	if( 0 <= Number(item) && Number(item) <= 100 ) {
		testCase.push(+item)
	}
});

solution(testCase);

function solution(input){
	
	const arr = input.map((item)=> item%42);
	let incluedsArr = [];
	arr.forEach((item) => {
		if(!incluedsArr.includes(item)){
			incluedsArr.push(item)
		}
	});
	
	console.log(incluedsArr.length);
}
