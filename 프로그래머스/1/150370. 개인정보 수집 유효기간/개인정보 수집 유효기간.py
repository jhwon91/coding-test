def solution(today, terms, privacies):
    answer = []
    terms_dict = {term.split()[0]: int(term.split()[1]) for term in terms}
    
    today_year, today_month, today_day = map(int, today.split('.'))
    today_total_days = today_year * 12 * 28 + today_month * 28 + today_day

    for idx, item in enumerate(privacies):  # enumerate를 사용하여 인덱스와 항목을 동시에 가져옴
        date_str, term_type = item.split()
        year, month, day = map(int, date_str.split('.'))
        
        # 수집 날짜를 일수로 변환
        collect_total_days = year * 12 * 28 + month * 28 + day
        
        # 유효기간을 더해서 만료 날짜 계산
        duration_months = terms_dict[term_type]
        expire_total_days = collect_total_days + duration_months * 28 - 1
        
        # 오늘 날짜와 비교
        if today_total_days > expire_total_days:
            answer.append(idx + 1)  # idx를 사용하여 번호를 추가
    
    return answer

