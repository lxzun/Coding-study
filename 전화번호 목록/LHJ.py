def solution(phone_book):
    pb = {k: {j: [] for j in range(1, 21)} for k in range(0, 10)}
    for pn in phone_book:
        pb[int(pn[0])][len(pn)].append(pn)

    for x in range(0, 10):
        for i in range(1, 20):
            for j in pb[x][i]:
                for k in range(i + 1, 21):
                    for y in pb[x][k]:
                        if j == y[:i]:
                            return False

    return True