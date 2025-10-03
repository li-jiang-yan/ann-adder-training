# Starting weights
w1 = 0.3
w2 = -0.7
training_rate = 0.1

# Each row: input 1, input 2, target output
lookup_table = [
    [1, 2, 3],
    [1, 3, 4],
    [1, 1, 2],
    [3, 3, 6]
]

# Column header
print("E | S | i1 | i2 |   w1 |   w2 | Ot | Or |  err | Delta_w1 | Delta_w2")

for e in range(5):
    for s in range(4):
        i1 = lookup_table[s][0] # input 1
        i2 = lookup_table[s][1] # input 2
        Ot = lookup_table[s][2] # target output
        Or = i1 * w1 + i2 * w2
        err = Ot - Or
        Delta_w1 = training_rate * err * i1
        Delta_w2 = training_rate * err * i2
        print("{} | {} |  {} |  {} | {: .1f} | {: .1f} | {: .0f} | {: .0f} | {: .1f} | {: .5f} | {: .5f}".format(e, s, i1, i2, w1, w2, Ot, Or, err, Delta_w1, Delta_w2))
        w1 += Delta_w1
        w2 += Delta_w2

print("Final solution: w1 = {}, w2 = {}".format(w1, w2))
