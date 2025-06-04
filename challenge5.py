ite = int(input())
data = []

wave_y = []
wave_m = []


for i in range(ite):
   data.append(input().split())

init_y, init_m = input().split()
input()

wave_y.append([init_y, "0"])
wave_m.append([init_m, "0"])

for dt in data:
    if dt[0] == "Y":
        if dt[1] == "U":
            if dt[2] == init_y:
                wave_y.append([dt[3], dt[4]])
        elif dt[1] == "B":
            if dt[2] == init_y:
                wave_y.append([dt[3], dt[4]])
            elif dt[3] == init_y:
                wave_y.append([dt[2], dt[4]])
    elif dt[0] == "M":
        if dt[1] == "U":
            if dt[2] == init_m:
                wave_m.append([dt[3], dt[4]])
        elif dt[1] == "B":
            if dt[2] == init_m:
                wave_m.append([dt[3], dt[4]])
            elif dt[3] == init_m:
                wave_m.append([dt[2], dt[4]])

wave_unique = []

for i in range(len(wave_y)):
    for j in range(len(wave_m)):
        if wave_y[i][0] == wave_m[j][0]:
            wave_unique.append([wave_y[i][0], int(wave_y[i][1])+int(wave_m[i][1])])

min_cost = ["",500]

for w in wave_unique:
    if min_cost[1] > w[1]:
        min_cost[1] = w[1]
        min_cost[0] = w[0]

print(min_cost[1], min_cost[0])
