

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