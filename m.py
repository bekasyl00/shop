br='I'
bs='V'

i=int(input())
if i<4:
    print(str(br)*i)
elif i==4:
    print(br+bs)
elif i==5:
    print(bs)
elif i>5:
    p=(i-5)*br
   
    print(bs+p)