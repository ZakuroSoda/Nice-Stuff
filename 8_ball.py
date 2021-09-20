#########################################################

import random
import time
import pyperclip

listanswers = ["It is certain","It is decidedly so","Without a doubt","Yes, definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]

value = str(input("Ask the MAGICK 8-Ball your burning question here: "))

shakey = input("Shake the 8-Ball by typing in 'SHAKEY SHAKEY' here: ")

def main():
    if shakey == "SHAKEY SHAKEY":
        print("8-Ball is deciding...")
        time.sleep(3)
        a = listanswers[random.randint(0,19)]
        print(a + ".")
        time.sleep(1)
    else:
        print("GAY SHIT SHAKE THE BALL OR ELSE")
    
    copy = input("Copy your results to clipboard? (y/n): ")
    
    if copy == "y":
        pyperclip.copy("Question: '" + value + "'\n" + "Answer: '" +  a + "'.")
    
main()

time.sleep(3)

########################################################