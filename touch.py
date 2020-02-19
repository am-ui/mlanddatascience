import sys
file_names=sys.argv[1:]
prit(file_names)

for i in file_names:
    f=open(i,'w')
    f.close()