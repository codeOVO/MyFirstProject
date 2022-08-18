number=int(input('几的阶乘？'))
result=1
while True:
    result=number*result
    number=number-1
    if number==1:
        print("阶乘是{}".format(result))
        break