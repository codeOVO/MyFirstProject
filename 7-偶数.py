
evenlist=[]
def even_print(begin,end):
    for n in range(begin,end+1):
        if n%2==0:
            evenlist.append(n)
    print(evenlist)


begin=int(input('区间的起点:'))
end=int(input('区间的末尾:'))

even_print(begin,end)