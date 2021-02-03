def bubble_sort(alist):
    count = 0
    for j in range(0,len(alist) - 1):#整个数列排序循环
        for i in range(0,len(alist) - 1 - j):
            # 元素从头走到尾，走完一次，排好一个数
            if alist[i] > alist[i + 1]:
                #因为要和下一个数相比，所以i只需要走到len(alist) - 1 - j
                alist[i],alist[i + 1] = alist[i + 1],alist[i]
            print(alist)
            count += 1
    print(count)
if __name__ == "__main__":
    li = [53,26,93,17,77,31,44,55,20,33,2,2,2,3,4,5555,6,6,6,66,67,67,76,77,3,34,34,23,232,3,3]
    print(li)
bubble_sort(li)