function solution(cipher, code) {
    const BaseArray = [...cipher]
    let count = code;
    let answer = '';
    
    for (let i = 0 ; i < BaseArray.length ; i++){
        if (i + 1 === count) {
            answer +=  BaseArray[i];
            count += code
        }
    }
    
    return answer;
}