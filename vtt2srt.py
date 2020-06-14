#vttname=input('input filename')
#Official This House by James Graham _ Free National Theatre Live Full Performance-6vsSHyjEMrg.en-GB.vtt
#vtt=open(vttname)
import re
filename = input('Enter vtt file name: ')
fhand = open(filename, encoding='utf-8')
foutname = re.findall("(.*).vtt", filename)
foutname = foutname[0] + '.srt'
wsrt = open(foutname,'w+',encoding='utf-8')
diagf = False
diagn = 0
for line in fhand:

    if re.search('[0-9][0-9]:[0-9][0-9]',line):
        diagf = True
        diagn += 1
        wsrt.write(str(diagn)+'\n')
        wsrt.write(line.replace('.',','))
        
    elif diagf:
        wsrt.write(line.strip()+'\n')
        

fhand.close()
wsrt.close()
