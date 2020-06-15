'''
from tkinter import *
root = Tk()
root.title("Mancala GUI")
'''

import time
import random
from pympler import asizeof

class Login:

    def __init__(self):

        self.username = "kalpanabaheti"
        self.password = "12345"

    def accept(self):

        u = input("\nEnter username: ")
        p = input("\nEnter password: ")

        if u!=self.username or p!=self.password:
            return 0
        else:
            return 1


class Mancala:


    def __init__(self):

        self.me=[]
        self.you=[]
        self.combo=[]
        print("\nGAME: ",asizeof.asized(self.combo, detail=1).format())
        self.result=[]
        self.myhome=0
        self.yourhome=0
        self.flag=None
 

        

        for i in range(0,6):
            self.me.append(4)
            self.you.append(4)

        


        
    def show(self):

        for i in range(0,6):
            print("   ",self.you[i], end='     ')
        print("\n\n")
        print("\n",self.yourhome,"\t\t\t\t\t\t\t",self.myhome)
        print("\n\n")
        for i in range(0,6):
            print("   ",self.me[i], end='     ')

        print("\n\n\nMY HOME: ",self.myhome)
        print("\nYOUR HOME: ",self.yourhome)

        

    def iprepare1(self):
        
        self.you.reverse()
        self.me.append(self.myhome)
        self.combo=self.me+self.you
        self.flag=0

        

    def iprepare2(self):

        self.myhome = self.combo[6]
        self.you = self.combo[7:]
        self.you.reverse()
        self.me = self.combo[0:6]
        self.show()

    def youprepare1(self):

        self.you.reverse()
        self.you.append(self.yourhome)
        self.combo = self.you+self.me
        self.flag = 0

    def youprepare2(self):

        self.yourhome = self.combo[6]
        self.me = self.combo[7:]
        self.you = self.combo[0:6]
        self.you.reverse()
        self.show()

    def decision(self):

        maxi=0
        arrt=[]
        pos=random.randint(0,5)

        for k in range(6):

            t = self.combo[:]
            initial = t[6]
            f=0
            j=k

            while (f==0 and t[k]!=0) or (f==1 and t[k]!=1 and k!=6):

                f=1

                temp = t[k]
                t[k]=0

                for i in range(temp):

                    k+=1
                    k%=13
                    t[k]+=1

            if k!=6 and t[12-k]!=0:

                final = t[6] + t[12-k]+ 1
                x = final-initial
                arrt.append(x)

                if x>maxi:

                    maxi=x
                    pos=j

        return pos

    
                
    def getcup(self):
        
        cup = int(input("\nEnter cup number please: "))
        return cup


    def savestate(self):

        t = temp=self.buffer()
        return t
        
        
        

    def buffer(self):

        buff = self.combo[:]
        return buff
                


    def play(self,k,p):

        if self.combo[k]==0:
            return 2

        elif k!=6 and (self.combo[k]!=1 or self.flag==0):

            self.flag=1

            temp = self.combo[k]
            self.combo[k]=0

            for i in range(temp):

                k+=1
                k%=13
                self.combo[k]+=1
            
            print("\t\t",self.combo)
            return self.play(k,p)

        elif k==6:
            
            if p==1:
                self.iprepare2()
            elif p==2:
                self.youprepare2()
            return 0

        else:

            print("\n",self.combo)

            if self.combo[12-k]!=0:

                print("\n final slot: ",k+1," and taking slot: ",13-k)
                self.combo[6]+=self.combo[12-k]+1
                self.combo[k]=0
                self.combo[12-k]=0
                if p==1:
                    self.iprepare2()
                elif p==2:
                    self.youprepare2()

            else:
                
                if p==1:
                    self.iprepare2()
                elif p==2:
                    self.youprepare2()

            return 1


    def check(self):

        if self.myhome>=24:
            return 1
        elif self.yourhome>=24:
            return 0
        else:
            return 999

            

    
       
            

        
        

#main environment

m = Mancala()
'''
print(asizeof.asized(m, detail=1).format())
'''
x = Login()
'''
open1 = [
'''
teach = [['This choice you made with cup number', 'ended up in this manner: ', 'And you earned your home ', 'marbles which is good but if you look closer there was another option you could’ve taken, which was', 'Now you see, if you had picked that up, what would have followed is:', 'That would give you more marbles in your home than what you had got..'],['Well when you picked ',' what happened was this:  ','. And that gave you a profit of ',' marbles, if I am not mistaken. Now let’s suppose you picked ',' then what would have happened is this: ', ' That might have just been better, right?'],['Remember this move you made?', 'So here is what happened: ', 'and in went your earnings of ', ' marbles right! Now how about if you had picked ', 'and then you get more marbles you see!', 'That move you made was good. This was a wee bit smarter. Lets play like that huh!']]


print("\nWELCOME TO THE MANCALA USER INTERFACE.\n\n")



flag1 = 0

feedback = []
state = []
l1 = getattr(m,'combo')
l2 = getattr(m,'combo')


while True:


    print("\nLOGIN: \n")
    entry = x.accept()
    if entry==0:
        print("\nIncorrect credentials,.. resetting login:\n")
        continue
    else:
        print("\nRULES:\n1. On your turn, you can choose one of your cups that are filled and take the marbles out. Then you will distribute the marbles consecutively in every cup counter-clockwise, except the opponent home cup.\n2. When your last marble lands in a cup, if it has something in it, you will pick all the marbles in that cup plus the one you are holding and continue the distribution the same way.\n3. If your last marble lands in your home, you get another chance.\n4. If your last marble lands in an empty cup, you get that marble plus the opposite cups contents shifted to your home. If the opposite cup is empty, you leave your last marble in the empty cup you landed in and you get nothing. Your turn ends.\n5. The opponent follows similar rules. Think carefully before you choose the cup. The player to cross 24 marbles in their home cup wins the game. \n")
        print("\nThe game has begun. Good luck!\n\n")
        m.show()
        break


print("\n")
        
while True:

    m.iprepare1()
    b=m.buffer()
    p=m.decision()
    k=m.getcup()
    if p!=(k-1) and flag1==0:
        feedback = []
        flag1 = 1
        state = m.savestate()

        feedback.append(k)
        l1 = getattr(m,'combo')
        i = l1[6]
        
    

    try:

        y=m.play(k-1,1)
        if y==2:
            print("\nEmpty cup!")
            continue
 
        l2 = getattr(m,'combo')
        f = l2[6]
        actprof = f-i
        print(actprof)
        feedback.append(actprof)
        feedback.append(p+1)
        
    except:
        y=1
        tot = 0
        for i in range(5):
            tot=tot+m.combo[i]
        m.combo[6]+=tot
    
    while(y==0):
        m.iprepare1()
        k=int(input("\n\nPlayer 1! Enter a position: "))
        
        try:
 
            y=m.play(k-1,1)
            if y==2:
                print("\nEmpty cup!")
                continue
 
        except:
            tot = 0
            for i in m.combo:
                tot=tot+i
            m.combo[6]+=tot
            
        
        if m.check()==1:
            print("\nPlayer 1 WON!!")
            flag2 = 0
            break
    if m.check()==1:
        print("\nPlayer 1 WON!!")
        flag2 = 0
        break

    m.youprepare1()
    
    dec = m.decision()
    print("\nPlayer 2 chose ",dec+1)
    
    
    #k=int(input("\n\nPlayer 2! Enter a position: "))
    
    try:
        y=m.play(dec,2)
        if y==2:
            print("\nEmpty cup!")
            continue
    except:
        y=1
        tot = 0
        for i in m.combo:
            tot=tot+i
        m.combo[6]+=tot
    
    while(y==0):
        m.youprepare1()
        dec = m.decision
        print("\nPlayer 2 chose ",dec+1)
        #k=int(input("\n\nPlayer 2! Enter a position: "))
        try:
            y=m.play(dec,2)
            if y==2:
                print("\nEmpty cup!")
                continue
        except:
            tot = 0
            for i in m.combo:
                tot=tot+i
            m.combo[6]+=tot
            
        if m.check()==0:
            print("\nPlayer 2 WON!!")
            flag2 = 1
            break
    if m.check()==0:
        print("\nPlayer 2 WON!!")
        flag2 = 1
        break


l3 =[]  
if flag1==1:


    l = len(teach)
    c1 = random.randrange(0,l)
    print(c1)
    cup1 = feedback[0]
    print("\n",teach[c1][0],cup1,teach[c1][1],":\n")
    setattr(m,'combo',state)
    print("Initial game state:\n")
    m.iprepare2()
    print("\nFinal game state:\n")
    m.play(cup1-1,1)
    cup2 = feedback[2]
    print("\n",teach[c1][2],feedback[1],teach[c1][3],cup2,teach[c1][4],":\n")
    setattr(m,'combo',state)
    i = state[6]
    print("Initial game state:\n")
    m.iprepare2()
    print("\nFinal game state:\n")
    m.play(cup2-1,1)
    l3 = getattr(m,'combo')
    j = l3[6]
    print("\nPredicted profit: ",j-i,"\n")
    print(teach[c1][5])

 
    

    
    



    


