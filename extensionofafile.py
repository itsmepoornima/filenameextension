
filename=input("input the filename:")
f_extns=filename.split(".")
e=f_extns[-1]
str="py"
str1="cpp"
b="c"
c="java"
d="txt"
if e==str:
    print("the extension of the file is python")
elif e==str1:
    print("the extension of the file is C++")
elif e==b:
    print("the extension of the file is C")
elif e==c:
    print("the extension  of the file is Java")
elif e==d:
    print("the extension of the file is text")
else:
    print("not found")

