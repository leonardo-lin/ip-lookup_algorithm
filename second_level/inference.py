# -*- coding:utf-8 -*-
#verified
"""new_access='1600753409 3271393328 65535 21 6 413'
new_access=new_access.split()
print(new_access)


"""

def ver_ip(sor,ver):
    check=False
    cnt=2
    #print(ver,sor) 
    while(ver>=sor):
        #print(ver,sor)
        if ver==sor:
            check=True
            break
        ver=ver//cnt
        ver=ver*cnt
        #print(ver)
        cnt*=2
    return check


def verified(inpt,ver):
    ech=inpt.split()


    #source ip
    tmp=ech[0].split('@')
    #print(tmp)
    tmp=tmp[1].split('.')
    tm=tmp[3].split('/')
    #print(tm)
    tmp.pop()
    tmp.append(tm[0])
    tmp.append(tm[1])
    #print(tmp)
    #source_ip=tmp
    tm=0
    #print(tmp)
    for i in range(4):
        tm=tm+(int(tmp[3-i])*(256**i))
        #print(tm)
    #print(tm)
    source_ip=tm
    #print('source_ip = ',source_ip)

    #destination_ip
    tmp=ech[1].split('.')
    tm=tmp[3].split('/')
    #print(tm)
    tmp.pop()
    tmp.append(tm[0])
    tmp.append(tm[1])
    #print(tmp)
    tm=0
    for i in range(4):
        tm=tm+(int(tmp[3-i])*(256**i))
    #print(tm)
    destination_ip=tm
    #print('destination_ip = ',destination_ip)

    source_from=int(ech[2])
    source_end=int(ech[4])
    des_from=int(ech[5])
    des_end=int(ech[7])
    pac_type=ech[8][0:4]
    wirec=ech[8][-2]+ech[8][-1]
    #print(source_ip,destination_ip,source_from,source_end,des_from,des_end,pac_type,wirec)
    #print(ech)
    #deal with rule

    ver=ver.split(' ')
    for i in range(len(ver)):
        ver[i]=int(ver[i])
    #print(ver)
    check=True
    if ver_ip(source_ip,ver[0]) ==False:
        check=False
        #print('sor',check)
    if ver_ip(destination_ip,ver[1]) == False:
        check=False
        #print('des',check)
    if ver[2]<source_from or ver[2]>source_end or ver[3]<des_from or ver[3]>des_end:
        check=False
        #print('port',check)
    if wirec =='FF':
        #print(pac_type)
        #pac_type=int(pac_type[1])+int(pac_type[0]*16)3840+240+10
        
        
            #print(pac_type)
        #print(pac_type,ver[4])
        pac_type=int(pac_type,16)
        if int(ver[4])!=(pac_type):
            check=False
            #print('type',check,ver[4],pac_type)

    return check


if __name__ == '__main__':
    
    cut=64
    inpt=[]
    inpt2=[]
    f = open('ipc1_10K.txt', 'r')
    f2 = open('ipc1_10K_trace.txt','r')
    i=0
    for line in f2.readlines():
        i+=1
        if i==200:
            break
        #inpt2.append(line)
    #print(len(inpt2))
    
    for line in f.readlines():
        inpt.append(line)
    #print(len(inpt))
    li_inpt=[]
    head=0
    part=int(len(inpt)/cut)
    for i in range(cut):
        end=head+part
        if head+part>len(inpt):
            end=len(inpt)-1
        li_inpt.append(inpt[head:end])
        head=end
        if head==len(inpt)-1:
            break
    li_inpt.append(inpt[head:len(inpt)])
    #print(len(li_inpt[64]))
    
    """cnt=0
    cnt2=0
    for i in range(len(inpt2)):
        for j in range(len(inpt)):
            cnt+=1
            if verified(inpt[j],inpt2[i])==True:
                #print(inpt2[i],inpt[j],i,j,"find")
                #k=input()
                #print(j)
                cnt2+=1
                break           
    print(len(inpt2))
    print(cnt2)
    print(cnt)"""
    question=input() #測試時改這裡!!!!!!!!!!!
    inpt2=[question]
    cutcnt=[]
    for k in range(cut+1):
        cnt=0
        cnt2=0
        for i in range(len(inpt2)):
            for j in range(len(li_inpt[k])): 
                cnt+=1
                if verified(li_inpt[k][j],inpt2[i])==True:
                    #print(inpt[j],k,'rule',j+1,"find")
                    #print(j)
                    cnt2+=1
                    break  
    #    print(cnt2)
        #print(k,'執行次數',cnt)
        cutcnt.append(cnt)
    #print(len(inpt2))
    print(cutcnt)
    answers=0
    for i in range(len(cutcnt)):
        answers+=cutcnt[i]
        if cutcnt[i]!=cutcnt[i+1]:
            answers+=cutcnt[i+1]
            break
    print('查找次數=',max(cutcnt))
    print(answers)
    f2.close()
    f.close()