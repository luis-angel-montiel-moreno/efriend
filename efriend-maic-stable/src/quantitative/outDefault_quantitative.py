

file_name2= "tmp/Adial_cuantitative.int"
iden2 =open(file_name2,"w")


Adial3=["q10", "x3", "a71", "e21"]

for i in range(0, len(Adial3)):
 iden2.writelines(Adial3[i])
 iden2.writelines(",")

iden2.close
print (Adial3)
