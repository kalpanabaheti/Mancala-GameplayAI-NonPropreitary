
'''
This is the file-handling system. It has the functions:
1. Adding members (AddPlayer.csv)
2. Saving game states (GameState.csv)
3. Saving move sequences (CurrentGame.csv)
4. Storing repository of initial comments (Part1.csv)
5. Storing repository of feedback fill-ins (Part2.csv)
6. Storing repository of appreciation fill-ins (Part3.csv)
'''

import os
import random
import time
from pympler import asizeof

class Login:

    def __init__(self):

        self.username = "kalpanabaheti"
        self.password = "12345"

    def accept(self):

        u = input("\nEnter username: ")
        p = input("\nEnter password: ")

        if u==self.username and p!=self.password:
            
            return 0
        
        elif u==self.username and p==self.password:
            
            return -1
        
        else:
            
            if not os.path.isfile('AddPlayer.CSV'):
                print("\nFile does not exist!")
                
            else:

                flag = 0
                
                file1 = open('AddPlayer.CSV','r')
                L = file1.readlines()
                file1.close()
                
                for record in L:
                    frame = record.rstrip('\n').split(',')
                    if str(frame[1]) == str(u) and str(frame[2]) == str(p):
                        print("\nWelcome ",u,", to your Mancala Streak! :)")
                        flag = int(frame[0])
                        
                return flag
                    
                            
            

class Mancala(object):


    def __init__(self):

        self.me=[]
        self.you=[]
        self.combo=[]
        print("\nGAME: ",asizeof.asized(self.combo, detail=1).format())
        self.result=[]
        self.myhome=0
        self.yourhome=0
        self.flag=None
        self.buffer=[]
 

    def standard(self):

        self.me = []
        self.you = []

        for i in range(0,6):
            self.me.append(4)
            self.you.append(4)

    def random(self):

        self.me = []
        self.you = []

        i = 0
        count = 0

        while i<4:
            x = random.randint(0,6)
            self.me.append(x)
            count = count + x
            i+=1
            
        y = int((24-count)//2)
        self.me.append(y)
        self.me.append(y)

        i = 0
        count = 0

        while i<4:
            x = random.randint(0,6)
            self.you.append(x)
            count = count + x
            i+=1
            
        y = int((24-count)//2)
        self.you.append(y)
        self.you.append(y)


        
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
        finlist = []
        current = self.combo[6]

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

                    finlist = t
                    maxi=x
                    pos=j

        l = [pos,finlist,current,maxi]

        return l

    
                
    def getcup(self):
        
        cup = int(input("\nEnter cup number please: "))
        return cup


    def savestate1(self,c): #beforeuserplays

        self.buffer = self.decision()

        if self.buffer[0]!=c:

            t = self.combo[:]
            self.buffer.insert(1,t)
            self.buffer.insert(1,c) #you still need flag, actual profit and actual final state
            return 1
        else:
            return 0

    def savestate2(self): #afteruserplays

        t = self.combo[:]
        
        try:
            
            actualprof = self.combo[6] - self.buffer[4]
            if actualprof>self.buffer[5]:
                flag = -1
            elif actualprof<self.buffer[5]:
                flag = 1
            else:
                flag = 0
            self.buffer.append(actualprof)
            self.buffer.insert(0,flag)
            self.buffer.insert(5,t)
            print(len(self.buffer)," :should be size 9\n")
            #buffer list final = [flag,predcup,actcup,initstate,predfinstate,actfinstate,initprof,predfinprof,predactprof]

        except:

            print("\nList out of range. Please check manually what went wrong.")
        


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

            

class Files(Mancala):

    def __init__(self):

        Mancala.__init__(self)


        self.id = 0 #addplayer
        self.user = None
        self.level = "Novice"
        self.config = "fixed"
        self.password = None

        self.stateid = 0 #gamestate
        self.gamestate = []
        self.totalerror = 0
        self.actual = 0
        self.predicted = 0
        self.intent = 0
        self.decaycount = 0
        self.last = 0

        
        self.commentid1 = 0 #part1
        self.inp1 = None
        self.gamestatus = None
        self.win = None

        self.commentid2 = 0 #part2
        self.a1 = None
        self.a2 = None
        self.a3 = None
        self.a4 = None
        self.a5 = None
        self.a6 = None

        self.commentid3 = 0 #part3
        self.b1 = None
        self.b2 = None
        self.b3 = None

        self.currid = 0
        self.actualsequence = [] #currentgame
        self.predictedsequence = []
        self.profit = []
        self.flag = []
        self.flawstates = []
        self.smartstates = []
        self.winner = 1
        

    def addMember(self):

        if not os.path.isfile('AddPlayer.CSV'):
            self.id=1
            self.user = input("\nPlease set your username: ")

        else:
            file1 = open('AddPlayer.CSV','r')
            L = file1.readlines()
            self.id = 1+len(L)
            file1.close()

            while True:

                username = input("\nPlease set your username: ")
                for record in L:
                    frame = record.rstrip('\n').split(',')
                    if str(frame[1]) == str(username):
                        flag=0
                        print("\nUsername already exists, please type in another...")
                    else:
                        flag=1
                if flag==1:
                    break
                
        self.user = username
        self.password = input("\nPlease set a password: ")

        file1 = open('AddPlayer.CSV','a')
        file1.write((str(self.id))+','+self.user+','+self.password+','+self.level+','+self.config+'\n')
        file1.close()

    '''
    def updateRecord(self):

        if not os.path.isfile('GameState.CSV'):
            self.stateid=1
        else:
            file1 = open('GameState.CSV','r')
            L = file1.readlines()
            self.stateid = 1+readlines()               
            file1.close()

        self.actual = Mancala.getcup(self)
        self.predicted = Mancala.match(self)
        if self.actual==self.predicted:
            self.intent = 0
        else:
            self.intent = 1
            
        self.gamestate = Mancala.buffer(self)

        file1 = open('GameState.CSV','a')
        c = Mancala.check(self)
        if c!=999:
            self.last = L+1
        file1.write((str(self.stateid))+','+(str(self.gamestate))+','+(str(self.totalerror))+','+(str(self.actual))+','+(str(self.predicted))+','+(str(self.intent))+','+(str(self.decaycount))+','+(str(self.last))+'\n')
        file1.close()
    '''

    def firstInput(self):


        if not os.path.isfile('Part1.CSV'):
            self.commentid1=1
        else:
            file1 = open('Part1.CSV','r')
            L = file1.readlines()
            self.commentid1 = 1+len(L)
            file1.close()

        self.inp1 = input("\nEnter comment: ")
        self.gamestatus = input("\nStatus: ")
        self.win = int(input("\nClassify as 1 if narrow win, else 0: "))

            
        file1 = open('Part1.CSV','a')
        file1.write((str(self.commentid1))+','+(str(self.inp1))+','+(str(self.gamestatus))+','+(str(self.win))+'\n')
        file1.close()


    def firstOutput(self):

        k = self.winner
            
        if not os.path.isfile('Part1.CSV'):
            print("\nFile does not exist!")
        else:
            file1 = open('Part1.CSV','r')
            L = file1.readlines()
            file1.close()
            
            t = len(L)
            i = random.randint(1,t)
            result = ""
            for record in L:
                frame = record.rstrip('\n').split(',')
                if str(frame[0]) == str(i):
                    result = str(frame[1])
                    p = len(frame)
                        
            return result


    def secondInput(self):


        if not os.path.isfile('Part2.CSV'):
            self.commentid2=1
        else:
            file1 = open('Part2.CSV','r')
            L = file1.readlines()
            self.commentid2 = 1+len(L)
            file1.close()

        self.a1 = input("\nEnter bit 1: ")
        self.a2 = input("\nEnter bit 2: ")
        self.a3 = input("\nEnter bit 3: ")
        self.a4 = input("\nEnter bit 4: ")
        self.a5 = input("\nEnter bit 5: ")
        self.a6 = input("\nEnter bit 6: ")

            
        file1 = open('Part2.CSV','a')
        file1.write((str(self.commentid2))+','+self.a1+','+self.a2+','+','+self.a3+','+self.a4+','+self.a5+','+self.a6+'\n')
        file1.close()


    def secondOutput(self):

        if not os.path.isfile('Part2.CSV'):
            print("\nFile does not exist!")
        else:
            file1 = open('Part2.CSV','r')
            L = file1.readlines()
            file1.close()
            
            t = len(L)
            i = random.randint(1,t)
         
            l1 = []
            
            for record in L:
                
                frame = record.rstrip('\n').split(',')
                if str(frame[0])==str(i):
                       
                    l1.append(str(frame[1]))
                    l1.append(str(frame[2]))
                    l1.append(str(frame[3]))
                    l1.append(str(frame[4]))
                    l1.append(str(frame[5]))
                    l1.append(str(frame[6]))
                    
            return l1


    def thirdInput(self):

        if not os.path.isfile('Part3.CSV'):
            self.commentid3 = 1
        else:
            file1 = open('Part3.CSV','r')
            L = file1.readlines()
            self.commentid3 = 1+len(L)
            file1.close()

            self.b1 = input("\nEnter bit 1: ")
            self.b2 = input("\nEnter bit 2: ")
            self.b3 = input("\nEnter bit 3: ")
            
        file1 = open('Part3.CSV','a')
        file1.write((str(self.commentid3))+','+self.b1+','+self.b2+','+self.b3+'\n')
        file1.close()


    def thirdOutput(self):

        if not os.path.isfile('Part3.CSV'):
            print("\nFile does not exist!")
        else:
            file1 = open('Part3.CSV','r')
            L = file1.readlines()
            file1.close()
            
            t = len(L)
            i = random.randint(1,t)
         
            l1 = []
            
            for record in L:
                
                frame = record.rstrip('\n').split(',')
                if str(frame[0])==str(i):
                       
                    l1.append(str(frame[1]))
                    l1.append(str(frame[2]))
                    l1.append(str(frame[3]))
                    
            return l1


    def currentGameSave(self,buff):

        if not os.path.isfile('CurrentGame.CSV'):

            print("\nCreating Current Game File...")
            file1 = open('CurrentGame.CSV','a')
            file1.write((str(buff))+'\n')
            file1.close()
            
        else:
            
            file1 = open('CurrentGame.CSV','a')
            file1.write((str(buff))+'\n')
            file1.close()

    def currentGameGet(self):


        file1 = open('CurrentGame.CSV','r')
        L = file1.readlines()
        t = len(L)
        r = random.randint(1,t)
        j = 0
            
        for record in L:

            frame = record.rstrip('\n').split(',')
            flag = int(frame[0][1])

            if j!=r and flag!=1:

                continue

            else:
                
                predcup = int(frame[1])
                actcup = int(frame[2])
                
                initstate = []
                initstate.append(int(frame[3][2]))
                for i in range(4,15):
                    initstate.append(int(frame[i]))
                initstate.append(int(frame[15][1]))

                predfinstate = []
                predfinstate.append(int(frame[16][2]))
                for i in range(17,28):
                    predfinstate.append(int(frame[i]))
                predfinstate.append(int(frame[28][1]))

                actfinstate = []
                actfinstate.append(int(frame[29][2]))
                for i in range(30,41):
                    actfinstate.append(int(frame[i]))
                actfinstate.append(int(frame[41][1]))
                
                initprof = int(frame[42])
                predfinprof = int(frame[43])
                predactprof = int(frame[44][1])
                buff = [flag,predcup,actcup,initstate,predfinstate,actfinstate,initprof,predfinprof,predactprof]
                return buff
                
                break

        



class Driver(Files,Login,Mancala):
    

    def __init__(self):

        Files.__init__(self)
        Login.__init__(self)

    def logincheck(self):

        while True:

            c = int(input("\n1. SIGN UP\n2. LOGIN\n3. QUIT\nEnter 1,2 or 3: ",))
            
            if c == 1:
    
                Files.addMember(self)
                return 0

            elif c == 2:

                retval = Login.accept(self)

                if retval == 0:

                    print("\nWrong username or password, please try again.")
                    continue

                elif retval == -1:

                    print("\nWelcome to game tester and research mode.")
                    self.playgame()
                    l = [0]
                    return l

                else:

                    print("\nLet the games begins. May the best player win.")
                    l = self.setgame(retval)
                    self.playgame()
                    self.feedbackstream()
                    return l

            elif c == 3:

                print("\nCYA NEXT TIME BUDDY!!:)")

                break

            else:

                print("\nPlease enter a valid choice.")

    
    def setgame(self,r):

        file = open('CurrentGame.CSV','r+')
        file.truncate(0)
        file.close()

        file1 = open('AddPlayer.CSV','r')
        L = file1.readlines()
        file1.close()
            
        for record in L:
            frame = record.rstrip('\n').split(',')
            if str(frame[0]) == str(r):
                level = str(frame[3])
                config = str(frame[4])
        setting = [level,config]
        return setting
        
    
    def playgame(self):

        Mancala.__init__(self)
        Mancala.standard(self)
        Mancala.show(self)

        while True:

            Mancala.iprepare1(self)
            d = Mancala.decision(self)
            print(d[0])
            k = Mancala.getcup(self)
            tosave = Mancala.savestate1(self,k)

            
            try:

                y=Mancala.play(self,k-1,1)
                if y==2:
                    print("\nEmpty cup!")
                    continue
                
                if tosave == 1:
                    Mancala.savestate2(self)
                    print("\nState to be saved. Flag: ",self.buffer[0])
                    Files.currentGameSave(self,self.buffer)
                else:
                    print("\nGood work")
                
            except:
                
                y=1
                tot = 0
                for i in range(6):
                    tot=tot+self.combo[i]
                    self.combo[i]=0
                self.combo[6]+=tot
               
            
            while(y==0):
                
                Mancala.iprepare1(self)
                d = Mancala.decision(self)
                print(d[0])
                k=Mancala.getcup(self)
                tosave = Mancala.savestate1(self,k)

                
                try:
         
                    y=Mancala.play(self,k-1,1)
                    if y==2:
                        print("\nEmpty cup!")
                        continue

                    if tosave == 1:
                        Mancala.savestate2(self)
                        print("\nState to be saved. Flag: ",self.buffer[0])
                        Files.currentGameSave(self,self.buffer)
                    else:
                        print("\nGood work")
                        
         
                except:
                    
                    tot = 0
                    for i in range(6):
                        tot=tot+self.combo[i]
                        self.combo[i]=0
                    self.combo[6]+=tot
                   
                    
                
                if Mancala.check(self)==1:
                    print("\nYOU WON, YAY!")
                    break
                
            if Mancala.check(self)==1:
                print("\nYOU WON, YAY!")
                break

            Mancala.youprepare1(self)
            
            d = Mancala.decision(self)
            dec = d[0]
            print("\nI am going to go with cup number ",dec+1)
            
            try:
                y=Mancala.play(self,dec,2)
                if y==2:
                    print("\nEmpty cup!")
                    continue
            except:
                
                y=1
                tot = 0
                for i in range(6):
                    tot=tot+self.combo[i]
                    self.combo[i]=0
                self.combo[6]+=tot
            
            while(y==0):
                
                Mancala.youprepare1(self)
                d = Mancala.decision(self)
                dec = d[0]
                print("\nI am going to go with cup number ",dec+1)

                try:
                    y=Mancala.play(self,dec,2)
                    if y==2:
                        print("\nEmpty cup!")
                        continue
                except:
                    
                    tot = 0
                    for i in range(6):
                        tot=tot+self.combo[i]
                        self.combo[i]=0
                    self.combo[6]+=tot
                    
                if Mancala.check(self)==0:
                    print("\nHAHA I WONNN, Y A Y Y Y!!!")
                    break
                
            if Mancala.check(self)==0:
                print("\nHAHA I WONNN, Y A Y Y Y!!!")
                break

    '''

    def updatesystemfile(self):
    '''

    def feedbackstream(self):

        f1 = Files.firstOutput(self)

        f2 = Files.currentGameGet(self)

        f3 = Files.secondOutput(self)

        f4 = Files.thirdOutput(self)

        time.sleep(3)

        print("\n",f1)
        time.sleep(3)
        print("\nOKAY LEARNING TIME!!")
        try:
            
            time.sleep(3)
            print("\n"+f3[0]+" "+(str(f2[2]))+f3[1])
            print("\nStart State: \n")
            self.combo = f2[3]
            Mancala.iprepare2(self)
            time.sleep(3)
            print("\nEnd State: \n")
            self.combo = f2[5]
            Mancala.iprepare2(self)
            time.sleep(3)
            print("\n"+f3[2]+" "+(str(f2[8]))+f3[3]+" "+(str(f2[1]))+f3[4])
            print("\nStart State: \n")
            self.combo = f2[3]
            Mancala.iprepare2(self)
            time.sleep(3)
            print("\nEnd State: \n")
            self.combo = f2[4]
            Mancala.iprepare2(self)
            print("\nProfit: ",f2[7])
            time.sleep(3)
            print("\n"+f3[5])
            
        except:

            print("\nYou did it perfectly this time!")
            
        print("\n"+f4[0]+"\n"+f4[1]+"\n"+f4[2])
    
        
    


#Main Environment

driver = Driver()

while True:

    driver.logincheck()
    ans = input("\nStart game? (Y/N): ")
    if ans == "Y":
        print("\nRULES:\n1. On your turn, you can choose one of your cups that are filled and take the marbles out. Then you will distribute the marbles consecutively in every cup counter-clockwise, except the opponent home cup.\n2. When your last marble lands in a cup, if it has something in it, you will pick all the marbles in that cup plus the one you are holding and continue the distribution the same way.\n3. If your last marble lands in your home, you get another chance.\n4. If your last marble lands in an empty cup, you get that marble plus the opposite cups contents shifted to your home. If the opposite cup is empty, you leave your last marble in the empty cup you landed in and you get nothing. Your turn ends.\n5. The opponent follows similar rules. Think carefully before you choose the cup. The player to cross 24 marbles in their home cup wins the game. \n")
        print("\nThe game has begun. Good luck!\n\n")
        file = open('CurrentGame.CSV','r+')
        file.truncate(0)
        file.close()
        driver.playgame()
        driver.feedbackstream()
    elif ans == "N":
        break
    else:
        print("\nInvalid entry, you are logged out!")
        



       
                       
                    

            

        
                
            
            
            
        
            
            
                
            
            

        













    
        
