#!/usr/bin/python
# coding=utf-8
#///.coded by cabdulahi sharif
import time
import os,sys
from fbspam import c
from fbspam import s
from fbspam import f

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

green = '\033[32;1m'

gta = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
  #//Colors 
white = '\033[1;37m' # White 
prred = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan
green = ("\033[92m")
pryellow = ("\033[93m")
prlight=("\033[94m")
prCyan=("\033[96m")
prgray = ("\033[97m")
prBlack=("\033[98m")



class fbspam:
  def __init__(self):
      self.cade=(pryellow+'[💡]saif waleed)=>:  ')
      print pryellow+"""

  ██████  ▄▄▄       ██▓  █████▒
▒██    ▒ ▒████▄    ▓██▒▓██   ▒ 
░ ▓██▄   ▒██  ▀█▄  ▒██▒▒████ ░ 
  ▒   ██▒░██▄▄▄▄██ ░██░░▓█▒  ░ 
▒██████▒▒ ▓█   ▓██▒░██░░▒█░    
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░▓   ▒ ░    
░ ░▒  ░ ░  ▒   ▒▒ ░ ▒ ░ ░      
░  ░  ░    ░   ▒    ▒ ░ ░ ░    
      ░        ░  ░ ░          
                              
          [Facebook Multi Chat Tool  2020]\n"""+C+p+"""      Youtube Channel: x-Rahba-_iq
       facebook : saif waleed
       github: https://github.com/Cabdulahi
       developer: saif waleed
       """
      print '-'*43
      time.sleep(1)
      return self.choose()
      
      
      
  def choose(self):
      print (p+'         ({1})'+pryellow+' Custom Messager')
      print (p+'         ({2}) '+pryellow+'Spammer Message')
      print (p+'         ({3}) '+pryellow+'Custom List Messager')
      print (p+'         ({4}) '+pryellow+'GROUP CHAT SPAMMER')
      print (p+'         ({0}) '+pryellow+'Exit')
      time.sleep(1)
      print
      return self.mee()
      
      
      
  def mee(self):
      inn =raw_input(self.cade+'')
      if (inn=='1' ):
          print
          c.shit2()
      elif (inn=='2'):
          print
          s.shit()
      elif (inn=='3'):
          print
          f.shit3()
      elif (inn=='4'):
          self.buy()
      elif (inn=='0'):
          time.sleep(1)
          exit()
      else:
          return self.mee()
      
     
      
  def buy(self):
      print
      print ('[🔗]Paid .this option is locked')
      
 





       
       
       

       
if __name__ == "__main__":
	fbspam()