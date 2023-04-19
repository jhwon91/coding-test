const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs
							.readFileSync(filePath)
							.toString()
							.split('\n')
							.map((item) => item.split(' ').map((value) => +value));

// 3, 3
const [N, M] = input.shift();
let [y, x, d] = input.shift();
let cnt = 0;

//0 : 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪾
const dy = [-1,0,1,0];
const dx = [0,1,0,-1];

while (1) {
	if (input[y][x] === 0) {
		input[y][x] = 2;
		cnt++;		
	}
	let sw = false;

	let changeD  = d ;
	for(let i = 1; i < 5; i++) {	
		changeD -= 1
		if (changeD === -1 ) { changeD = 3 };

		const ny = y + dy[changeD];
		const nx = x + dx[changeD];
		if (0 <= ny && ny < N && 0 <= nx && nx < M){
			if (input[ny][nx] === 0 ){
				d = changeD;
				y = ny;
				x = nx;
				sw = true;
				break;
			}
		}
	}
	
	//청소되지 않은 빈칸이 없는 경우
	if (sw === false) {
		const ny = y - dy[d];
		const nx = x - dx[d];
		if (0 <= ny && ny < N && 0 <= nx && nx < M){
				if (input[ny][nx] === 1) {
					break;
				} else {
					y = ny;
					x = nx;
				}
		} else {
			break;
		}
	}
}

console.log(cnt);