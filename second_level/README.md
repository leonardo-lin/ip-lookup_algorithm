# Explanation of the problem

## In this work we find the first rule that is met

the input rule will be show as the following format</br>
4238902869 1620785308 0 5631 6 //479</br>

Our task is to find the first rule that matches in order from the table</br>

the rule table will be show as the following format</br>
@230.86.143.212/32 122.58.92.251/32 5530 : 5530 514 : 514 0x11/0xFF</br>
@241.220.251.170/32 96.112.121.80/32 137 : 137 1723 : 1723 0x11/0xFF</br>
@241.193.234.112/32 96.112.121.84/32 1433 : 1433 5530 : 5530 0x11/0xFF</b</br>r>
@210.41.248.166/32 73.9.237.115/32 80 : 80 80 : 80 0x11/0xFF</br></br>
...</br>
@0.0.0.0/0 189.254.0.0/16 0 : 65535 0 : 65535 0x00/0x00</br>
@0.0.0.0/0 191.211.0.0/16 0 : 65535 0 : 65535 0x00/0x00</br>
@0.0.0.0/0 0.0.0.0/0 0 : 65535 0 : 65535 0x01/0xFF</br>
@0.0.0.0/0 0.0.0.0/0 0 : 65535 0 : 65535 0x06/0xFF</br>
@0.0.0.0/0 0.0.0.0/0 0 : 65535 0 : 65535 0x33/0xFF</br>
@0.0.0.0/0 0.0.0.0/0 0 : 65535 0 : 65535 0x00/0x00</br>

### the first rule in the table has the highest priority </br>
### Each column is a rule, consisting of five fields. The first two columns are IP Address Prefixes, the third and fourth columns are any range of Transport-layer Port, before the colon is the start point of the range, after the colon is the end point of the range, the last column is Protocol, and the value after the slash is 0x00 means the field is wildcard , if it is 0xff, a single Protocol value before the slash.</br>


# solve the problem

The most basic way to solve the problem is search the table linearly
Most of the researchers used to solve it with binary tree or hashmap. they find the the appropriate IP address pair and check that which pair of IP address pair has the correct range of port, correct protocol and has the highest priority.

# How I deal with it
I still choose to use the basic way:linear. But different from the basic way, I simulate it with parallel processing. I cut the table into many small table so that it can simulate that there are many routers and each of them just need to deal with a small table. After each router find the first rule in there table, the router which find a rule(some router don't have the correct rule) and has the highest priority will output the answer
![image](https://user-images.githubusercontent.com/67550587/216061475-d8bc8c88-e08b-4ccc-8def-b3afea3c740d.png)
![image](https://user-images.githubusercontent.com/67550587/216061524-380cc8de-2e59-406f-8afb-d5e40e73b4d1.png)
![image](https://user-images.githubusercontent.com/67550587/216061563-b1fe1384-1a7e-4c37-b7cd-ad7201327716.png)

# example
![image](https://user-images.githubusercontent.com/67550587/216061833-e100ebb2-4249-457b-8bd0-db30a1acebdc.png)




