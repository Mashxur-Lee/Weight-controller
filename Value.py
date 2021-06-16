import pyttsx3
from colorama import init
from colorama import Fore, Back, Style
init()

while True:
       print( Back.CYAN )
       print( Fore.RED )

       engine = pyttsx3.init()
       engine.say("Are you a man or woman?")
       engine.runAndWait()

       person = input("Are you a man or woman? ")

       engine = pyttsx3.init()
       engine.say("Your height:")
       engine.runAndWait()

       height = int( input("Your height: "))
                        
       print( Back.GREEN )
       print( Fore.BLACK )
     
       if person ==  "woman" : 
              if height >= 150:
                 fr = height * 0.24
                 to = height * 0.27
              if height >= 160:
                 fr = height * 0.30
                 to = height * 0.33
              if height >= 170:
                 fr = height * 0.37
                 to = height * 0.40
              if height >= 180:
                 fr = height * 0.40
                 to = height * 0.43       
       if person ==  "man" :
              if height >= 150:
                 fr = height * 0.27
                 to = height * 0.30
              if height >= 160:
                 fr = height * 0.33
                 to = height * 0.37
              if height >= 170:
                 fr = height * 0.40
                 to = height * 0.43
              if height >= 180:
                 fr = height * 0.43
                 to = height * 0.47
       engine = pyttsx3.init()
       engine.say("Result:")
       engine.runAndWait()

       print("Your height has to be from" , fr ,  " to " , to, "kilograms")

       engine = pyttsx3.init() 
       engine.say("Your weight matches these numbers?")
       engine.runAndWait()

       LOL = input(str("Your weight matches these numbers?(yes or no)"))

       if LOL == "yes" :
           engine = pyttsx3.init()
           engine.say("You are perfect!")
           engine.runAndWait()
           print("You are perfect!")
           again = input("again?(yes or no)")
           if again == "yes":
               continue
           else:
              break
              input()
              quit()
           
       if LOL == "no" :
           engine = pyttsx3.init()
           engine.say("Your weight?")
           engine.runAndWait()

       weight = float( input("Your weight?"))
       if weight < fr:
           engine = pyttsx3.init()
           engine.say("Then, you have to eat more and sleep more!")
           engine.runAndWait()
           print("Then, you have to eat more and sleep more!")
       if weight  > to:
           engine = pyttsx3.init()
           engine.say("Then, you have to eat less and work harder!")
           engine.runAndWait()
           print("Then, you have to eat less and work harder!")
       engine = pyttsx3.init()
       engine.say("Again or more?")
       engine.runAndWait()
       again = input("again? (yes or no)")
       if again == "no":
              break
              input()
              quit()

