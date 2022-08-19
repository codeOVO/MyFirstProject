import math #引入自带的pi，提高精度
def computer_are(n):
    area=math.pi*n*n
    print('半径为{}的圆的面积是{}'.format(n,area))
    pass


n=int(input('你要算的圆的半径:'))
computer_are(n)