
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
def solution(phone_book):
    pb = {i:{j:{k:{y:[] for y in range(10)} for k in range(10)} for j in range(10)} for i in range(3, 21)}
    pb[1] = {i:[] for i in range(10)} 
    pb[2] = {i:{j:[] for j in range(10)} for i in range(10)} 
    for pn in phone_book:
        i = len(pn)
        if i == 1:
            pb[i][int(pn[0])].append(pn)
        elif i == 2:
            pb[i][int(pn[0])][int(pn[1])].append(pn)
        else:
            pb[i][int(pn[0])][int(pn[1])][int(pn[2])].append(pn)

    for x in range(1, 20):
        if x == 1:
            for i in range(10):
                for j in pb[x][i]:
                    for xx in range(10):
                        for y in pb[2][i][xx]:
                            if j == y[0]: return False

                    for k in range(3, 21):
                        for xx in range(10):
                            for xxx in range(10):
                                for y in pb[k][i][xx][xxx]:
                                        if j == y[0]: return False
        elif x == 2:
            for i in range(10):
                for j in range(10):
                    for k in pb[x][i][j]:
                        for xx in range(x+1, 21):
                            for xxx in range(10):
                                for y in pb[xx][i][j][xxx]:
                                    if k == y[:x]: return False
        else:
            for i in range(10):
                for j in range(10):
                    for jj in range(10):
                        for k in pb[x][i][j][jj]:
                            for xx in range(x+1, 21):
                                for y in pb[xx][i][j][jj]:
                                    if k == y[:x]: return False
    return True