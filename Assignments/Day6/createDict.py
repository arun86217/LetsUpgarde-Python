list1 = [1,2,3,4,5,7,8]
list2 = ["a","b","c","d","e"]
p={}
a=[ p.update((list1[i],list2[i])) for i in range(len(list2))]
print(a)
