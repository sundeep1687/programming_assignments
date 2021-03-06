#Program to add a single number until we reach single digit
#eg: 38: 3+8=11: 1+1=2
def maxprofit(ary):

    max=-9999
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):
            num=ary[j]-ary[i]
            if i==0 and j==0:
                max=num
            elif num>max:
                max=num

    print(max)

def multiply(ary):

    left=[1]*len(ary)
    right=[1]*len(ary)
    prod=[1]*len(ary)

    for i in range(1,len(ary)):
        left[i]=ary[i-1]*left[i-1]

    for i in range(len(ary)-2,-1,-1):
        right[i]=ary[i+1]*right[i+1]

    for i in range(0,len(ary)):
        prod[i]=left[i]*right[i]

    print(prod)

def binsrch(ary,n):

    left=0
    right=len(ary)-1
    mid=int((left+right+1)/2)

    while n!=ary[mid]:
        if n<ary[mid]:
            right=mid-1
        else:
            left=mid+1
        mid = int((left + right+1) / 2)

    print(mid)

def binsrch(ary,n):

    left=0
    right=len(ary)-1
    mid=int((left+right+1)/2)

    while n!=ary[mid]:
        if n<ary[mid]:
            right=mid-1
        else:
            left=mid+1
        mid = int((left + right+1) / 2)

    print(mid)

def reversenum(num):
    lst=[]

    neg_flg=False
    if num<0:
        num=num*(-1)
        neg_flg=True

    while num!=0:
        lst.append(str(num%10))
        num=int(num/10)

    if neg_flg==True:
        print(int(''.join(lst))*-1)
    else:
        print(''.join(lst))

def secondmax(ary):

    for i in range(0,len(ary)):
        if i==0:
            max=ary[i]
        elif ary[i]<max:
            if i==1:
                sec_max=ary[i]
            elif sec_max>ary[i]:
                sec_max=ary[i]
        elif ary[i]>max:
            sec_max=max
            max=ary[i]

    print(max)
    print(sec_max)

def sumofnum(ary):

    for i in range(0,len(ary)):
        if i==0:
            max=ary[i]
        elif ary[i]<max:
            if i==1:
                sec_max=ary[i]
            elif sec_max>ary[i]:
                sec_max=ary[i]
        elif ary[i]>max:
            sec_max=max
            max=ary[i]

    print(max)
    print(sec_max)

def numsum(num):

    while num>10:
        sum=0
        while num!=0:
            sum=sum+num%10
            num=int(num/10)
        if sum>9:
            num=sum

    print(sum)


def groupanagrams(ary):

    lst={}

    for i in range(0,len(ary)):
        key=''.join(sorted(ary[i]))
        if key in lst.keys():
            lst[key].append(ary[i])
        else:
            lst[key]=[]
            lst[key].append(ary[i])

    for key,val in lst.items():
        print(val)

def gcd(num1,num2):

    if num1<num2:
        small=num1
        large=num2
    else:
        small=num2
        large=num1

    while large%small!=0:
        tmp=small
        small=large%small
        large=tmp

    print(small)

def stringreverse(str1):

    tmp=[]
    for i in range(len(str1)-1,-1,-1):
        tmp.append(str1[i])

    print(tmp)
    print(''.join(tmp))

def twosum(num1,num2):

    num1=str(num1)
    num2=str(num2)

    carry=0
    val=0
    if len(num1)>len(num2):
        maxlen=len(num1)
    else:
        maxlen=len(num2)

    lst=[]
    print(num1,num2)
    for i in range(0,maxlen):
        val=carry
        if i<len(num1):
            val=val+ord(num1[len(num1)-1-i])-48
        if i <len(num2):
            val=val+ord(num2[len(num2)-1-i])-48
        if val>9:
            carry=int(val/10)
        lst.append(str(val%10))

    lst.reverse()
    print(lst)
    print(''.join(lst))

def adddigits(num):

    while True:
        sum=0
        while num!=0:
            sum=sum+num%10
            num=int(num/10)
        if sum>9:
            num=sum
        else:
            break

    print(sum)

def firstunique(str1):

    lst={}
    for i in range(0,len(str1)):

        key=str1[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1

    for i in range(0,len(str1)):

        key=str1[i]

        if lst.get(key)==1:
            print(i)
            break

def poweroftwo(n):

    if n%2!=0:
        print('Number is NOT power of 2')
    else:
        while True:
            n=int(n/2)
            print(n)
            if n==1:
                print('Number is power of 2')
                break
            elif n%2!=0:
                print('Number is NOT Power of 2')
                break
            else:
                continue

def happynumber(n):

    sum=0
    while True:
        while n!=0:
            sum=sum+(n%10)*(n%10)
            n=int(n/10)
        if sum>9:
            n=sum
            sum=0
        elif sum==1:
            print('Happy Number')
            break
        else:
            print('Sad Number',n)
            break

def gcd(num1,num2):

    if num1>num2:
        large=num1
        small=num2
    else:
        large=num2
        small=num1


    while large%small!=0:
        tmp=large%small
        large=small
        small=tmp

    print(small)

def palindromenumber(num):

    lst=[]
    n=num
    while n!=0:
        key=n%10
        lst.append(str(key))
        n=int(n/10)

    if num==int(''.join(lst)):
        print('Number is palindrome')
    else:
        print('Number is NOT palindrome')

def cumsum(ary):

    sum=0
    lst=[0]*len(ary)
    for i in range(0,len(ary)):
        sum=sum+ary[i]
        lst[i]=sum
    print(lst)

def oddposition(ary):

    lst=[]
    for i in range(0,len(ary)):
        if i%2==1:
            lst.append(ary[i])
        else:
            continue
    print(lst)

def binarysearch(ary,num):

    st=0
    end=len(ary)-1
    print(ary)
    while st<end:
        mid=int((st+end)/2)
        print(mid)
        if num<ary[mid]:
            end=mid-1
        elif num>ary[mid]:
            st=mid+1
        else:
            return mid
    return -1

def secondmax(ary):

    max=0
    sec_max=0

    for i in range(0,len(ary)):
        if i==0:
            max=ary[i]
            sec_max=ary[i]
        elif ary[i]>max:
            sec_max=max
            max=ary[i]

    print(max,sec_max)

def reversearray(ary):

    st=0
    end=len(ary)-1
    print(ary)
    while st<end:
        tmp=ary[st]
        ary[st]=ary[end]
        ary[end]=tmp
        st=st+1
        end=end-1
    print(ary)

def reversewords(str1):

    tmp=''
    st=0
    end=0
    flg=True

    for i in range(len(str1)-1,-1,-1):

        if str1[i]==' ' or i==0:
            if i==0:
                st=0
            else:
                st=i+1
            if tmp=='':
                tmp=str1[st:end]
            else:
                tmp=tmp+' '+str1[st:end]
            flg=True

        else:
            if flg==True:
                end=i+1
                flg=False
    print(tmp)

def median(ary):

    if len(ary)%2==0:
        indx1=int(len(ary)/2)-1
        indx2=int(len(ary)/2)

        tmp=(ary[indx1]+ary[indx2])/2
        print(tmp)
    else:

        indx=int(len(ary)/2)
        print(ary[indx])

def wordpattern(str1,pattern):

    j=0
    st=0
    end=0
    lst={}
    ptrn_flg=True

    for i in range(0,len(str1)):
        key=str1[i]
        flg=1
        print('sayee')
        while j<len(pattern):
            if pattern[j]==' ' or j+1==len(pattern):
                end=j
                tmp=pattern[st:end]
                print(tmp)
                if key in lst.keys():
                    val=lst.get(key)
                    if tmp==val:
                        j=j+1
                        break
                    else:
                        ptrn_flg=False
                        j=j+1
                        break
                else:
                    lst[key]=tmp
                    j=j+1
            else:
                if flg==1:
                    st=j
                    flg=0
                    print('kartik')
                j=j+1
        if ptrn_flg==False:
            break
    print(lst)
    if ptrn_flg==False:
        print('String are not in pattern')
    else:
        print('Strings are in pattern')

def compression(str1):

    prev_char=''
    cnt=0
    tmp=''
    for i in range(0,len(str1)):

        if i==0:
            prev_char=str1[i]
            cnt=cnt+1
        elif str1[i]==prev_char:
            cnt=cnt+1
        else:
            if tmp=='':
                tmp=prev_char+str(cnt)
            else:
                tmp=tmp+prev_char+str(cnt)
            cnt=1
        prev_char=str1[i]

    tmp=tmp+prev_char+str(cnt)
    print(tmp)

def palindrome(str1):

    st=0
    end=len(str1)-1
    flg=True

    while st<end:
        if str1[st]!=str1[end]:
            flg=False
            break

        st=st+1
        end=end-1
    if flg==True:
        print('Palindrome')
    else:
        print('Not Palindrome')


def wordcount(str1):

    st=0
    end=0
    flg=True
    lst={}
    for i in range(0,len(str1)):
        if str1[i]==' ' or i==len(str1)-1:

            if prev_char==' ':
                prev_char=str1[i]
                continue
            else:
                if i==len(str1)-1:
                    end=i+1
                else:
                    end=i
                key=str1[st:end]
                flg=True
                if key in lst.keys():
                    lst[key]=lst.get(key)+1
                else:
                    lst[key]=1
                prev_char = str1[i]
        else:
            if flg==True:
                st=i
                flg=False
            prev_char=str1[i]


    print(lst)

def main():

    #str1='kartik'
    #palindrome(str1)

    str1='The sky    is blue  in  sayee today in Seattle sayee kartik     '
    wordcount(str1)
    #ary=[12,11,15,3,10]
    #maxprofit(ary)

    #ary=[1,2,3,4]
    #multiply(ary)

    #ary=[1,3,4,6,7,34,45,78]
    #n=34
    #binsrch(ary,n)

    #num=-1234
    #reversenum(num)

    #ary=[3,4,8,1,5,-2,43]
    #secondmax(ary)

    #num=87459
    #numsum(num)

    #ary = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    #groupanagrams(ary)

    #num1=8
    #num2=12
    #gcd(8,12)

    #str1='kartiksayee'

    #stringreverse(str1)

    #num1=345
    #num2=5688

    #twosum(num1,num2)

    #num=9878

    #adddigits(num)

    #str1='loveleetcode'

    #firstunique(str1)

    #n=64

    #poweroftwo(n)

    #n=19
    #happynumber(n)

    #num1=24
    #num2=60
    #gcd(num1,num2)

    #num=7447
    #palindromenumber(num)

    #ary=[2,45,7,-2]
    #cumsum(ary)

    #ary=[0,1,2,3,4,5]
    #oddposition(ary)

    #ary = [5, 89, 20, 64, 19, 57, 45, 23, 67, 32, 30]
    #ary.sort()

    #num=45
    #print('The index is',binarysearch(ary,num))

    #ary = [3, 4, 8, 1, 5, -2, 43]
    #secondmax(ary)

    #reversearray(ary)

    #str1='Dog Bites Man'
    #reversewords(str1)

    #ary1 = [5, 89, 20, 64, 20, 45]
    #ary2 = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]

    #ary1.sort()
    #ary2.sort()
    #print(ary1)
    #print(ary2)

    #median(ary1)
    #median(ary2)

    #str1 = 'abba'
    #pattern = 'dog cat cat dog'

    #wordpattern(str1, pattern)

    #str1 = 'aabcccccaa'

    #compression(str1)

if __name__=='__main__':
    main()