def solution(clothes):
    answer = 1
    dd = {}
    for i in clothes:
        if i[1] in dd:
            dd[i[1]] += 1
        else:
            dd[i[1]] = 1
        
    for i in dd.keys():
        answer *= (dd[i] + 1)
    return answer -1
