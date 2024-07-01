
from collections import deque

def solution(cards1, cards2, goal):
    answer = []
    
    card1 = deque(cards1)
    card2 = deque(cards2)
    
    for word in goal:
        if card1 and word == card1[0]: 
            answer.append(card1.popleft()) 
        if card2 and word == card2[0]: 
            answer.append(card2.popleft())
    
    return "Yes" if answer == goal else "No"