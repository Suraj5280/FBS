def binarySearch(li,searchEle):
    beg = 0
    end = len(li) -1
    while(beg <= end):
        mid = (beg + end)//2
        if(searchEle == li[mid]):
            return mid
        elif(searchEle < li[mid]):
            print('less than')
            end = mid - 1
        elif(searchEle > li[mid]):
            beg=mid+1
    else:
        return -1

ele = int(input('enter element to find:'))
li = [40,67,23,89,56,13,10,90]

res = binarySearch(li, ele)
#print(res)
if(res != -1):
    print(f'{ele} is present at index {res}.')
else:
    print(f'{ele} is not present in list.')