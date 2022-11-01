const fs = require('fs')
const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const inputC = input[0].split('');
const column = +(inputC[0].charCodeAt(0) - 'a'.charCodeAt(0) + 1);
const row = +inputC[1];

//column , row
const steps =[
	[-2, -1],
	[-1, -2],
	[2, -1],
	[-1, 2],
	[1, -2],
	[-2, 1],
	[2, 1],
	[1, 2]
]

solution(column, row , steps)

function solution(column, row , steps) {
	let count = 0;
	steps.forEach((move) => {
		let moveColumn = column + parseInt(move[0])
		let moveRow = row + parseInt(move[1])
		
		if ( 0 < moveColumn && moveColumn <=8 && 0 < moveRow && moveRow <=8 ) {
			count += 1;
		}
	});

	console.log(count);
}