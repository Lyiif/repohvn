<<<<<<< HEAD
from PIL import Image


import os
dir = "dogs"
for filename in sorted(os.listdir(dir),key=len):
  print(filename)
  os.rename("dogs/"+filename, "dogs/"+"z"+input().upper()+filename)
print("man fuck it git.")
=======
from PIL import Image


import os
dir = "dogs"
for filename in sorted(os.listdir(dir),key=len):
  print(filename)
  os.rename("dogs/"+filename, "dogs/"+"z"+input().upper()+filename)
print("git?")
>>>>>>> ac8690a81c06236a553d19196bac7bba41159a19
