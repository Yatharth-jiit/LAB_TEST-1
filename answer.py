import numpy as np
patients = {101:['sonu',102,'Skin Disease',12000],102:['Tonu',103,'Liver Disease',21000],103:['soniya',102,'Skin Disease',25000]}
doctors = {102:['Dr. Rajeev','Skin Specialist'],103 :['Dr. Monty','Liver']}
print(patients.items())
pats = np.array(patients)
docs = np.array(doctors) 
print(pats)
print(docs)
def getpats(docid):
    newlist = []
    for keys,values in patients.items():
        if (values[1]==docid):
            newlist.append(values)
    print(newlist)
getpats(102)
def uptreat(patid,newtreat):
    patients[patid][2]=newtreat
uptreat(101,"Cancer")
print(patients)
newdocdict = {}
for key,value in patients.items():
    if (value[1] not in newdocdict):
        newdocdict[value[1]]=1
    else :
        newdocdict[value[1]]=newdocdict[value[1]]+1
    
print(newdocdict)
maxid =-1
minid =-1
valuemax = 0
valuemin = 100
for key,value in newdocdict.items():
    if (value>valuemax):
        valuemax = value
        maxid = key
    if (value <valuemin):
        valuemin= value
        minid = key
        
print("doctor : ",maxid," has the maximum patients : ",valuemax)
print("doctor : ",minid," has the minimum patients : ",valuemin)
print(patients)
minbill = 100000
maxbill = -50
patidmax = -1
patidmin= -1

for key,value in patients.items():
        if (value[3]>maxbill):
            maxbill = value[3]
            patidmax = key
        if (value[3]<minbill):
            minbill = value[3]
            patidmin = key
newans = []
newans.append(patients[patidmax])
newans.append(patients[patidmin])
print("details of the patient with max bill : ", newans[0])
print("details of the patient with min bill : ", newans[1])
