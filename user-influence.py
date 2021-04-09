import pickle
import numpy as np
import sys

def jac(l1,l2):
	inter=list(set(l1) & set(l2))
	uni=list(set(l1) | set(l2))
	try:
		return float(len(inter))/float(len(uni))*1.0
		#return float(len(inter))/float(min(len(l1),len(l2)))*1.0

	except:
		return 0

def Sort_Tuple(tup):
	lst=len(tup)
	for i in range(0,lst):
		for j in range(0,lst-i-1):
			if int(tup[j][1])>int(tup[j+1][1]):
				temp=tup[j]
				tup[j]=tup[j+1]
				tup[j+1]=temp

	return tup

mj=pickle.load(open("sample-memjoin","rb"))
egroup=pickle.load(open("sample-egroup","rb"))
ge={}
for k in egroup.keys():
	try:
		ge[egroup[k]].append(k)
	except:
		ge[egroup[k]]=[k]


gj={}
gmem={}
for k in mj.keys():
	gj[k]=[]
	for i in range(0,len(mj[k])):
		gj[k].append(mj[k][i][0])
		try:
			gmem[mj[k][i][0]].append(k)
		except:
			gmem[mj[k][i][0]]=[k]


me={}
ersvp=pickle.load(open("sample-ersvp","rb"))
dd={}
for k in ersvp.keys():
	rsvp=Sort_Tuple(ersvp[k])
	for i in range(0,len(rsvp)):
		try:
			me[rsvp[i][0]].append(k)
		except:
			me[rsvp[i][0]]=[k]
	for i in range(0,len(rsvp)-1):
		dd[rsvp[i][0]]={}

groupjoin=pickle.load(open("sample-groupjoin","rb"))
print("groupjoin=",len(groupjoin))


count=0
d={}

for k in groupjoin.keys():
	rsvp=Sort_Tuple(groupjoin[k])
	print(k)
	for i in range(0,len(rsvp)-1):
		d[rsvp[i][0]]={}

for k in groupjoin.keys():
	rsvp=Sort_Tuple(groupjoin[k])
	count+=1
	print("count=",count)
	for i in range(0,len(rsvp)-1):
		x=rsvp[i][0]
		for j in range(i+1,len(rsvp)):
			if int(rsvp[j][1])-int(rsvp[i][1])<=86400000 and int(j-i)<=3:
					try:
						d[x][rsvp[j][0]]+=1
					except:
						d[x][rsvp[j][0]]=1

pickle.dump(d,open("sample-influence","wb"))

print "The pairwise influence between users:"
for k in d.keys():
	for k1 in d[k].keys():
		print("Value for",k,k1," is ",d[k][k1])









