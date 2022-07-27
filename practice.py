import random


# 线性查找,返回所有v  的下标的列表
def linear_search(li,v):
    tmp_li = []
    for i,j in enumerate(li):
        if j == v:
            tmp_li.append(i)
    return tmp_li


# 二分查找,默认列表是有序的，返回一个v的下标
def binary_search(li,v):
    n = len(li)
    left = 0
    right = n-1
    while left<=right:
        mid = (left+right)//2
        if li[mid]<v:
            left = mid+1
        elif li[mid]>v:
            right = mid-1
        elif li[mid] == v:
            return mid
        else:
            return None


# 冒泡排序
def dubbed_sort(li):
    n = len(li)
    for i in range(n-1):
        exchange = False
        for j in range(n-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        if exchange == False:
            return li
    return li


# 选择排序
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[min_loc]>li[j]:
                min_loc = j
        li[min_loc],li[i] = li[i],li[min_loc]
        print(li)


# 插入排序
def insert_sort(li):
    n = len(li)
    for i in range(1,n):
        j = i-1
        tmp = li[i]
        while j>=0 and li[j] > tmp:
            li[j+1] = li[j]
            j-=1
        li[j+1] = tmp
    return li


#  快速排序
def quick_sort(li,left,right):
    if left < right:
        mid = partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

def partition(li,left,right):
    tmp = li[left]
    while left < right:
        while li[right] >= tmp and left < right:
            right -=1
        li[left] = li[right]
        while li[left] <= tmp and left < right:
            left +=1
        li[right] = li[left]
    li[left] = tmp
    # print(li)
    return left


# 堆排序
def heap_sort(li):
    n = len(li)
    for i in range(n // 2 - 1, -1, -1):
        sift(li, i, n - 1)
    for i in range(n-1,-1,-1):
        li[0],li[i] = li[i],li[0]
        sift(li,0,i-1)

def sift(li,low,high):
    tmp = li[low]
    i = low
    j = 2*i+1
    while j<=high:
        if j+1<=high and li[j]<li[j+1]:
            j = j+1
        if li[j]>tmp:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


# topk问题
def topk(li,k):
    li_1 = li[0:k]
    # 建堆
    for i in range(k//2 -1,-1,-1):
        sift(li_1, i, k-1)
    n = len(li)
    # 遍历
    for i in range(k,n-1):
        if li[i]>li[k-1]:
            li[k-1],li[i] = li[i],li[k-1]
            sift(li,0,k-1)
    # 出数
    return li_1


# 归并排序
def merge_sort(li,low,high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

# 当mid左右两边有序时，直接一次归并排序
def merge(li,low,mid,high):
    i = low
    j = mid+1
    li_tmp = []
    while i<=mid and j<=high:
        if li[i]<li[j]:
            li_tmp.append(li[i])
            i+=1
        else:
            li_tmp.append(li[j])
            j+=1
    while i<=mid:
        li.append(li[i])
        i+=1
    while j<=high:
        li.append(li[j])
        j+=1
    li[low:high+1] = li_tmp






li = [9,7,8,9,6,1,2,3,4,5]
# print(li)
merge_sort(li,0,len(li)-1)
print(li)









