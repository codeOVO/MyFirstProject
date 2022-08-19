#素数是指它只有两个因子，也就是1和它本身
primes=[]
#创建一个空列表，接收素数
def is_primes(number):
    if number==1:
        return False
    else:
        for divisor in range(2,number):
            if number%divisor==0:
                return False
    return True


#养成这种自下而上去编写函数的习惯
#根据要求，进行函数的编写
def print_primes(begin,end):
    for number in range(begin,end+1):  #range是左闭右开的，所以要加一
        if is_primes(number):
            primes.append(number)
            pass
    print(primes)

begin=int(input('区间的起点:'))
end=int(input('区间的末尾:'))

print_primes(begin,end)

