rdata = []
with open("data/day3.txt") as f:
    for line in f:
        rdata.append(list(map(int, line.strip())))

gamma_bin = ''
epsilon_bin = ''
ddata = [rdata[::], rdata[::]]

for i, column in enumerate(list(zip(*rdata))):
    k = int(sum(column) > (len(rdata) // 2)
    gamma_bin += str(k)
    epsilon_bin += str(abs(k -1))

    for j, dset in enumerate(ddata):
        cols = list(zip(*dset))
        n = len(cols[i])
        n1 = sum(cols[i])
        n0 = n - n1
        b = n0 > n1 if j else n1 >= n0
       
        if len(ddata[j]) != 1:
            ddata[j] = list(filter(lambda o: o[i] == b, ddata[j]))
        


print("Q1", int(gamma_bin, base=2) * int(epsilon_bin, base=2))
print("Q2", int(''.join(map(str, ddata[0][0])), base=2) 
            * int(''.join(map(str, ddata[1][0])), base=2))


