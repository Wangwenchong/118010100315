def a(s):
    m = 1
    print("加密:",end='')
    for p in s:
        if ord("a") <= ord(p) <=ord("z"):
            print(chr(ord("a") + (ord(p)-ord("a")+m) % 26),end='')
            m = m+1
        elif ord("A") <= ord(p) <=ord("Z"):
            print(chr(ord("A") + (ord(p)-ord("A")+m) % 26),end='')
            m = m+1
        else:
            print(p,end='')

def b(k):
    n = 1
    print("解密后:",end='')
    for p in k:
        if ord("a") <= ord(p) <=ord("z"):
            print(chr(ord("a") + (ord(p)-ord("a")-n) % 26),end='')
            n = n+1
        elif ord("A") <= ord(p) <=ord("Z"):
            print(chr(ord("A") + (ord(p)-ord("A")-n) % 26),end='')
            n = n+1
        else:
            print(p,end='')

s = input("请输入需要加密的信息：")
k = input("请输入需要解密的信息：")
a(s)
print('')
b(k)
