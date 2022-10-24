const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

const inputC = input[0].split(' ').map((item) => +item);;
const arr = input[1].split(' ').map((item) => +item);

const inputTestCase = [];

for(let i = 0 ; i< inputC[0] ; ++i){
	inputTestCase.push(arr[i])
}

//정렬
inputTestCase.sort((a,b) => {
	return b-a;
})

solution(inputC, inputTestCase);

function solution(inputC, inputTestCase) {
	const first = inputTestCase[0];  //가장큰수
	const second = inputTestCase[1];   //두번째로 큰수
	
	const M = inputC[1] //숫자더해지는 횟수
	const K = inputC[2] //연속해서 더해지는 제한 횟수

	let count = parseInt( M / ( K + 1 ) ) * K //가장 큰수가 더해시지는 횟수
	count += ( M % ( K + 1 )) //M이 K+1 로 나누어 떨어지지 않는 경우

	const firstSum = count * first;
	const secondSum = (M - count) * second;

	console.log(firstSum + secondSum);

}