def tocom(int1):
    int1 = int1.replace('1','2')
    int1 = int1.replace('0','1')
    return int1

def cptext(str0,str1,Dic):
    int0 = Dic[str0]
    int1 = Dic[str1]
    equ = 0
    ret = ''
    for i in range(len(int1) if len(int0) > len(int1) else len(int0)):
        if int1[i] == int0[i]:
            equ += 1
        else:
            break
    if equ == 0:
        ret = '5' + tocom(int1)
    elif equ < ((len(int1)+1)/2):
        int1 = tocom(int1)
        ret = '4' + int1
    else:
        int0 = int0[equ:]
        int1 = int1[equ:]
        ret =  ('3' * (len(int0)+1)) + tocom(int1)
    return ret
#比对并提交合适的路径（1为列表第一项，2为列表第二项，3为返回，4为到最顶层，5为重复录入）
def s2c(Str,Dic):
    restr = ''
    for i in range(len(Str)-1):
        text = cptext(Str[i],Str[i+1],Dic)
        restr += text
        restr = tocom(Dic[Str[0]]) + restr
    return restr
#主函数
