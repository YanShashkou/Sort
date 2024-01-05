def merge (list1,list2):
    list_result = list1
    for num in list2:
        list_result.append(num)
    for i in range(len(list_result)-1):
        print(f"{i} 1")
        for j in range(i+1,len(list_result)):
            print(f"{j} 2")
            print(list_result)
            if list_result[i] > list_result[j]:
                list_result[i], list_result[j] = list_result[j],list_result[i]
    print(list_result)
merge([1,5,2,7,8,3,1],[1,2,3])