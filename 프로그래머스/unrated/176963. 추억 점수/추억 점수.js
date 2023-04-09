function solution(name, yearning, photo) {
    let answer = [];
    let arr = [];
    
    for (i = 0 ; i < name.length ; i++) {
        let obj =  {
            name : name[i],
            cost : yearning[i]
        }
        arr.push(obj)
    }
    
    let sum = 0;
    photo.forEach((row) => {
        sum = 0;
        row.forEach((rowData) => {
            arr.forEach((data) => {
                if (data.name === rowData) {
                    sum += data.cost
                }
            })
        })
        answer.push(sum)
    })
    return answer;
}