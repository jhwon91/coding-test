const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

input = input[0];
solution(input);

function solution(input) {
  let coin  = 1000- input;
	let count = 0;

	const coinType = [500,100,50,10,5,1]

	coinType.forEach((value) => {
		count += Math.floor(coin/value);
		coin %= value
	});
	console.log(count);
}