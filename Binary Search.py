def binary_search(a,b):
    index1=0
    index2=len(a)-1
    while index1<=index2:
        mid = (index1+index2)//2
        if a[mid]<b:
            index1=mid+1
        elif a[mid]>b:
            index2=mid-1
        elif a[mid]==b:
                return mid+1
    return None


A=binary_search([1,2,3],2)
print(A)