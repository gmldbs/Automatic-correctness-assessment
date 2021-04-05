import csv
import sys

file_path = sys.argv[1]
bug_info = sys.argv[2]
f = open(file_path,'r',encoding='utf-8')
FL_result_file = open("/TBar/SuspiciousCodePositions/"+bug_info+"/Ochiai.txt",'w')
rdr = csv.reader(f)
cnt = 0
for line in rdr:
    cnt += 1
    if cnt == 1: continue
    if float(line[1]) == 0: continue
    line = line[0].split('#')
    line = line[0]+'@'+line[1]
    line = line.split('.java')
    line = line[0]+line[1]
    line = line.split('/')
    new = ""
    for each in line:
        new+=each+'.'
    new = new[:-1]
    FL_result_file.write(new+'\n')
f.close()
FL_result_file.close()
