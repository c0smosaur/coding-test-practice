def solution(phone_book):

    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        curr = phone_book[i]
        if phone_book[i+1].startswith(curr):
            return False
    
    return True