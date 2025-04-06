from hfmdict import dicthfmChar
from str2compressed import s2c
import sys,str2hfm
inp =  sys.stdin.read()
if inp == '':
    exit()
#转哈夫曼树
lind = str2hfm.s2f(inp)
print(lind)
#转字典
Dind = dicthfmChar(lind)
#转压缩源码
rawcom = s2c(inp,Dind)
print(rawcom)