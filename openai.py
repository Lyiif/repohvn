

import os
dir = "dogs"
for filename in sorted(os.listdir(dir),key=len):
  print(filename)
  os.rename("dogs/"+filename, "dogs/"+"z"+input().upper()+filename)
print("man fuck it git.")
from PIL import Image