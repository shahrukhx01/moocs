#!/usr/bin/python

import sys

hitsTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
nodes = []
users = []
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 6 and len(data_mapped)!= 10:
        # Something has gone wrong. Skip this line.
        continue
    if "A" in data_mapped[1]  :
	users.append(data_mapped)
    elif 'B' in data_mapped[1]:
	nodes.append(data_mapped)
    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        oldKey = thisKey;
	for node in nodes:
		author_id,type,id,title,tagnames,node_type,parent_id,abs_parent_id, added_at,score = node
		#print author_id,"\t",id, "\t",title,"\t", tagnames,"\t",node_type, "\t",parent_id, "\t",abs_parent_id,"\t", added_at, "\t",score
		for user in users:
			user_ptr_id, data_type, reputation, gold, silver, bronze = user
			print author_id,"\t",id, "\t",title,"\t", tagnames,"\t",node_type, "\t",parent_id, "\t",abs_parent_id,"\t", added_at, "\t",score,"\t",reputation,"\t", gold,"\t", silver,"\t", bronze
    oldKey = thisKey
   

if oldKey != None:
    	for node in nodes:
		author_id,type,id,title,tagnames,node_type,parent_id,abs_parent_id, added_at,score = node
		#print author_id,"\t",id, "\t",title,"\t", tagnames,"\t",node_type, "\t",parent_id, "\t",abs_parent_id,"\t", added_at, "\t",score
		for user in users:
			user_ptr_id, data_type,reputation, gold, silver, bronze = user
			print author_id,"\t",id, "\t",title,"\t", tagnames,"\t",node_type, "\t",parent_id, "\t",abs_parent_id,"\t", added_at, "\t",score,"\t",reputation,"\t", gold,"\t", silver,"\t", bronze

