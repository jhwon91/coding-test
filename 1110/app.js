const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

input = input[0];
if ( input < 10 ){ input = '0'+ input}
solution(input);

function solution(input) {
	let result = input;
	let count = 0;

	do {
		count++;
		let sum = Math.floor(result/10)+ (result%10);
		result = ((result%10)*10) + (sum%10);
	} while (input != result);
	
	console.log(count);
}