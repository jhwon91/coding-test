def solution(players, callings):

    player_dict = {player: idx for idx, player in enumerate(players)}
    for n in callings:
        idx = player_dict[n]
        
        players[idx - 1] ,players[idx] = players[idx] ,players[idx - 1]
        
        player_dict[players[idx]] = idx
        player_dict[players[idx - 1]] = idx - 1
        
    return players