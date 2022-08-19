




def sum_print(number):
    result=0
    for n in range(1,number+1):
        result=result+n*n
        pass
    print(result)


number=int(input('你要求前几的平方和？'))
sum_print(number)