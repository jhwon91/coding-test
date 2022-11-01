const fs = require('fs')
const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const inputC = +input[0]

solution(inputC)

function solution(N) {
	let count = 0;
	for (let i = 0; i <= N; i++) {
		for (let j = 0; j <= 59; j++) {
			for (let k = 0; k <= 59; k++) {
				if ((String(i)+String(j)+String(k)).indexOf(3) !== -1) {count += 1}
			}
		}
	}
	console.log(count);
}