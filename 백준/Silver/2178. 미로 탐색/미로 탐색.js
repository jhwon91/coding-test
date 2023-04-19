/**
 * 1. 아이디어
 *  - 최단거리 문제는 BFS로 풀기
 *    
 * 
 * 2. 시간 복잡도
 *  - BFS :  N, M <= 100이므로, 최악의 상황에서 N과 M이 같다. 따라서 O(N^2)
 *  - 100 * 100 > 가능
 * 
 * 3. 자료구조
 *  - 그래프 : int[][]
 *  - 방문 : bool[]
 *  - 결과값 : int[]
 * 
 */

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs
						.readFileSync(filePath)
						.toString()
						.split('\n');

const [N, M] = input.shift().split(" ").map((v) => +v);	
input = input.map((item) => item.split('').map((value) => +value));;

let result = 0;

let chk = Array.from({length: N  },() => 
	Array.from({length: M },() => 0)
);

const dy = [1, 0, -1, 0];
const dx = [0, 1, 0, -1];

const BFS = (i,j) =>{
	let queue = [[i,j]]
	result++;
	chk[i][j] = 1;

	while(queue.length){
		const [y, x] = queue.shift();
		let sw = true;
		for(let k =0; k < 4 ; k++){
			const ny = y + dy[k];
			const nx = x + dx[k];

			if (0 <= ny && ny < N && 0 <= nx && nx < M) {
				if (input[ny][nx] === 1 && !chk[ny][nx]) {
					chk[ny][nx] = chk[y][x]+1;
					queue.push([ny,nx])
					
				} 
			}
		}
	}
}

BFS(0,0)
console.log(chk[N-1][M-1])


