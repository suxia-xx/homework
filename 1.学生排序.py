students=eval(input())
students.sort(key=lambda x:x[2],reverse=True)
for i in students:
    print(*i)








