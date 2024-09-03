/**
 * 1 3 5 7 9 20 31 42 53 64
 * 
 * d(1) =  2
 * d(2) = 4
 * d(3) = 6
 * 4= 8
 * 5 = 10
 * 6 = 12
 * 7 = 14
 * 8 = 16
 * 9 = 18
 * 10 = 11
 * 12 = 15
 * 13 = 17
 * 14 = 19
 * 15 = 
 * 
 * 
 * 
 * 1. che array 만듦
 * 1 ~ N 까지 함수에 넣으면서 결과과 값 만환
 * chk array에 true로 체크
 */

const sequence = (value) => {
	
	let chk = Array.from({length: value +1},() => false);

	for(let i = 1; i <= value ; i++){
		chk[funD(i)] = true;
	};

	for(let i = 1 ; i <= value; i++){
		if(!chk[i]){console.log(i)};
	}
}

const funD = (x) => {
	let result = 0;
	let resultSub = [];

	if (String(x).length > 1){
		resultSub = String(x).split('').map((v) => +v)
		for(let i = 0; i < resultSub.length; i++){
			result += resultSub[i]
		}
		result += x;
	} else {
		result = x + x;
	}

	return result; 
}

sequence(10000);