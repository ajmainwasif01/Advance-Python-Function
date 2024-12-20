n1 = [4,5,6]

n2 = [7,8,9]

result = map(lambda x, y: x * x, n1,n2)

print(list(result))

num = [3,4,2,6,9,17]

def sq(n):
    return n*n
sq = list(map(sq , num))

print(sq)