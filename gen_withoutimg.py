import random

DOB = input("input: ").upper()
d,m,y = DOB.split("-")
no = "S"
no += y[2:4]
temp=str(random.randint(0,99999))
no+=temp.zfill(5)
temp=no[1:]
checksum=(int(temp[0])*2+int(temp[1])*7+int(temp[2])*6+int(temp[3])*5+int(temp[4])*4+int(temp[5])*3+int(temp[6])*2)%11
if checksum==0:
  no+="J"
elif checksum==1:
  no+="Z"
elif checksum==2:
  no+="I"
elif checksum==3:
  no+="H"
elif checksum==4:
  no+="G"
elif checksum==5:
  no+="F"
elif checksum==6:
  no+="E"
elif checksum==7:
  no+="D"
elif checksum==8:
  no+="C"
elif checksum==9:
  no+="B"
else:
  no+="A"
print(no)



