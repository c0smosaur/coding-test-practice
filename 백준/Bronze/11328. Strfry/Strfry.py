num = int(input())

for i in range(num):
    str1, str2 = map(str, input().split())
    d1 = {}
    d2 = {}
    
    for i in str1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in str2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1

    characters = set(d1.keys()).union(set(d2.keys()))
    
    possible = True

    for character in characters:
        c1 = d1.get(character, 0)
        c2 = d2.get(character, 0)
        diff = abs(c1-c2)
        
        if diff != 0:
            possible = False
            break
    
    if possible:
        print("Possible")
    else:
        print("Impossible")