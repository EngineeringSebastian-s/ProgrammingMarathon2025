ite = int(input())
output = []

for i in range(ite):
    dim = int(input())
    vec1 = input().split(" ").sort()
    vec2 = input().split(" ").sort()
    res = 0
    for j in range(dim):
        res += int(vec1[j]) * int(vec2[j])
    output.append(res)

for k in range(len(output)):
    print("Case#"+str(k+1)+": "+str(output[k]))