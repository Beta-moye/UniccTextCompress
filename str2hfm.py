def s2f(str):
    strDict = {}  #定义字典以计数
    #给文本每个字计数
    for i in range(len(str)):
        if strDict.get(str[i]) == None:
            strDict[str[i]] = 1
        else:
           strDict[str[i]] += 1
    #转为可排序列表
    rtlst = []
    keys = list(strDict.keys())
    for i in range(len(keys)):
        rtlst.append((keys[i],strDict[keys[i]]))
    #构造霍夫曼树
    while not len(rtlst) == 1:
        rtlst.sort(key=lambda a:a[1])
        l1 = rtlst[0][0]
        l2 = rtlst[0][1]
        L1 = rtlst[1][0]
        L2 = rtlst[1][1]
        rtlst.append(('['+ l1 +L1 +']',l2 + L2))
        rtlst.remove((l1,l2))
        rtlst.remove((L1,L2))
    return rtlst
