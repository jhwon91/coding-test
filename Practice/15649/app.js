/**
 * 1. 아이디어
 *  - 백트랙킹 재귀함수 안에사, for  돌면서 숫자 선택 (방문 여부 확인)
 * 	- 재귀함수에서  M개를 선택할 경우 print
 * 
 * 2. 시간 복잡도
 *  백트랙킹
 *  - N^N : 중복이 가능, N =8 까지 가능
 *  - N! : 중복이 불가, N =10 까지 가능
 * 
 * 3. 자료구조
 *  - 결과값 저장 int[]
 *  - 방문여부 체크 bool[]
 * 
 */

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs
							.readFileSync(filePath)
							.toString()
							.split('\n')
							.map((item) => item.split(' ').map((value) => +value));


const [N, M] = input.shift();
// 4, 2
let result = [];
let chk = Array.from({length: N+1},() => false);

const recur = (num) => {
	if (num === M) {
		console.log(result.join(' '))
		return;
	}

	for(let i = 1 ; i < N+1 ; i++) {
		if (chk[i] === false) {
			chk[i] = true;
			result.push(i);
			recur(num+1);
			chk[i] = false;
			result.pop();
		}
	}
}

recur(0);
