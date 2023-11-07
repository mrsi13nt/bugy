import time,sys,os
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.09)

def clear():
  os.system("clear")