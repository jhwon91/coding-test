/**
 * 1. 아이디어
 *  - 2중 For => 값 1 && 방문 x => BFS
 * 	- BFS 돌면서 그림 개수 +1, 최대값을 갱신
 * 
 * 2. 시간 복잡도
 *  - BFS : O(V+E)
 *  - V : 500 * 500
 *  - E : 4 * 500 * 500
 *  - V + E : 5 * 250000 = 100 만 < 2억 >> 가능
 * 
 * 3. 자료구조
 *  - 그래프 전체 지도 : int[][]
 *  - 방문 : bool[][]
 *  - Queue(BFS)
 * 
 */

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs
							.readFileSync(filePath)
							.toString()
							.split('\n')
							.map((item) => item.split(" ").map((value) => +value));;

let cnt = 0;
let maxValue = 0;	
const [n, m] = input.shift();

let chk = Array.from({length: n},() => 
	Array.from({length:m},() => false)
);

const dy = [0, 1, 0, -1];
const dx = [1, 0, -1, 0];

const BFS = ((i,j) => {
	let total = 1; //그림 넚이
	let Queue = [[i,j]];
	
	while(Queue.length) {
		const [y,x] = Queue.shift();

		for (let k = 0 ; k < 4; k++) {
			const ny = y + dy[k];
			const nx = x + dx[k];
			if (0 <= ny && ny < n && 0 <= nx && nx < m) {				
				if(input[ny][nx] === 1 && !chk[ny][nx]){
					total++;
					chk[ny][nx] = true
					Queue.push([ny,nx])
				}
			}
		}
	}
	return total;
});

for (let i = 0 ; i < n ; i++) {
	for (let j = 0; j < m ; j++) {
		if (input[i][j] === 1 && !chk[i][j]) {
			chk[i][j] =  true;
			// 전체 그림 갯수 +1
			cnt++; 
			// BFS > 그림크기 구해주고
			// 최대값 갱신
			maxValue = Math.max(maxValue,BFS(i,j))
		}
	}
}

console.log(cnt + `\n` + maxValue)


