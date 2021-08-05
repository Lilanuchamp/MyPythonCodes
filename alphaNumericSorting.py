def alpha_numeric_sort(input):
    res = []
    print(len(input))
    a = ""
    input += "z"
    for i in range(0,len(input)):
        print(res)
        if input[i].islower() or input[i].isupper():
            if a:
                res.append(a)
            res.append(input[i])
            a = ""
            continue
        elif input[i].isdigit():
            a += input[i]
            continue

    res = res[:-1]
    return sorted(res)

print(alpha_numeric_sort('A12a4'))
