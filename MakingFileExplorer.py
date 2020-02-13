# inbuilt concepts related to OS on 10 feb 2020---->

import os
for file in os.listdir("C:/Users/Annie/Documents"):
    if file.endswith(".txt"):
       print(os.path.join("C:/Users/Annie/Documents",file))


       