def angryProfessor(k, a):
    count = 0
    for i in a:
        if i < 1:
            count += 1
    return 'YES' if count < k else 'NO'

    # present = len([x for x in a if x < 1])
    # if present >= k:
    #     return 'NO'
    # else:
    #     return 'YES'


list = [-93, -86, 49, -62, -90, -63, 40, 72, 11, 67]
present = [x + 1 for x in list if x > 0]
print(present)
# if present >= k:
#     print('YES')
# else:
#     print('NO')
