/**
 * 1. 아이디어
 *  - 2중 For => 값 1 && 방문 x => DFS
 * 	- DFS를 통해 찾은 값을 저장 후 정렬 해서 출력
 * 
 * 2. 시간 복잡도
 *  - DFS : O(V+E)
 *  - V : N^2
 *  - E : 4N^2
 *  - V + E : 5N^2 ~= N^2 ~= 625 >> 가능
 * 
 * 3. 자료구조
 *  - 그래프 전체 지도 : int[][]
 *  - 방문 : bool[][]
 *  - 결과값 : int[]
 * 
 */

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs
							.readFileSync(filePath)
							.toString()
							.split('\n');

const n = input.shift();	
input = input.map((item) => item.split('').map((value) => +value));;

let result = [];	
let each = 0;	

console.log(n)
console.log(input)

let chk = Array.from({length: n},() => 
	Array.from({length:n},() => false)
);

const dy = [0, 1, 0, -1];
const dx = [1, 0, -1, 0];

const DFS = (i,j) => {
	each++;
	for(let k = 0 ; k < 4 ; k++) {
		const ny = i + dy[k];
		const nx = j + dx[k];

		if (0 <= ny && ny < n && 0 <= nx && nx < n) {
			if (input[ny][nx] === 1 && !chk[ny][nx]) {
				chk[ny][nx] = true;
				DFS(ny,nx)
			}
		}
	}
};

for (let i = 0 ; i < n ; i++) {
	for (let j = 0; j < n ; j++) {
		if (input[i][j] === 1 && !chk[i][j]) {
			chk[i][j] =  true; 
			each = 0;
			DFS(i,j);
			result.push(each);
		}
	}
};

result.sort((a,b) => a-b);
const answer = [result.length, ...result];
console.log(answer.join('\n'));


