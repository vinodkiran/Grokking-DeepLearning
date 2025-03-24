
weights = [0.3, 0.2, 0.9]

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

def ele_mul(number, vector):
    output = [0,0,0]
    assert len(output) == len(vector)
    for i in range(len(vector)):
        output[i] = number * vector[i]

    return output

def neural_network(input, weights):
    prediction = ele_mul(input, weights)
    return prediction

input = wlrec[0]
pred = neural_network(input, weights)
print(pred)