import random
from tkinter import *
import tkinter as tk

# Created by Martin Balogh
class Board1:
    def __init__(self):       
        self.board = []
        self.movement = 0
        self.killed =[]
        self.tummaruutukuva = "Tumma.jpg"
        self.vaalearuutukuva = "Vaalea.jpg"
        self.window= Tk()
        self.window.title("Tsakkipeli")
        self.window.geometry('700x700')
        self.vuoro = "White"
        for n in range (8):
            tmp = []
            for b in range(8):
                tmp.append(0)
                boardpart= n+b
                if (boardpart%2) == 0:
                    self.tummaruutukuva = "Hahhaa tää on väärin :D"                                
                else:
                    self.vaalearuutukuva = "Vaalea.jpg"                  
            self.board.append(tmp)
            

            
    def sijoitanappula(self, nappula, uusisijainti):
        if nappula.paikka[0] >=0 and nappula.paikka[0]<8 and nappula.paikka[1]>=0\
        and nappula.paikka[1]<8:
            self.board[nappula.paikka[0]][nappula.paikka[1]] = 0
            
        if self.board[uusisijainti[0]][uusisijainti[1]] != 0:
            self.killed.append(self.board[uusisijainti[0]][uusisijainti[1]])
        
        if uusisijainti[0] >=0 and uusisijainti[0]<8 and uusisijainti[1]>=0 \
        and uusisijainti[1]<8:                
            self.board[uusisijainti[0]][uusisijainti[1]] = nappula
            nappula.paikka = uusisijainti
            
        elif nappula.paikka[0] >=0 and nappula.paikka[0]<8 and nappula.paikka[1]>=0 \
        and nappula.paikka[1]<8:
            self.board[nappula.paikka[0]][nappula.paikka[1]] = nappula
            
    def PrintBoard(self):
        self.movement
        tulos = "  0,  1,  2,  3,  4,  5,  6,  7"
        indeksi = 0
        for rivinumero, rivi in enumerate(self.board):
            tulos += "\n"+str(indeksi)+"["
            eka = True
            for sarakenumero, nappula in enumerate(rivi):
                if eka:
                    eka = False
                else:
                    tulos += ", "
                
                if nappula == 0:
                    if((rivinumero + sarakenumero) % 2 == 0):
                        tulos += "██"
                    else:
                        tulos += "░░"
                else:
                    tulos += nappula.vari[0:1] + nappula.tyyppi[0:1]
            tulos += "]"
            indeksi += 1
            
        print ("Kierros: " + str(munboardi1.movement))    
        print(tulos)
        print(" ")
        
        
    def etsivari(self, vari):
        tulos=[]
        for rivi in self.board:
            for nappula in rivi:
                if nappula != 0 and nappula.vari == vari:
                    tulos.append(nappula)
        return tulos
        

munboardi1= Board1()


class Figure:
    def __init__(self,peliruudukko):
        self.liikku="none"
        self.paikka = [-1,-1]
        self.liikkeet=["liikusuora", "liikuvino","liikukuningas","liikuheppa",]
        self.tyyppi="ei mitaan"
        self.vari= "none"
        self.boardi = peliruudukko
#         self.boardi.sijoitanappula(self)
        self.kuva = "kuva.jpg"
        
    def liikkuminen(self, sijainti):
        self.boardi.sijoitanappula(self, sijainti)
        if self.tyyppi == "Sotilas" and (self.paikka[0]==7 or self.paikka[0]==0):
            possiblepromotions = ["Quningatar", "Torni", "Lahetti", "Heppa"]
            while True : 
                print("0: Kuningatar\n1: Torni\n2: Lähetti\n3: Heppa")
                try:
                    vastaus= possiblepromotions[int(input("Valitse uusi tyyppi: "))]
                    self.tyyppi=vastaus
                    break
                except:
                    pass
                
            
        
    def liikmah(self):
        movement=[]
            
        if self.tyyppi == "Kuningas":
            self.liikkeet=["liikukuningas"]
            
        if self.tyyppi == "Heppa":
            self.liikkeet =["liikuheppa"]
        
        if self.tyyppi == "Torni":
            self.liikkeet=["liikusuora"]
            
        if self.tyyppi == "Lahetti":
            self.liikkeet=["liikuvino"]
            
        if self.tyyppi == "Quningatar":
            self.liikkeet = ["liikuvino","liikusuora"]
            
        if self.tyyppi == "Sotilas":
            self.liikkeet = ["liikusotilas"]
        
        if "liikusotilas" in self.liikkeet:
            y = 0
            if self.vari == "Black":
                y = -1
            else:
                y = 1

            for x in range(-1, 2):
                    checkpos = [self.paikka[0] + y, self.paikka[1] + x]
                    if checkpos[0] >=0 and checkpos[0]<8\
                       and checkpos[1]>=0 and checkpos[1]<8\
                       and ((self.boardi.board[checkpos[0]][checkpos[1]] != 0 and x != 0)\
                            or (self.boardi.board[checkpos[0]][checkpos[1]] == 0 and x == 0)): 
                        movement.append(checkpos)
            
            if (self.vari == "Black" and self.paikka [0]== 6) or (self.vari == "White" and self.paikka[0]==1):
                if self.vari == "Black":
                    y = -2
                else:
                    y = 2
                
                checkpos = [self.paikka[0] + y, self.paikka[1]]
                if (self.boardi.board[checkpos[0]][checkpos[1]] == 0): 
                    movement.append(checkpos)
                        
        
        if "liikusuora" in self.liikkeet:
            for y in range (-1,2):
                for x in range (-1,2):
                    checkpos = [self.paikka[0] + y, self.paikka[1] + x]
                    while abs(x) != abs(y):
                        if self.paikka != checkpos and checkpos[0] >=0 \
                           and checkpos[0]<8 and checkpos[1]>=0 and checkpos[1]<8:
                            movement.append(checkpos)
                            if self.boardi.board[checkpos[0]][checkpos[1]] != 0:
                                break
                            else:
                                checkpos = [checkpos[0] + y, checkpos[1] + x]
                        else:
                            break
                        
        if "liikuvino" in self.liikkeet:
            for y in range (-1,2):
                for x in range (-1,2):
                    checkpos = [self.paikka[0] + y, self.paikka[1] + x]
                    while abs(x) == abs(y) and x != 0:
                        if self.paikka != checkpos and checkpos[0] >=0 \
                           and checkpos[0]<8 and checkpos[1]>=0 and checkpos[1]<8:
                            movement.append(checkpos)
                            if self.boardi.board[checkpos[0]][checkpos[1]] != 0:
                                break
                            else:
                                checkpos = [checkpos[0] + y, checkpos[1] + x]
                        else:
                            break
            
        
        if "liikukuningas" in self.liikkeet:
            for y in range (-1,2):
                for x in range (-1,2):
                    checkpos = [self.paikka[0] + y, self.paikka[1] + x]
                    if self.paikka != checkpos and checkpos[0] >=0 \
                    and checkpos[0]<8 and checkpos[1]>=0 and checkpos[1]<8:
                        movement.append(checkpos)
                        
        if "liikuheppa" in self.liikkeet:
            for y in range (-2,3):
                for x in range (-2,3):
                    checkpos = [self.paikka[0] + y, self.paikka[1] + x]
                    if y != 0 and x != 0\
                       and abs(y) != abs(x)\
                       and checkpos[0] >=0 and checkpos[0]<8\
                       and checkpos[1]>=0 and checkpos[1]<8:
                        movement.append(checkpos)
                        
        index = 0
        while index < len(movement):
            if self.boardi.board[movement[index][0]][movement[index][1]] != 0 and self.boardi.board[movement[index][0]][movement[index][1]].vari == self.vari:
                movement.pop(index)
            else:
                index += 1
        return movement
    
    


#valkoiset
kuningas1=Figure(munboardi1)
kuningas1.tyyppi="Kuningas"
kuningas1.vari="White"
kuningas1.boardi.sijoitanappula(kuningas1, [0,4])

kuningatar1=Figure(munboardi1)
kuningatar1.tyyppi="Quningatar"
kuningatar1.vari="White"
kuningatar1.boardi.sijoitanappula(kuningatar1, [0,3])

Heppa1 = Figure(munboardi1)
Heppa1.tyyppi="Heppa"
Heppa1.vari="White"
Heppa1.boardi.sijoitanappula(Heppa1, [0,2])

Heppa2 = Figure(munboardi1)
Heppa2.tyyppi="Heppa"
Heppa2.vari="White"
Heppa2.boardi.sijoitanappula(Heppa2, [0,5])

Lahetti1 = Figure(munboardi1)
Lahetti1.tyyppi="Lahetti"
Lahetti1.vari="White"
Lahetti1.boardi.sijoitanappula(Lahetti1, [0,1])

Lahetti2 = Figure(munboardi1)
Lahetti2.tyyppi="Lahetti"
Lahetti2.vari="White"
Lahetti2.boardi.sijoitanappula(Lahetti2, [0,6])

Torni1 = Figure(munboardi1)
Torni1.tyyppi="Torni"
Torni1.vari="White"
Torni1.boardi.sijoitanappula(Torni1, [0,0])

Torni2 = Figure(munboardi1)
Torni2.tyyppi="Torni"
Torni2.vari="White"
Torni2.boardi.sijoitanappula(Torni2, [0,7])

Sotilas1V = Figure(munboardi1)
Sotilas1V.tyyppi="Sotilas"
Sotilas1V.vari="White"
Sotilas1V.boardi.sijoitanappula(Sotilas1V, [1,0])


Sotilas2V = Figure(munboardi1)
Sotilas2V.tyyppi="Sotilas"
Sotilas2V.vari="White"
Sotilas2V.boardi.sijoitanappula(Sotilas2V, [1,1])

Sotilas3V = Figure(munboardi1)
Sotilas3V.tyyppi="Sotilas"
Sotilas3V.vari="White"
Sotilas3V.boardi.sijoitanappula(Sotilas3V, [1,2])


Sotilas4V = Figure(munboardi1)
Sotilas4V.tyyppi="Sotilas"
Sotilas4V.vari="White"
Sotilas4V.boardi.sijoitanappula(Sotilas4V, [1,3])

Sotilas5V = Figure(munboardi1)
Sotilas5V.tyyppi="Sotilas"
Sotilas5V.vari="White"
Sotilas5V.boardi.sijoitanappula(Sotilas5V, [1,4])


Sotilas6V = Figure(munboardi1)
Sotilas6V.tyyppi="Sotilas"
Sotilas6V.vari="White"
Sotilas6V.boardi.sijoitanappula(Sotilas6V, [1,5])

Sotilas7V = Figure(munboardi1)
Sotilas7V.tyyppi="Sotilas"
Sotilas7V.vari="White"
Sotilas7V.boardi.sijoitanappula(Sotilas7V, [1,6])


Sotilas8V = Figure(munboardi1)
Sotilas8V.tyyppi="Sotilas"
Sotilas8V.vari="White"
Sotilas8V.boardi.sijoitanappula(Sotilas8V, [1,7])

# mustat
kuningas2=Figure(munboardi1)
kuningas2.tyyppi="Kuningas"
kuningas2.vari="Black"
kuningas2.boardi.sijoitanappula(kuningas2, [7,3])

kuningatar2=Figure(munboardi1)
kuningatar2.tyyppi="Quningatar"
kuningatar2.vari="Black"
kuningatar2.boardi.sijoitanappula(kuningatar2, [7,4])

Heppa3 = Figure(munboardi1)
Heppa3.tyyppi="Heppa"
Heppa3.vari="Black"
Heppa3.boardi.sijoitanappula(Heppa3, [7,2])

Heppa4 = Figure(munboardi1)
Heppa4.tyyppi="Heppa"
Heppa4.vari="Black"
Heppa4.boardi.sijoitanappula(Heppa4, [7,5])

Lahetti3 = Figure(munboardi1)
Lahetti3.tyyppi="Lahetti"
Lahetti3.vari="Black"
Lahetti3.boardi.sijoitanappula(Lahetti3, [7,1])

Lahetti4 = Figure(munboardi1)
Lahetti4.tyyppi="Lahetti"
Lahetti4.vari="Black"
Lahetti4.boardi.sijoitanappula(Lahetti4, [7,6])

Torni3 = Figure(munboardi1)
Torni3.tyyppi="Torni"
Torni3.vari="Black"
Torni3.boardi.sijoitanappula(Torni3, [7,0])

Torni4 = Figure(munboardi1)
Torni4.tyyppi="Torni"
Torni4.vari="Black"
Torni4.boardi.sijoitanappula(Torni4, [7,7])

Sotilas1B = Figure(munboardi1)
Sotilas1B.tyyppi="Sotilas"
Sotilas1B.vari="Black"
Sotilas1B.boardi.sijoitanappula(Sotilas1B, [6,0])


Sotilas2B = Figure(munboardi1)
Sotilas2B.tyyppi="Sotilas"
Sotilas2B.vari="Black"
Sotilas2B.boardi.sijoitanappula(Sotilas2B, [6,1])

Sotilas3B = Figure(munboardi1)
Sotilas3B.tyyppi="Sotilas"
Sotilas3B.vari="Black"
Sotilas3B.boardi.sijoitanappula(Sotilas3B, [6,2])


Sotilas4B = Figure(munboardi1)
Sotilas4B.tyyppi="Sotilas"
Sotilas4B.vari="Black"
Sotilas4B.boardi.sijoitanappula(Sotilas4B, [6,3])

Sotilas5B = Figure(munboardi1)
Sotilas5B.tyyppi="Sotilas"
Sotilas5B.vari="Black"
Sotilas5B.boardi.sijoitanappula(Sotilas5B, [6,4])


Sotilas6B = Figure(munboardi1)
Sotilas6B.tyyppi="Sotilas"
Sotilas6B.vari="Black"
Sotilas6B.boardi.sijoitanappula(Sotilas6B, [6,5])

Sotilas7B = Figure(munboardi1)
Sotilas7B.tyyppi="Sotilas"
Sotilas7B.vari="Black"
Sotilas7B.boardi.sijoitanappula(Sotilas7B, [6,6])


Sotilas8B = Figure(munboardi1)
Sotilas8B.tyyppi="Sotilas"
Sotilas8B.vari="Black"
Sotilas8B.boardi.sijoitanappula(Sotilas8B, [6,7])

# Sotilas1M = Figure(munboardi1)
# Sotilas1M.tyyppi="Sotilas"
# Sotilas1M.vari="Black"
# Sotilas1M.boardi.sijoitanappula(Sotilas1M, [7,2])

munboardi1.PrintBoard()

vuoro = "White"
def paivitys():
    global vuoro
    if(kuningas1.boardi.board[kuningas1.paikka[0]][kuningas1.paikka[1]] == kuningas1\
      and kuningas2.boardi.board[kuningas2.paikka[0]][kuningas2.paikka[1]] == kuningas2):
        if vuoro == "White":
            print("Valkoinen vuoro!!!!")
            munboardi1.movement += 1
            #kuningas1.liikkuminen(kuningas1.liikmah()[int(input("Valitse sijainti: " + str(kuningas1.liikmah())))])
            Nappula = 0
            while(Nappula == 0 or Nappula.vari != "White"):
                        inputti = input("Valitse nappula muodossa 'y,x': ")
                        try:
                            inputti = inputti.split(",")
                            Nappula = munboardi1.board[int(inputti[0])][int(inputti[1])]
                        except:
                            pass
            indeksi = 0
            for (mah) in Nappula.liikmah():
                suunta = ""
            #if mah[0] < kuningas1.paikka[0]:
            #    suunta += "Ylä"
            #elif mah[0] > kuningas1.paikka[0]:
            #    suunta += "Ala"
            #if mah[1] < kuningas1.paikka[1]:
            #    suunta += "Vasen"
            #elif mah[1] > kuningas1.paikka[1]:
            #    suunta += "Oikea"
            
            #print(str(indeksi) +": "+ suunta)
                print(str(indeksi) +": "+ str(mah))
                indeksi+=1

            inputtikelvollinen = False;
            while(inputtikelvollinen == False):
                    inputti = input("Valitse sijainti: ")
                    try:
                        Nappula.liikmah()[int(inputti)]
                        inputti = int(inputti)
                        inputtikelvollinen = True
                    except:
                        pass
            Nappula.liikkuminen(Nappula.liikmah()[inputti])

            vuoro = "Black"
        elif vuoro == "Black":
            print("Musta vuoro!!!!")
            Nappula = 0
            while(Nappula == 0 or Nappula.vari != "Black"):
                        inputti = input("Valitse nappula muodossa 'y,x': ")
                        try:
                            inputti = inputti.split(",")
                            Nappula = munboardi1.board[int(inputti[0])][int(inputti[1])]
                        except:
                            pass
            indeksi = 0
            for (mah) in Nappula.liikmah():
                suunta = ""
            
            #print(str(indeksi) +": "+ suunta)
                print(str(indeksi) +": "+ str(mah))
                indeksi+=1

            inputtikelvollinen = False
            while(inputtikelvollinen == False):
                    inputti = input("Valitse sijainti: ")
                    try:
                        Nappula.liikmah()[int(inputti)]
                        inputti = int(inputti)
                        inputtikelvollinen = True
                    except:
                        pass
            Nappula.liikkuminen(Nappula.liikmah()[inputti])
            vuoro = "White"

        
        print("Killed: ")
        for kuollut in munboardi1.killed:
            print(kuollut.vari + " " + kuollut.tyyppi + ",\n")
        print()
        munboardi1.PrintBoard()
        
while True:
#korvaa mainluupin
    #munboardi1.window.mainloop()
    #munboardi1.window.update_idletasks()
    #munboardi1.window.update()
    paivitys()
    
    
    



    


    


