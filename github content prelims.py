
import random

class Mancala:


    def __init__(self):

        self.me=[]
        self.you=[]
        self.combo=[]
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
                print(arrt)

                if x>maxi:

                    maxi=x
                    pos=j

        return pos

                
    def getcup(self):
        
        cup = int(input("\nEnter cup number please: "))
        return cup


    def match(self):

        m = self.decision()
        return m

    def buffer(self):

        buff = self.combo[:]
        return buff
                


    def play(self,k,p):

        if k!=6 and (self.combo[k]!=1 or self.flag==0):

            self.flag=1

            temp = self.combo[k]
            self.combo[k]=0

            for i in range(temp):

                k+=1
                k%=13
                self.combo[k]+=1
            
            return self.play(k,p)

        elif k==6:
            
            if p==1:
                self.iprepare2()
            elif p==2:
                self.youprepare2()
            return 0

        else: 

            if self.combo[12-k]!=0:

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


print("\nRULES:\n1. On your turn, you can choose one of your cups that are filled and take the marbles out. Then you will distribute the marbles consecutively in every cup counter-clockwise, except the opponent home cup.\n2. When your last marble lands in a cup, if it has something in it, you will pick all the marbles in that cup plus the one you are holding and continue the distribution the same way.\n3. If your last marble lands in your home, you get another chance.\n4. If your last marble lands in an empty cup, you get that marble plus the opposite cups contents shifted to your home. If the opposite cup is empty, you leave your last marble in the empty cup you landed in and you get nothing. Your turn ends.\n5. The opponent follows similar rules. Think carefully before you choose the cup. The player to cross 24 marbles in their home cup wins the game. \n")
print("\nThe game has begun. Good luck!\n\n")
m.show()

        
while True:

    m.iprepare1()
    k=m.getcup()

    try:
        y=m.play(k-1,1)
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
        except:
            tot = 0
            for i in m.combo:
                tot=tot+i
            m.combo[6]+=tot
            
        
        if m.check()==1:
            print("\nPlayer 1 WON!!")
            break
    if m.check()==1:
        print("\nPlayer 1 WON!!")
        break

    m.youprepare1()
    
    dec = m.decision()
    print("\nPlayer 2 chose ",dec+1)
    
    
    #k=int(input("\n\nPlayer 2! Enter a position: "))
    
    try:
        y=m.play(dec,2)
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
        except:
            tot = 0
            for i in m.combo:
                tot=tot+i
            m.combo[6]+=tot
            
        if m.check()==0:
            print("\nPlayer 2 WON!!")
            break
    if m.check()==0:
        print("\nPlayer 2 WON!!")
        break
  

    



    



