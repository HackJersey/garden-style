import json

mylist = [line.rstrip().split(',') for line in open("localnames.csv", "r") if '"' not in line]


localnames=open("localnames.csv", "r")
for line in localnames.readlines():
    if '"' in line:
        newstring=["The " + line[1:line.find(",")]]
        restofline = line[line.find(",", line.find(",")+1)+1:].rstrip().split(',')
        mylist.append(newstring+restofline)
    else:
        continue

localnames.close()

newlist = []
for item in mylist:
    mydict = {}
    mydict['nick'] = [item[0]]
    mydict['town'] = item[1]
    mydict['county'] = item [2]
    mydict['uniqname'] = "_".join(item[1].split()) + "_" + item[2]
    newlist.append(mydict)
    
flist=newlist[1:]


#loop through the list of dictionaries. 
#If the uniqname appears, then just add the nick to the list of nicks for that entry.
#if not, make a new entry

biglist=[]

for item in flist:
    if any(myitem['uniqname'] == item['uniqname'] for myitem in biglist):
        for myitem in biglist:
            if myitem['uniqname']==item['uniqname']:
                myitem['nick'].append(item['nick'][0])
            else:
                pass
    else:
        biglist.append(item)

myfile=open("output.txt","w")

print >> myfile, json.dumps(biglist)
myfile.close()