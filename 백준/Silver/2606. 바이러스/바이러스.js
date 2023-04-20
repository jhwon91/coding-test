

const fs = require('fs');
const { validateHeaderName } = require('http');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs
						.readFileSync(filePath)
						.toString()
						.split('\n');

const N = +input.shift();
const M = +input.shift();

let graph = Array.from({length: N + 1},() => [])
let chk = Array.from({length: N + 1 },() => false);
let result = 0;

chk[1]=true;

for(let i = 0 ; i < M ; i++){
	let [from, to] = input.shift().split(' ').map((v) => +v);

	graph[from].push(to);
	graph[to].push(from);
}

const BFS = (V) => {
	let queue = graph[V];

	while(queue.length){
		let x = queue.shift();
		if(chk[x] === true) continue;
		chk[x] = true;
		result++;
		for(let i = 0; i < graph[x].length; i++){
			let next = graph[x][i];
			if(chk[next]===false)(
				queue.push(next)
			)
		}
	}
}


BFS(1)
console.log(result);
