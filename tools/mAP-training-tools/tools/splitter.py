filepath = 'left-fps3.txt'

with open(filepath) as fp:
   line = fp.readline()
   count = 0

   file = open("splits/"+str(count) + ".txt","w")

   while line:
       line = line.strip()
       if line == "":
           print(count)
           count += 1
           file = open("splits/"+str(count) + ".txt","w")
       elif len(line) >= 27:
           print(line)
           file.write(line+"\n")
       line = fp.readline()
