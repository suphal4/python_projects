import os,sys
english=sys.argv[1]
path=sys.argv[2]
output=sys.argv[3]
for files in os.listdir(path):
    if files.endswith('.txt'):
        outputfile=os.path.join(path,files)
        openfile=open(outputfile,'r')
        xopen = open(english)
        x=xopen.read().split()
        y=openfile.read().split()
        ucase=0
        punc=0
        num=0
        words=0
        cwords=0
        inwords=0
        punc_list = '''.?!,:;—-(){}[]'""…'''
        num_list = "1234567890"
        for i in y:

            for j in i:
                if j.isupper():
                    ucase+=1
                    i=i.replace(j,j.lower())
                if j in punc_list:
                    punc+=1
                    i=i.replace(j,"")
                if j in num_list:
                    num+=1
                    i=i.replace(j,"")
            if len(i)==0:
                continue
            words+=1
            if i in x:
                cwords+=1
            else:
                inwords+=1

        files=files.replace('.txt','_j54137ss.txt')
        output2=os.path.join(output, files)
        out=open(output2,'w')
        out.write(f"""j54137
Formatting ###################
Number of upper case letters changed: {ucase}
Number of punctuations removed: {punc}
Number of numbers removed: {num}
Spellchecking ###################
Number of words: {words}
Number of correct words: {cwords}
Number of incorrect words: {inwords}
""")
        out.close()
