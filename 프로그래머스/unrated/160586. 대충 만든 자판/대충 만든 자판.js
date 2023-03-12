function solution(keymap, targets) {
    let answer = [];
    const keytable = keymap.reduce((obj, keys) => {
        [...keys].forEach((key, i) => {
            if (obj[key]) {
                obj[key] = Math.min(obj[key], i + 1)
            } else {
                obj[key] = i + 1
            }
        })
        return obj
      }, {})
    
    answer = targets.map((target) => {
        let clicked = 0
        for (const key of [...target]) {
            
            if (!keytable[key]) {
                clicked = -1
                break
            }
            clicked += keytable[key]
        }
        return clicked
    })
    return answer;
}