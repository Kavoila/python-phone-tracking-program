#Working with files in python.
# writing, appending and copying files.
text= "have a nice day"
with open('test.txt', 'a') as file:
 file.write(text)
import shutil
shutil.copyfile('test.txt', 'copy.text') #src.txt, dst.txt.
# moving files
import os
 Source : str = "test.txt"
 Destination = "C:\\Users\\ADN\\Desktop\\test.txt"
 try:
  if os.path.exists(Destination):
   print(" the file already exists")
  else
   os.replace ( Source, Destination)
      print( Source+" was moved")
except FileNotFoundError:
print(Source+" was not found" )




