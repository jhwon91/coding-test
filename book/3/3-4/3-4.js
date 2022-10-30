const fs = require('fs')
const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const inputC = input[0].split(' ').map((item) => +item);

solution(inputC[0], inputC[1])

function solution(N, K) {
	let count = 0 ;
	let target = 0;
	
	// while (true) {
	// 	target = parseInt((N / K)) * K
	// 	count += (N - target)
	// 	N = target;
	// 	if (N < K){ break ;}

	// 	count += 1;
	// 	N /= K;
		
	// }
	// count += (N - 1);
	
	while (true) {
		if (N % K === 0) {
			N /= K;
			count ++;
		} else {
			N -= 1;
			count ++;
		}

		if (N === 1) break;
	}
	console.log('count',count);
	
}