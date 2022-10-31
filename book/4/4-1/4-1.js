const fs = require('fs')
const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const inputC = input[1].split(' ');

solution(input[0], inputC)

function solution(N, move) {
	
  let x = 1;
	let y = 1;

	move.forEach((item) => {
		switch (item) {
			case 'L':
				if (x - 1 > 0) { x -= 1; }
				break;
			case 'R':
				if (x + 1 <= N) { x += 1; }
				break;
			case 'U':
				if (y - 1 > 0) { y -= 1; }
				break;
			case 'D':
				if (y + 1 <= N) { y += 1; }
				break;
		}
		
	});

	console.log(`${y} ${x}`)

}