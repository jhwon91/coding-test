/**
 * 1. 아이디어
 *  - 배열의 n번째 인데스 요소가 n번 정점과  연결된 장점들로 이루어진 배열이
 *    되도록 그래프 배열 생성
 *    
 * 
 * 2. 시간 복잡도
 *  - DFS, BFS :  O(V+E)
 *  - 1,000 + 10,000 > 가능
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

const [N, M, V] = input.shift().split(" ").map((v) => +v);	
let result = [];
let chk = [];
let graph = Array.from({length: N +1 },() => []);

const initArray = () => {
	chk = Array.from({length: N +1 },() => false);
	result = [];
}

//간 노드 인접 행렬
for (let i = 0; i < M ; i++) {
	let [from, to] = input.shift().split(" ").map((v) => +v);	
	graph[from].push(to);
	graph[to].push(from);
}

graph.forEach((datas) => {
	datas.sort((a,b) => a - b);
})

const DFS = (V) => {
	if (chk[V] === true) return;
	chk[V] = true;
	result.push(V);
	for(let i = 0 ; i < graph[V].length; i++){
		let next = graph[V][i];
		if(chk[next] === false) {
			DFS(next)
		}
	}	
}

const BFS = (V) =>{
	let queue = [V];

	while (queue.length)	{
		let x = queue.shift();
		if (chk[x] === true) continue;
		chk[x] = true;
		result.push(x);
		for(let i = 0; i < graph[x].length ; i++) {
			let next = graph[x][i];
			if (chk[next] === false) {
				queue.push(next);
			}
		}
	}
}

initArray();
DFS(V);
console.log(result.join(' '));
initArray();
BFS(V);
console.log(result.join(' '))



