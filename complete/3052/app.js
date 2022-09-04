const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

let incluedsArr = [];
input.forEach((item) => {

	const index = item % 42;

	if(incluedsArr.indexOf(index) === -1){
		incluedsArr.push(index)
	}
});
console.log(incluedsArr.length);
