from copy import copy
import imp
from re import sub
from turtle import hideturtle
from matplotlib.pyplot import cla



class one_arg:
    no=1
    def __init__(self,a):
        self.a=a
    def unify(self,unifer):
        r={}
        if(unifer.name==self.name):
            if(type(unifer.a)==int):
                r[unifer.a]=self.a
            if(type(unifer.a)==str):
                if(unifer.a!=self.a):
                    return None
            return r
        else:
            return None
    def substitute(self,s):
        if self.a in s.keys():
            self.a=s[self.a]
        return 0
    def if_substituted(self):
        if type(self.a)==int:
            return 0
        else:
            return 1
    def is_equal(self,x):
        if(x.name!=self.name):
            return 0
        if(x.a==self.a):
            return 1
        else:
            return 0
    

class two_arg:
    no=2
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def unify(self,unifer):
        r={}
        if(unifer.name==self.name):
            if(type(unifer.a)==int):
                r[unifer.a]=self.a
            if(type(unifer.a)==str):
                if(unifer.a!=self.a):
                    return None

            if(type(unifer.b)==int):
                r[unifer.b]=self.b
            if(type(unifer.b)==str):
                if(unifer.b!=self.b):
                    return None
            return r
        else:
            return None
    def substitute(self,s):
        if self.a in s.keys():
            self.a=s[self.a]
        if self.b in s.keys():
            self.b=s[self.b]
        return 0
    def if_substituted(self):
        if type(self.a)==int:
            return 0
        if type(self.b)==int:
            return 0
        else:
            return 1
    def is_equal(self,x):
        if (x.name!=self.name):
            return 0
        if (x.a!=self.a):
            return 0
        if (x.b!=self.b):
            return 0
        else:
            return 1

class interone(one_arg):
    def __init__(self,name,a):
        super().__init__(a)
        self.name=name
        
        
class intertwo(two_arg):
    def __init__(self,name,a,b):
        super().__init__(a,b)
        self.name=name
        

    
def make_p_array(con,index,facts):
    i=0
    j=0
    p_array=[]
    while(i<len(con)):
        j=0
        while(j<len(index)):
            n=con[i].name
            
            if(index[j]['proposition']==n):
                base=index[j]['pos']
                if(j+1==len(index)):
                    end=len(facts)
                else:                    
                    end=index[j+1]['pos']
                p_array.append([-1,base,end])
                break
            j=j+1
        if(j==len(index)):
            return 0
        i=i+1
    return p_array

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

def check_uniqueness(x):
    arr=list(x.values())
    i=0
    while len(arr)>0:
        v=arr.pop(0)
        if v in arr:
            return 0
        i=i+1
    return 1

def change(p_array):
    i=0
    while i<len(p_array):
        if p_array[i][0]==-1:
            break
        i=i+1
    if i==0:
        return 0
    else:
        if p_array[i-1][0]==p_array[i-1][2]:
            if(i-1>0):
                p_array[i-1][0]=-1                                   
            return 1
            
def sub_con(p_array,facts,con,c):
    cch=change(p_array)
    if(cch==1):
        return -1,{}
    i=0
    sub={}
    while i<len(con) and p_array[i][0]!=-1:
        p=facts[p_array[i][0]]
        con[i].substitute(sub)
        s=p.unify(con[i])
        
        if(s!=None):        
            if (con[i].no==1):
                if(type(con[i].a)==int):
                    sub[con[i].a]=s[con[i].a]
            if (con[i].no==2):
                if(type(con[i].a)==int):
                    sub[con[i].a]=s[con[i].a]
                if(type(con[i].b)==int):
                    sub[con[i].b]=s[con[i].b]
        else:
            return -1, {}
        i=i+1
    
    
    i=0
    while i<len(con):
        if con[i].no==1:
            con[i].a=c[i][0]
        if con[i].no==2:
            con[i].a=c[i][0]
            con[i].b=c[i][1]
        i=i+1
    
    return 1,sub



def copy_c(con):
    i=0
    copy_con=[]
    while i<len(con):
        if con[i].no==1:
            copy_con.append([con[i].a])
        if con[i].no==2:
            copy_con.append([con[i].a,con[i].b])
        i=i+1
    return copy_con



def find_substitute(p_array,facts,con):
    if(p_array==0):
        return []
    cop=copy_c(con)
    
    sub_store=[]
    i=0
    c=1
    j=0
    
    while (p_array[0][0]<p_array[0][2] ):
        while (i<len(p_array)):
            if p_array[i][0]==-1:
                break
            i=i+1
        f=1
        if c==1:
            f=0
            if i==len(p_array):
                sub_store.append(sub)
                i=i-1
                p_array[i][0]=p_array[i][0]+1
                c,sub=sub_con(p_array,facts,con,cop)

            else:
                p_array[i][0]=p_array[i][1]
                c ,sub =sub_con(p_array,facts,con,cop)

        if c==-1 and f==1:
            i=i-1
            p_array[i][0]=p_array[i][0]+1
            c,sub=sub_con(p_array,facts,con,cop)
        j=j+1
    

    i=0
    while i<len(sub_store):
        x=sub_store[i]
        if check_uniqueness(x)==0:
            sub_store.pop(i)
        else:
            i=i+1
    return sub_store

def find_x(x,index,facts):
    j=0
    n=x.name
    while (j<len(index)):
        if index[j]['proposition']==n:
            p=index[j]['pos']
            if j+1==len(index):
                q=len(facts)
            else:
                q=index[j+1]['pos']
                

            break
        j=j+1
    if j==len(index):
        return 0
        
    else:
        while p<q:
            if facts[p].is_equal(x):
                return 1
            p=p+1
        return 0

def add_fact(facts,index,added_fact):
    p=added_fact.name
    i=0
    c=0
    while(i<len(index)):
        if(c==1):
            index[i]['pos']=index[i]['pos']+1
        if(c==0):
            if(index[i]['proposition']==p):
                facts.insert(index[i]['pos'],added_fact)
                c=1
        i=i+1
    if(c==0):
        j=len(facts)
        x={'pos':j,'proposition':p}
        facts.append(added_fact)
        index.append(x)
        
   
    return 0




def add_f(imp,s,index,facts):
    i=0
    c=copy_c(imp)
    while i<len(imp):
        imp[i].substitute(s)
        
        if 0==imp[i].if_substituted():
            return 0
        i=i+1
    i=0
    while (i<len(imp)):
        if find_x(imp[i],index,facts)!=1:
            add_fact(facts,index,imp[i])
        i=i+1
    
    i=0
    
    while i<len(imp):
        if imp[i].no==1:
            imp[i]=interone(imp[i].name,c[i][0])
        if imp[i].no==2:
            imp[i]=intertwo(imp[i].name,c[i][0],c[i][1])
        i=i+1
    return 0



class rules():
    def __init__(self,con,imp):
        self.con=con
        self.imp=imp
    def sub(self,facts,index):
        p_array=make_p_array(self.con,index,facts)
        s=find_substitute(p_array,facts,self.con)
        
        return s
    def make_subs(self,facts,index):
        s=self.sub(facts,index)
        i=0
        while i<len(s):
            add_f(self.imp,s[i],index,facts)
            i=i+1
        return 0











class male(one_arg):
    name='male'
    


class female(one_arg):
    name='female'
    

class parent(two_arg):
    name='parent'
  

class father(two_arg):
    name='father'
   
class mother(two_arg):
    name='mother'
    

class child(two_arg):
    name='child'
    
class couple(two_arg):
    name='couple'
    
class son(two_arg):
    name='son'
    
class doughter(two_arg):
    name='doughter'
   
class sibling(two_arg):
    name='sibling'
    
class brother(two_arg):
    name='brother'
    

class sister(two_arg):
    name='sister'
   

class puncle(two_arg):
    name='puncle'
    
class uncle(two_arg):
    name='uncle'
    

class aunty(two_arg):
    name='aunty'
    
class nephew(two_arg):
    name='nephew'
    
class neice(two_arg):
    name='neice'
    
class couson(two_arg):
    name='couson'
    
class grandparent(two_arg):
    name='grandparent'
    

class grandfather(two_arg):
    name='grandfather'
    

class grandmother(two_arg):
    name='grandmother'
    

rules_list=[]
rules_list.append(rules([parent(1,2)],[child(2,1)]))
rules_list.append(rules([parent(1,2),male(1)],[father(1,2)]))
rules_list.append(rules([parent(1,2),female(1)],[mother(1,2)]))
rules_list.append(rules([child(1,2),male(1)],[son(1,2)]))
rules_list.append(rules([child(1,2),female(1)],[doughter(1,2)]))
rules_list.append(rules([parent(1,2),parent(3,2)],[couple(1,3)]))
rules_list.append(rules([couple(1,2)],[couple(2,1)]))
rules_list.append(rules([sibling(1,2)],[sibling(2,1)]))
rules_list.append(rules([parent(1,2),parent(1,3)],[sibling(2,3)]))
rules_list.append(rules([sibling(1,2),male(1)],[brother(1,2)]))
rules_list.append(rules([sibling(1,2),female(1)],[sister(1,2)]))
rules_list.append(rules([parent(1,2),sibling(1,3)],[puncle(3,2)]))
rules_list.append(rules([puncle(1,2),male(1)],[uncle(1,2)]))
rules_list.append(rules([puncle(1,2),female(1)],[aunty(1,2)]))
rules_list.append(rules([puncle(1,2),couple(1,3)],[puncle(3,2)]))
rules_list.append(rules([puncle(1,2),male(2)],[nephew(2,1)]))
rules_list.append(rules([puncle(1,2),female(2)],[neice(2,1)]))
rules_list.append(rules([parent(1,2),sibling(1,3),child(4,3)],[couson(2,3)]))
rules_list.append(rules([couson(1,2)],[couson(2,1)]))
rules_list.append(rules([grandparent(1,2),male(1)],[grandfather(1,2)]))
rules_list.append(rules([grandparent(1,2),female(1)],[grandmother(1,2)]))
rules_list.append(rules([sibling(1,2),sibling(1,3)],[sibling(1,3)]))
rules_list.append(rules([parent(1,2),couple(1,3)],[parent(3,2)]))
rules_list.append(rules([parent(1,2),parent(3,2),male(1)],[female(3)]))
rules_list.append(rules([parent(1,2),parent(3,2),female(1)],[male(3)]))
rules_list.append(rules([sibling(1,2),parent(3,2)],[parent(3,1)]))
rules_list.append(rules([parent(1,2),parent(3,1)],[grandparent(3,2)]))
