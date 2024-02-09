algo = ""
ident="    "
def Fix_Iden(x):
    s=""
    for i in range (len(x)):
        if (x[i]==" "):
            s = s+" "
        else:
            return s +ident
            break
with open('algo.txt', 'r') as f:
    for line in f:
        if (line.find("pour ")!=-1):
            cnt = line.find ("pour ")
            if (line[line.find("de ")+3:line.find("a ")-1] == "0"):
                algo = algo + "for "+line[cnt+5:line.find("de ")-1]+" in range ("+line[line.find("a ")+3:line.find(") faire")]+"+1):\n" + Fix_Iden(algo.split('\n')[-2])
            else:
                algo = algo + "for "+line[cnt+5:line.find("de ")-1]+" in range ("+line[line.find("de ")+3:line.find("a ")]+","+line[line.find("a ")+3:line.find(") faire")]+"):\n"+Fix_Iden(algo.split('\n')[-1])
        elif "si" in line:
            words = line.split()
            if (words[0]=="si"):
                algo = algo + "if"+words[1]+":\n"+Fix_Iden(algo.split('\n')[-1])
            elif (words[0]=="sinon"):
                try:
                    if (words[1]=="si"):
                        algo = algo + "elif"+words[2]+":\n"+Fix_Iden(algo.split('\n')[-1])
                except:
                    algo = algo + "else:\n"+Fix_Iden(algo.split('\n')[-1])
        elif "ecrire" in line:
            words = line.split()
            algo = algo +"print" + words[1]+"\n"+Fix_Iden(algo.split('\n')[-1])
        else:
            i=0
            x=0
            while (i<len(line)):
                if (line[i]==" "):
                    x = x+1
                else:
                    break
                i=i+1
            algo = algo + line[x:]+"\n"+Fix_Iden(algo.split('\n')[-1])



x = open("output.txt","w")
x.close()