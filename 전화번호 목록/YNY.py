import ast
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        phone_len = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:phone_len]:
            answer = False
            break
        else:
            continue
    return answer
