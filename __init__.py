if __name__== '__main__':
    x = [866, 783, 1046, 931, 907, 684, 764, 656, 702, 856, 1133, 1132]
    total = 0
    for i in x:
        total += i
    print(total)
    sum = 0
    for i in x:
        if i > 900:
            sum += i

    print(sum)

    print(sum/total)

