my_set = {1, 2, 3}
print(my_set)
#set nuk mundesh me shkru shuma duplikate pasi nuk e pranon e fshin vet psh:
set = set([4, 5, 6, 6])
print(set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#Union bashkon te dy setet
union_result_method = set.union(set1, set2)
union_result_operator = set1 | set2
print('Union of set1 and set2 using union method:',union_result_method) #12345
print('Union of set1 and set2 using union operator:',union_result_operator)#12345

#intersection printon te perbashketat e dy seteve
intersection_method = set1.intersection(set2)
intersection_operator = set1 & set2
print('Intersection of set1 and set2 using intersection method:',intersection_method)#3
print('Intersection of set1 and set2 using intersection operator:',intersection_operator)#3

#Difference printon vetem te dhenat e setit te caktuar ato qe nuk jan te perbashkta
difference_method = set1.difference(set2)
difference_operator = set1 - set2
print('Difference of set1 and set2 using difference method:',difference_method)#1,2
print('Difference of set1 and set2 using difference operator:',difference_operator)#1,2

#Symetric_difference printon te dhenat e te dy seteve per veq atyre te perbashktave
symmetric_method = set1.symmetric_difference(set2)
symmetric_operator = set1 ^ set2
print('Symmetric difference of set1 and set2 using symmetric method:',symmetric_method)#1,2,4,5
print('Symmetric difference of set1 and set2 using symmetric operator:',symmetric_operator)#1,2,4,5

#te seti munesh me shtu,me largu te dhana per dallim prej tuples psh:
my_set = {1, 2, 3}

my_set.add(4)
print(my_set)

my_set.remove(2)
print(my_set)

#Printon edhe nese aj numer ne set nuk egziston
my_set.discard(7)
print(my_set)

