import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image, ImageEnhance
import random

alias = input("Input your fake name (not more than 20 chars): ").upper()
x = alias.split("\n")
alias = ""
for i in x :
  alias += i
  alias += "\n"
race = input("Input your race: ").upper()
DOB = input("Input your DOB: ").upper()
d, m, y = DOB.split("-")
Gender = input("Input your gender: ").upper()
address = input("Input your address: ")
no = "S"
no += y[2:4]
temp = str(random.randint(0,99999))
no += temp.zfill(5)
temp = no[1:]
checksum = (int(temp[0])*2+int(temp[1])*7+int(temp[2])*6+int(temp[3])*5+int(temp[4])*4+int(temp[5])*3+int(temp[6])*2)%11
if checksum == 0:
  no += "J"
elif checksum == 1:
  no += "Z"
elif checksum == 2:
  no += "I"
elif checksum == 3:
  no += "H"
elif checksum == 4:
  no += "G"
elif checksum == 5:
  no += "F"
elif checksum == 6:
  no += "E"
elif checksum == 7:
  no += "D"
elif checksum==8:
  no += "C"
elif checksum == 9:
  no += "B"
else:
  no += "A"
print(no)
x = address.split(",,")
address = ""
for i in x :
  address += i
  address += "\n"
blood = random.choice(["A","B","AB","O"])+random.choice(["+","-"])
if 1970 > int(y):
  doi = str(random.randint(1,28))+"-"+str(random.randint(1,12))+"-"+str(random.randint(1970,2001))
else:
  doi = str(random.randint(1,28))+"-"+str(random.randint(1,12))+"-"+str(random.randint(int(y)+1,2001))

#doi,blood,address,alias,race,DOB,Gender,no="11-1-1","A+","test","asdf","","","F","T1234567A"
img=cv2.imread("IC_Front.png")
img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
copied=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
copied=Image.fromarray(copied)
draw=ImageDraw.Draw(copied)
font=ImageFont.truetype("Helvetica.otf",10)
bigfont=ImageFont.truetype("Helvetica-Bold.ttf",11)
nofont=ImageFont.truetype("Helvetica-Bold.ttf",11)
draw.text((133,37.7),no,fill="#303030",font=nofont)
draw.text((125,82),alias,fill="#303030",font=bigfont)
draw.text((125.5,143),race,fill="#303030",font=font)
draw.text((125.7,165.5),DOB,fill="#303030",font=font)
draw.text((194,165.5),Gender,fill="#303030",font=font)
draw.text((125.95,189),"SINGAPORE",fill="#303030",font=font)
processed=cv2.cvtColor(np.array(copied),cv2.COLOR_RGB2BGR)
if Gender=="M":
  pic=cv2.imread("m"+str(random.randint(1,10))+".png")
elif Gender=="F":
  pic=cv2.imread("f"+str(random.randint(1,10))+".png")
else:
  pic=cv2.imread(random.choice(["m","f"])+str(random.randint(1,10))+".png")
pic=cv2.resize(pic,(100,100))
lookUpTable = np.empty((1,256), np.uint8)
bg=cv2.imread("picbackground.png")
for i in range(100):
  for j in range(100):
    xxx=sum(pic[i,j])
    pic[i,j][0]=(xxx/643)*201
    pic[i,j][1]=(xxx/643)*207
    pic[i,j][2]=(xxx/643)*235
    if pic[i,j][0]==pic[i,j][1] and pic[i,j][1]==pic[i,j][2]:
      pic[i,j]=bg[i,j]
pic=cv2.GaussianBlur(pic,(3,3),1)
processed[80:180,15:115]=pic

for i in range(256):
  lookUpTable[0,i] = np.clip(pow(i / 255.0, 0.7) * 255.0, 0, 255)
processed = cv2.convertScaleAbs(processed, alpha=0.8, beta=50)
processed = cv2.LUT(processed, lookUpTable)
processed = cv2.convertScaleAbs(processed, alpha=1, beta=-50)
#processed[78:82,15:115]=cv2.medianBlur(processed[78:82,15:115],5)
processed[178:182,15:115]=cv2.medianBlur(processed[178:182,15:115],5)
#processed[80:180,13:17]=cv2.medianBlur(processed[80:180,13:17],5)
#processed[80:180,113:117]=cv2.medianBlur(processed[80:180,113:117],5)
cv2.imshow("asdf",processed)
bg=cv2.imread("bg"+str(random.randint(1,4))+".jpg")
bg=cv2.resize(bg,(400,300))

for i in range(219):
  for j in range(338):
    if sum(processed[i,j])==93:
      processed[i,j]=bg[0:processed.shape[0],10:processed.shape[1]+10][i,j]
bg[0:processed.shape[0],10:processed.shape[1]+10]=processed
cv2.imshow("front",bg)
back=cv2.imread("IC_Back.png")
back=cv2.resize(back,(back.shape[1]//2,back.shape[0]//2))
copied=cv2.cvtColor(back,cv2.COLOR_BGR2RGB)
copied=Image.fromarray(copied)
draw=ImageDraw.Draw(copied)
draw.text((160,72),no,fill="#303030",font=font)
draw.text((127.5,154),blood,fill="#303030",font=font)
draw.text((174,154),doi,fill="#303030",font=font)
draw.text((36.5,175),address,fill="#303030",font=font)
processed=cv2.cvtColor(np.array(copied),cv2.COLOR_RGB2BGR)
for i in range(256):
  lookUpTable[0,i] = np.clip(pow(i / 255.0, 0.4) * 255.0, 0, 255)
processed = cv2.convertScaleAbs(processed, alpha=0.8, beta=0)
processed = cv2.LUT(processed, lookUpTable)
processed = cv2.convertScaleAbs(processed, alpha=1.2, beta=-70)
cv2.imshow("back",processed)
cv2.waitKey(0)
cv2.destroyAllWindows()
