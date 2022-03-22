def GenerateBBSTArray(a):
    BBSTArray = [None]*len(a)
    a = sorted(a)
    index = 0
    def recurs_BBSTArray(a, BBSTArray, index):
        if len(a) == 0: return
        BBSTArray[index] = a[len(a)//2]
        left_branch = a[0:len(a)//2]
        left_index = 2*index+1
        right_branch = a[len(a)//2+1:]
        right_index = 2*index+2
        recurs_BBSTArray(left_branch, BBSTArray, left_index)
        recurs_BBSTArray(right_branch, BBSTArray, right_index)
    recurs_BBSTArray(a, BBSTArray, index)
    return BBSTArray
