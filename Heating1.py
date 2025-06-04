iter = int(input())
output = []
for i in range(iter):
    num = input()
    output.append(num)

for j in range(len(output)):
    count = 0
    while output[j] != output[j][::-1] and count < 1000+1:
        output[j] = str(int(output[j]) + int(output[j][::-1]))
        count += 1

    if count > 1000:
        print("Not palindrome exist")
    else:
        print(count,output[j])