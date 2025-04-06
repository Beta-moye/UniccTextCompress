'''def ChrGV(hfm,Chr):
    ranger = hfm
    for i in range(len(Chr)):
        ranger = ranger[int(Chr[i])]
    return ranger
顺便写的，没啥用'''
def IntoRange(hfm,fgive,dict):
    if isinstance(hfm,str):#这个函数用于迭代来遍历霍夫曼树的每一层
        dict[hfm] = fgive
    else:
        fgive = fgive + '0'
        ghfm = hfm[0]
        dict = IntoRange(ghfm,fgive,dict)
        fgive =fgive[:len(fgive)-1] + '1'
        ghfm = hfm[1]
        dict = IntoRange(ghfm,fgive,dict)
    return dict
def dicthfmChar(hfm):
    Edict = {}
    Num = ''
    IntoRange(hfm,Num,Edict)
    return Edict