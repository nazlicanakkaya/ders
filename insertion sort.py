#insertion sort

def sort(a):
    for i in range(1,len(a),1):
        k=a[i]
        j=0
        while k>a[j]:
            j=j+1
        a[j+1:i+1]=a[j:i]
        a[j]=k
        print(a)
    return a
