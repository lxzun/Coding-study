def solution(participant, completion):
    name2count = {k: 0 for k in set(participant)}
    for i in participant:
        name2count[i] += 1

    for i in completion:
        name2count[i] -= 1
        if name2count[i] == 0: del name2count[i]

    answer = list(name2count.keys())[0]
    return answer


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, n in enumerate(completion):
        if participant[i] != n:
            return participant[i]
    return participant[-1]