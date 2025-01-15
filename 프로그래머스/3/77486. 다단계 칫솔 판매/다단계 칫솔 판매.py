
def solution(enroll, referral, seller, amount):
    answer = []
    refMap = {} #본인 : 추천인
    result = {}
    
    def distribute(seller, price):
        if seller is None or price < 1:
            return
        share = price // 10
        result[seller] += price - share
        distribute(refMap.get(seller), share)
        
    
    for i in range(len(enroll)):
        name = enroll[i]  
        ref = referral[i]  
        if ref == "-":  # 추천인이 없는 경우
            refMap[name] = None
        else:  # 추천인이 있는 경우
            refMap[name] = ref
    
    for name in enroll:
        result[name] = 0
        
    for i in range(len(seller)):
        name = seller[i]
        price = amount[i] * 100
        distribute(name,price)
        
    for name in enroll:
        answer.append(result[name])
        
    return answer