import math
def change_base(n, q):   # 진법을 바꾸는 함수
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def is_prime(n):
  n = int(n)
  if n == 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def solution(n, k):
    answer = 0
    changed_num = change_base(n,k)
    nums = changed_num.split('0')
    
    for i in nums:
        if len(i) != 0:
            if is_prime(i)==True:
                answer +=1
            else: pass

    return answer
