num = int(input())

for i in range(num):
    str1, str2 = input().split()

    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    if str1 == str2:
        print("Possible")
    else:
        print("Impossible")