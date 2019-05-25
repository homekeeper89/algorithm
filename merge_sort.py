import random

# recursion 이용 
def performMergeSort(lstElementToSort): # sorting하고자 하는 리스트 받음. 
    # 얘가 escape routine이 됨.
    if len(lstElementToSort) == 1:
        return lstElementToSort

    lstSubElementToSort1 = []
    lstSubElementToSort2 = []
    for itr in range(len(lstElementToSort)):
        if len(lstElementToSort)/2 > itr: # 절반은 첫번째꺼에 넣고
            lstSubElementToSort1.append(lstElementToSort[itr])
        else: # 나머지는 두번째꺼에 넣음.
            lstSubElementToSort2.append(lstElementToSort[itr])
            
    lstSubElementToSort1 = performMergeSort(lstSubElementToSort1)
    lstSubElementToSort2 = performMergeSort(lstSubElementToSort2)
    # 여기까지 Decomposition !!
    
    idxCount1 = 0 # 여기부터 Aggregation !! 
    idxCount2 = 0
    for itr in range(len(lstElementToSort)):
        if idxCount1 == len(lstSubElementToSort1):
            lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 = idxCount2 + 1
        elif idxCount2 == len(lstSubElementToSort2):
            lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 = idxCount1 + 1
        elif lstSubElementToSort1[idxCount1] > lstSubElementToSort2[idxCount2]:
            lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 = idxCount2 + 1
        else:
            lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 = idxCount1 + 1
    return lstElementToSort

lstRandom = []
for itr in range(0,10):
    lstRandom.append(random.randrange(0,100))
print (lstRandom)
lstRandom = performMergeSort(lstRandom)
print (lstRandom)