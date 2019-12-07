with open("inputdayone.txt", "r") as f:
    lines = f.readlines()

fuels = [ (int(i.strip()) // 3) - 2 for i in lines if i.strip().isdigit()]

total = sum(fuels)

compute_fuels = list(filter(lambda x:x > 0, fuels))

while any(compute_fuels):
    compute_fuels = [ (f // 3) - 2  for f in compute_fuels]
    compute_fuels = list(filter(lambda x:x > 0, compute_fuels))
    total += sum(compute_fuels)

print(total)
