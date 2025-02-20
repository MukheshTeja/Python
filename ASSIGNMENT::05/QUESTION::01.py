def maxxor(num, check):
    max_xor = 0 
    for i in range(num, check + 1): 
        for j in range(i, check + 1):
            xor_value = i ^ j
            if xor_value > max_xor: 
                max_xor = xor_value 
            print(i, "xor", j, "=", xor_value) 
    print("Max XOR value:", max_xor)

maxxor(10, 15)
