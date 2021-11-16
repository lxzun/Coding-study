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


if __name__ == '__main__':
    n = input()
    m = ast.literal_eval(n)  # str to list
    ans = solution(m)
    print(ans)
