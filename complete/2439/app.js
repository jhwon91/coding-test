const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

input = input[0];
solution(input);


function solution(input) {
    for (let i = 1 ; i <= input; i++){
			let star = '';
			for (let j = 0 ; j <= input-1; j++ ){
				if (j >= input - i ){
					star += '*';
				}else {
					star += ' ';	
				}
			}
			console.log(`${star}`);
    }
}