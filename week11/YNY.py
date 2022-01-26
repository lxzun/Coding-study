from copy import deepcopy
def solution(new_id):
    # step1
    new_id = new_id.lower()

    # step2
    tmp = []
    for character in new_id:
        if 97 <= ord(character) <= 122 or ord(character) == 46 or ord(character) == 45 or ord(character) ==95 or 48<=ord(character)<=57:
            tmp.append(character)
        new_id = ''.join(tmp)

    # step 3
    tmp = []
    tmp.append(new_id[0])
    for i in range(1, len(new_id)):
        if new_id[i] != new_id[i - 1] or new_id[i]!='.':
            if new_id[i] != '.' or new_id[i-1] != '.':
                tmp.append(new_id[i])
            continue
    new_id = ''.join(tmp)

    # step 4
    new_id = new_id.strip('.')

    # step 5
    if len(new_id) == 0:
        new_id = 'a'

    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')

    # step 7
    if len(new_id)<=2:
        for i in range (3-len(new_id)):
            new_id+=new_id[-1]

    return new_id
