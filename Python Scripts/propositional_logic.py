
from family_class import *

facts=[parent('a','b'),parent('d','c'),parent('e','d'),sibling('h','c'),couple('a','d'),male('a'),female('d')]



def check_uniqueness(x):
    arr=list(x.values())
    i=0
    while len(arr)>0:
        v=arr.pop(0)
        if v in arr:
            return 0
        i=i+1
    return 1
x={1: 'd', 2: 'c', 3: 'c'}






def indexing(facts):
    i=0
    j=0
    index=[]
    proposition=(facts[0].name)
    while(i<len(facts)):
        p=facts[i].name
        if(p==proposition):
            i=i+1
        else:
            index.append({'pos':j,'proposition':proposition})
            proposition=p
            j=i
            i=i+1
    index.append({'pos':j,'proposition':p})
    return index









def show_con(con):
    i=0
    while(i<len(con)):
        n=con[i].name
        if(con[i].no==1):
            print(n,con[i].a)
        if(con[i].no==2):
            print(n,con[i].a,con[i].b)
        i=i+1
    return 0

index=(indexing(facts))
'''
(rules([parent(1,2),couple(3,1)],[parent(3,2)]).make_subs(facts,index))
(rules([parent(1,2),parent(1,3)],[sibling(2,3)]).make_subs(facts,index))
rules([parent(1,2),male(1)],[father(1,2)]).make_subs(facts,index)
(rules([parent(1,2),couple(1,3)],[parent(3,2)]).make_subs(facts,index))
rules([parent(1,2),parent(3,1)],[grandparent(3,2)]).make_subs(facts,index)
rules([couple(1,2)],[couple(2,1)]).make_subs(facts,index)
rules([parent(1,2),female(1)],[mother(1,2)]).make_subs(facts,index)
rules([sibling(1,2)],[sibling(2,1)]).make_subs(facts,index)
rules([parent(1,2),sibling(2,3)],[parent(1,3)]).make_subs(facts,index)
rules([parent(1,2),parent(3,1)],[grandparent(3,2)]).make_subs(facts,index)
'''
def run_unify(rules_list,facts,index):
    i=0
    nof=1
    cof=0
    while(nof>cof):
        cof=nof
        while(i<len(rules_list)):
            rules_list[i].make_subs(facts,index)
            i=i+1
        nof=len(facts)
        print(nof)
    return 0
run_unify(rules_list,facts,index)

con=[parent(1,2),female(1)]
p_array=make_p_array(con,index,facts)
print(find_substitute(p_array,facts,con))
run_unify(rules_list,facts,index)



#add_f(imp,s,index,facts)
print("hello")
show_con(facts)
#print(facts)
#print(find_x(uncle('c','n'),index,facts))




#show_con(con)
#print(sub_con(p_array,facts,con,c))





