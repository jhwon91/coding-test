def solution(park, routes):
    answer = []
    x,y = 0,0
    for row in range(len(park)):
        for col in range(len(park[y])):
            if park[row][col] == "S":
                x, y = row, col

    direction = {     
        'N': [-1, 0],
        'S': [1, 0],
        'W': [0, -1],
        'E': [0, 1]
    }
    
    for move in routes:
        move_route = move.split(' ')[0]
        move_count = int(move.split(' ')[1])
        move_x, move_y = x, y
        
        for n in range(move_count):
            ob_bool = False
            #이동
            move_x += int(direction[move_route][0])
            move_y += int(direction[move_route][1])
						
            #공원에서 벗어나는지 확인
            if move_x < 0 or move_x > len(park)-1 or move_y > len(park[0])-1 or move_y < 0 :
                break
            if park[move_x][move_y] == 'X':
                break
            ob_bool = True
        if ob_bool == True:
            x = move_x
            y = move_y
        
        # print(f'x: {x}, y: {y}')
    answer.append(x)
    answer.append(y)
    return answer
