import os,sys
path=sys.argv[1]
output=sys.argv[2]
for files in os.listdir(path):
    if files.endswith('.txt'):
        outputfile=os.path.join(path,files)
        openfile=open(outputfile,'r')
        points=openfile.read()
        x=0
        y=0
        for i in range (0,len(points)):
            if (points[i]=='T'):
                pass
            elif (points[i]=='1'):
                if (points[i+1]=='t'):
                    x=x+5
                elif (points[i+1]=='c'):
                    x=x+2
                else:
                    x=x+3
            elif (points[i]=='2'):
                if (points[i+1]=='t'):
                    y=y+5
                elif (points[i+1]=='c'):
                    y=y+2
                else:
                    y=y+3
            else:
                    pass
        files=files.replace('.txt','_j54137ss.txt')
        output2=os.path.join(output, files)
        out=open(output2,'w')
        out.write(str(x) +':' +str(y))
        out.close

