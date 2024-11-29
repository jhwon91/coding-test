def solution(new_id):
    answer = ''
    
    #1
    new_id = new_id.lower()
    
    #2
    allow = ['-','_','.']
    afterWord = ''
    for char in new_id:
        if char.isalnum() or char in allow: 
            afterWord += char
    new_id = afterWord
    
    #3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    #4
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')
    
    #5
    if not new_id:
        new_id = "a"
    
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    return new_id