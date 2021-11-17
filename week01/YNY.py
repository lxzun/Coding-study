def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append('_')
    for i,j in zip(participant,completion):
        if i != j:
            answer = i
            break
    return answer
