'''
a = 0xA2
d = int(a)
s = ""
mapD = {10:'A',2:'2'}
while d > 0:
    s = s + mapD[d%16]
    d = d//16

print(s[::-1])


a = "hello"

print(a[:-2])

he = '0x123'

print(int(he,16))

print(hex(int(he,16)))

a = ['0','0','0','0','1','2','3']

if a[0:3] == ['0','0','0']:
    a[0:3] = 'T'
print(a)
'''
'''
s = 'abcd'
l = list(s)
print(l)
ss = ""
for ll in l:
    #print(ll)
    ss = ss + ll

print(ss)

prices = [7,1,5,3,6,4]
min = prices[0]
index = 0
for i in range(0,len(prices)):
    if prices[i] < min :
        min = prices[i]
        index = i
        
newlst = prices[index+1::]
        
max = 0
for i in newlst:
    if i > max:
        max = i
print(max,min)
print(max-min)


for i in range(int(input())):
    
    l = []
    s=input()
    l=s.split()
   
    sum=0
    for j in l:
        sum = sum+int(j)
        
    if sum>6:
        print("YES")
    else:
        print("NO")

# cook your dish here

def rowflip(row):
    outrow=[]
    mid = len(row)//2 + 1
    
    flag=0
    
    half = row[:mid:]
    back = row[mid::]
    
    print(half)
    print(back)

    for i in range(len(back)):
        outrow.append(half[i])
        outrow.append(back[i])

    outrow.append(half[-1])
    return outrow

    

print(rowflip([1,2,3,4,5]))
'''

# cook your dish here
def test(m,slices):
    count = 0
    flag =True
    while count <len(slices) :
        
        if slices[count] < m:
            count+=1
            continue
        elif slices[count] == m:
            m=m-1
            count+=1
        else:
            flag = False
            count+=1
            break
    
    return flag


for i in range(int(input())):
    
    slices=[]
    n,q = map(int,input().split())
    s = input().split()
    
    for j in range(len(s)):
        s[j] = int(s[j])
        
    for k in range(q):
        l,r = map(int,input().split())
        slices = s[l-1:r:]
        
        max = slices[0]
        maxin = 0

        for x in range(0,len(slices)):
            if slices[x] > max:
                max = slices[x]
                maxin = x
        
        if test(max,slices) == True :
            print(max)
        else:
            print(max+1)
    

    


    