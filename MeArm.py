from Tkinter import * #allows us to make a GUI with TKinter
import os

root = Tk()
SNums = [0,1,2,3] #Numbers of the Servos we’ll be using in ServoBlaster
SName = ["Waist","Left","Right","Claw"] #Names of Servos
AInis = [90,152,90,60] #Initial angle for Servos 0-3
AMins = [0,60,40,60] #Minimum angles for Servos 0-3
AMaxs = [180,165,180,180] #Maximum angles for Servos 0-3
ACurs = AInis #Current angles being set as the intial angles
Step = 5
for i in range(4):
  print(SNums[i],AInis[i],AMins[i],AMaxs[i],ACurs[i])

os.system('sudo /home/pi/PiBits/ServoBlaster/user/servod –idle-timeout=2000') #This line is sent to command line to start the servo controller

#inc listens for all key presses. On certain presses in the if statements below it either calls a process to add or subtract from the current servo angle.
def inc(event):
  print ("pressed", repr(event.char))
  if repr(event.char) == "'a'":
    AAdd(0)
  if repr(event.char) == "'d'":
    ASub(0)

  if repr(event.char) == "'w'":
    AAdd(1)
  if repr(event.char) == "'s'":
    ASub(1)

  if repr(event.char) == "'j'":
    AAdd(2)
  if repr(event.char) == "'l'":
    ASub(2)

  if repr(event.char) == “‘i’”:
    AAdd(3)
  if repr(event.char) == "'k'":
    ASub(3)

def callback(event):
  frame.focus_set()

def AAdd(Servo):
  if ACurs[Servo] < AMaxs[Servo]:
    ACurs[Servo] = ACurs[Servo]+Step
    # micro = (1000 + (ACurs[Servo] * 5.555))
    micro = (1000 + (ACurs[Servo] * 8.3333))
    print(ACurs[Servo],micro)
    os.system("echo %d=%dus > /dev/servoblaster" % (SNums[Servo],micro))
  else:
    print ("Max Angle Reached",SName[Servo],"Servo")

def ASub(Servo):
  if ACurs[Servo] > AMins[Servo]:
    ACurs[Servo] = ACurs[Servo]-Step
    # micro = (1000 + (ACurs[Servo] * 5.555))
    micro = (1000 + (ACurs[Servo] * 8.3333))
    print(ACurs[Servo],micro)
    os.system("echo %d=%dus > /dev/servoblaster" % (SNums[Servo],micro))

  else:
  print ("Min Angle Reached",SName[Servo],"Servo")

frame = Frame(root, width=500, height=300)
boxtext = Label(root, text="Click this box for keyboard command of the MeArm. Use the a d s w j l i and k keys for control.")
boxtext.pack()
frame.bind("<Key>",inc)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
