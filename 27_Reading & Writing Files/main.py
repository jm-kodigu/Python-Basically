f = open("juliao.txt","w")

f.write("hello, world!")
f.write("\ni'm jm-kodigu, visit my account github\n")
f.write("https://github.com/jm-kodigu\n")

f.close()

f2 = open("juliao.txt","a")

f2.write("Hello, Again!")
f2.write("\npython is programming languague")

f2.close()

f3 = open("juliao.txt","r")

# print(f3.read())
#print(f3.read(20))
print(f3.readline())

f3.close()

# write html with python

htmlfile = open("index.html","w")

htmlfile.write("<!DOCTYPE html>\n")
htmlfile.write("<html>\n")
htmlfile.write("<head>\n")
htmlfile.write("\t<title>Hello, World!</title>\n")
htmlfile.write("</head>\n")
htmlfile.write("<body>\n")
htmlfile.write("\t<h1>Hello, World!</h1>\n")
htmlfile.write("</body>\n")
htmlfile.write("</html>")

htmlfile.close()