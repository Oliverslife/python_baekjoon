# is_on = True
# while is_on:
#     n = int(input())
#     if n == 0:
#         is_on = False
#     else:
#         arr = []
#         for i in range(n + 1, (n * 2) + 1):
#             err = 0
#             if i > 1:
#                 for j in range(2, i): # 2부터 i-1까지
#                     if i % j == 0:
#                         err += 1
#                         break # 2부터 i-1까지 나눈 몫이 0이면 err가 증가하고 break
#                 if err == 0:
#                     arr.append(i) # err가 없으면 소수를 리스트에 추가
#         print(len(arr)) 시간초과 뭐냐고!

########################################################
# 이건 왜안됨?

def solve():
    is_on = True
    while is_on:
        x = int(input())
        if x == 0:
            is_on = False
            pass
        elif x == 1:
            print("1")
        else:
            m = x + 1
            n = m * 2
            primes = [True] * (n + 1)
            primes[0] = False
            cnt = 0
            for i in range(2, n+1):
                if primes[i]:
                    for j in range(i*2, n+1, i): # 합성수 찾기 (배수)
                        primes[j] = False
            for i in range(m, n+1):
                if primes[i]:
                    # print(i)
                    cnt += 1
            print(cnt)
solve()
# 풀이중