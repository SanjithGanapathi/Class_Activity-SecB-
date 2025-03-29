def find_cube_pairs(targ): # included a colon which wasn't present and changed target to targ
    solutions = [] # removed the semicolon
    max_num = round(targ ** (1/3))  # changed *** to ** 

    for a in range(1, max_num + 1): #included colon and changed ranges to range
        for b in range(a, max_num + 1): #included colon and changed ranges to range
            if a**3 + b**3 == targ: # changed *** to ** and included colon
                solutions.append((a, b)) # removed semi colon and changed sol to solutions as initialised above
    return solutions # changed sol to solutions as initialised above

pairs = find_cube_pairs(1729)
print("Valid cube pairs for 1728:") # changed printf to print and removed comma
for a, b in pairs: # changed pair to pairs as declared above and included a colon
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1728") # changed printf to print and changed **2 to **3 as above
