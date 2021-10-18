def solution(str):
    list=[]
    for i in str:
        list.append(i)
    count={}
    for j  in sorted(list):
        count[j]=list.count(j)
    max(count.values())