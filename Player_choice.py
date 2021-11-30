#########Game Setup#########
#Author: 

import start
class Input():
  def get_inputs():
      Waitfor("input from story graph")
      Action("ShowList( Nodes from story graph Farm.Library)")

import start	  
class enableicon():
   def enable_icon():	  
     Action("EnableIcon(Farm,Tom,' + ',Library,Tom)")\
     input = Action("Player input selected")
	 return input

import start	   
clas disableIcon():
  def disabe_icon(input): 
     Action("DisableIcon(input)")
	  

import start
class Startaction():
   def start_action():	  
     Wainfor("input from story graph")
     Action("ShowList( Nodes from story graph Farm.Library)")
     Action("EnableIcon(Hammer,Tom,' + ',BlueBook,Tom)")
     Action("Player input selected")
	 
	 
	 
	 
	 
from Input import get_inputs
from enableicon import enable_icon
from disableIcon import disabe_icon
from Startaction import start_action 

def check_for_success(command):
    while True:
        received = input()
        if received == 'succeeded ' + command:
            return True
        elif received.startswith('failed ' + command):
            return False
        
def Action(command):
   print('start ' + command)
   return check_for_success(command)
   
obj = Input()
obj.get_inputs()

en = enableicon()
output = en.enable_icon() 

if output == " go fo"
  di = disableIcon()
  di.disabe_icon(outpt)
else:
  sa = Startaction()
  sa.start_action()
