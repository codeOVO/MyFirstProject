#本次采用直接按照值来删除列表里面的元素
# list1=[3,5,7,9,11,13]
# list1.remove(7)
# list1.remove(11)
# print(list1)

#如果要移除的元素用列表表示
def remove_elements_fromlist(list1,list2):
    for item in list2:
        list1.remove(item)
    return list1


list1=[3,5,7,9,11,13]
list2=[7,11]
print(remove_elements_fromlist(list1,list2))