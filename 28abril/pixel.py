from urllib2 import urlopen

url="http://lorempixel.com/400/200"
resultado=urlopen(url)
lectura=resultado.read()
f=open("holder.jpg","wp")
f.write(lecture)
f.close()





