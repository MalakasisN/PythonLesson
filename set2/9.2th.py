def decompress(y):
    s=''
    nums='1234567890'
    c=''
    for i in range(0,len(y)+1):
        if i==len(y)-1:
            c+=y[i]
            s+=int(c)*y[i-len(c)]
            break
        if not y[i] in nums:
            if c=='':
                continue
            else:
                s+=int(c)*y[i-len(c)-1]
                c=''
        if y[i] in nums:
            c+=y[i]
    print(s)
decompress('a2h1t1o3t1o3t3u4-11o1')