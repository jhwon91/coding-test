function solution(number) {
    let answer = 0;
    
    for (let first  = 0 ; first < number.length ; first++) {
        for (let second  = first + 1 ; second < number.length ; second++) {
            for (let third  = second + 1 ; third < number.length ; third++) {
                if (number[first] + number[second] + number[third] === 0) {
                    answer++;
                }
            }
        }
    }
    return answer;
}