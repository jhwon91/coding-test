n = int(input())

# 5로 나눈 나머지가 짝수인 경우만 가능
if n % 5 % 2 == 0:
    # 5로 나눈 몫
    five = n // 5
    # 5로 나눈 나머지를 2로 나눈 몫
    two = (n % 5) // 2
    # 5원 동전 개수와 2원 동전 개수의 합
    print(five + two)
else:
    # 5로 나눈 몫에서 1을 빼고
    five = n // 5 - 1
    if five < 0:
        print(-1)
    else:
        # 남은 금액을 2로 나눈 몫
        two = (n - five * 5) // 2
        print(five + two)