def solution(phone_book):
    pb = {k:[] for k in range(1, 21)}
    for pn in phone_book:
        pb[len(pn)].append(pn)
        
    for i in range(1, 20):
        for j in pb[i]:
            for k in range(i+1, 21):
                for y in pb[k]:
                    if j == y[:i]:
                        return False
    
    return True