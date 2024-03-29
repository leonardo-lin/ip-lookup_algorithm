# Explanation of the problem
## in this work we will have to find the "next hop" with the given IP address
### ip will be show as the following format

IP Address      
103.25.85.161      
187.223.245.98       
204.16.22.49        
23.211.110.7       
178.237.221.179    
74.119.238.125      

### and you have to find the next hop with a rule prefix table to find the next hop
rule table：
|Prefix        |       Next Hop|
| --- | --- |
|0.0.0.0/0      |      32.13.45.147 |
|1.0.0.0/24     |      92.40.106.120 |
|1.0.4.0/22      |     43.103.243.56 |
|1.0.4.0/24      |     66.202.235.230 |
|1.0.64.0/18      |    210.188.172.185 |
...
|223.255.250.0/24  |   160.189.193.58 |
|223.255.251.0/24  |   118.215.125.249 |
|223.255.252.0/24   |  247.87.225.249 |
|223.255.253.0/24   |  220.76.84.104 |
|223.255.254.0/24   |  165.251.122.152 |

Let's learn how to read this table first</br>
All ip's can be considered as a 32bit code such as </br>
1.2.3.4 -> 00000001 00000010 00000011 00000100</br>
the number after "/" is called mask such as 1.2.3.4/"24". That means we only have to consider the first "mask bits" of IP table. Using 1.2.3.4/24 we can have</br>
00000001 00000010 00000011 xxxxxxxx (x=don't care)</br>
If the input ip matches this rule than we find the next hop (1.2.3.128 matches 1.2.3.4/24 find 92.40.106.120 as next hop)</br>

---

# solve the problem 
there are two way to fix the problem 1.binary search 2.hash</br>
binary search cost more time but it use less space</br>
hash has the opposite advantage and disadvantage</br>

I choose hash to solve this problem and I find that there's a Strange Phenomenon in the prefix table. Over 99 of the rule have the mask between 16 to 24 so I only solve these rule (actually I have solve other does not fit in this range, but I didn't haha) </br>

for method of hash let's looking at the follwing example</br>
given input 1.0.0.128</br>
I check :</br></br>
1.0.0.128</br>
1.0.0.64(128/2)</br>
1.0.0.32(64/2)</br>
...</br>
1.0.0.2</br>
1.0.0.1</br>
1.0.0.0</br>
so I find 1.0.0.0 is in the hash table and the next hop is 92.40.106.120</br>

# inference
if you want to run the code you have to download the following file</br>
[prefix file](https://drive.google.com/file/d/1gmu6AkGuIDF0V27t8sfDxx1abGtkgpa3/view?usp=sharing)</br>
[trace file](https://drive.google.com/file/d/1GOHjsDsryoj0CR6dMlOmOo4Med7nt4qd/view?usp=sharing)</br>
inside prefix file is the prefix table and you can try it with trace file(answer). Insert any IP in trace file and test if it's next hop is equal to the output from "inference.py"

# example
![image](https://user-images.githubusercontent.com/67550587/215998254-56676df1-0d12-4259-8601-a9fe76dcd7e2.png)

