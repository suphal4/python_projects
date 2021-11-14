import os,sys
morse_to_eng_dict = { '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g','....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '}
path=sys.argv[1]
output=sys.argv[2]
for files in os.listdir(path):
    b=''
    if files.endswith('.txt'):
        outputfile=os.path.join(path,files)
        openfile=open(outputfile,'r')
        code=openfile.read()
        code=code.lower()
        if '\n' in code :
            code=code.replace('\n','')
        if (code[0]=='c'):
            for i in range (0,len(code)):
                if (code[i]==':'):
                    for j in range (i+1,len(code)):
                        if (code[j]==' '):
                            b+=' '
                        elif (code[j]=='a'):
                            b+='x'
                        elif (code[j]=='b'):
                            b+='y'
                        elif (code[j]=='c'):
                            b+='z'
                        else:
                            x=ord(code[j])
                            x=x-3
                            y=chr(x)
                            b+=y
                    break      
        elif (code[0]=='h'):
            for i in range (0,len(code)):
                if (code[i]==':'):
                    
                    for j in range (i+1,len(code),3):
                        a=code[j]+code[j+1]
                        x=bytes.fromhex(a)
                        y=x.decode('ASCII')
                        b+=y
                        
                    break
        elif (code[0]=='m'):
            ind=code.index(":")
            data=code[ind+1:]
            a=""
            for i in data:
                if i==" ":
                    y=morse_to_eng_dict.get(a)
                    b+=y
                    a=""
                    continue
                a+=i
            y=morse_to_eng_dict.get(a)
            b+=y
        files=files.replace('.txt','_j54137ss.txt')
        output2=os.path.join(output, files)
        out=open(output2,'w')
        out.write(b.lower())
        out.close
                    
