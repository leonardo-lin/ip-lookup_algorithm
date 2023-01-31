#print("hi")
#print(str(bin(3)))
import sys
count=0
wcount=0
head=0
path = 'text.txt'
f = open("prefix_20211123.txt", 'r')
dic={}
#print(f.read())
for line in f.readlines():
    if head==0:
        head+=1
        continue
    spit=line.split()
    hop=spit[1]
    ori=spit[0].split("/")
    mask=int(ori[1])
    ori=ori
    ori=ori[0].split(".")
    if mask>24:
        continue
        ori=ori[0]+"."+ori[1]+"."+ori[2]+"."+ori[3]
    elif mask<16:
        continue
    else:
        ori=ori[0]+"."+ori[1]+"."+ori[2]
    dic[ori]=hop
f.close()
#print(dic)
f = open("trace_20211123.txt", 'r')

head=0
for line in f.readlines():
    if head==0:
        head+=1
        continue
    tra_spit=line.split()
    answer_hop=tra_spit[1]
    trace_ori=tra_spit[0]
    if trace_ori in dic:
        #print(trace_ori+"   "+dic[trace_ori]+"   "+answer_hop)
        pass
    else:
        trace_ori=(trace_ori.split("."))
        tr=""
        for i in range(int(trace_ori[2])):
            count+=1
            tr=trace_ori[0]+"."+trace_ori[1]+"."+str(int(trace_ori[2])-i)
            #print(tr)
            if tr in dic:
                if dic[tr]==answer_hop:
                    #print("true")
                    pass
                else:
                    #print("false")
                    #print(tr+"   "+dic[tr]+"   "+answer_hop+"   ")
                    #print(trace_ori)
                    pass
                break #find
                    
f.close()

print(count)
print("hashmap node = "+ str(len(dic)))
print("hashmap size = "+ str(sys.getsizeof(dic)))
print("start")
query=input()
if query in dic:
    print(dic[query])
que=query.split(".")
#print(que)
tr=""
for i in range(int(que[2])):
    tr=que[0]+"."+que[1]+"."+str(int(que[2])-i)
    

    if tr in dic:
        print(dic[tr])
        break
        