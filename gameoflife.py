import numpy as np
def main():
    #generating random grid
    dim = input('enter grid dimensions:')
    arr1=np.random.rand(int(dim),int(dim))
    t=0
    #1 is alive, 0 is dead
    for r, c in np.ndindex(arr1.shape):
        if arr1[r,c] < .5:
            arr1[r,c] = 1
        else:
            arr1[r,c] = 0
    arr2=arr1.copy()

    #simulation
    while (t<=1000):
        r=0
        c=0
        for r, c in np.ndindex(arr1.shape):
            neighbors=countNeighbors(arr1,r,c)
            if arr1[r,c]==1:
                if neighbors==1 or neighbors==0:
                    arr2[r,c]=0
                if neighbors>=4:
                    arr2[r,c]=0
                if neighbors==2 or neighbors==3:
                    arr2[r,c]=1
            else:
                if neighbors==3:
                    arr2[r,c]=1
        t=t+1
        print(arr1)
        print(arr2)
        if (np.array_equal(arr1,arr2)):
            break
        arr1=arr2.copy()
    print(t-1)

def countNeighbors(arr,r,c):
    count = 0
    rows, cols=arr.shape
    if c!=cols-1 and arr[r,c+1] == 1:
        count+=1
    if r!=rows-1 and arr[r+1,c] == 1:
        count+=1
    if r!=0 and arr[r-1,c] == 1:
        count+=1
    if c!=0 and arr[r,c-1] == 1:
        count+=1
    if r!=rows-1 and c!=cols-1 and arr[r+1,c+1] == 1:
        count+=1
    if r!=0 and c!=0 and arr[r-1,c-1] == 1:
        count+=1
    if r!=rows-1 and c!=0 and arr[r+1,c-1] == 1:
        count+=1
    if r!=0 and c!=cols-1 and arr[r-1,c+1] == 1:
        count+=1
    return count
for i in range(15):
    main()
#main()