#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#


import sys
import re
node_head = True
user_head = True

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 19:
	if node_head != True:
        	id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
		print int(author_id.replace("\"","")),"\t","B","\t",id, "\t",title,"\t", tagnames,"\t",node_type, "\t",parent_id, "\t",abs_parent_id,"\t", added_at, "\t",score
	else:
		node_head = False
		continue
		
    elif len(data) == 5:			
	if user_head != True and re.match('^[0-9]+$',data[2].replace("\"","")):	
		user_ptr_id, reputation, gold, silver, bronze = data
		print int(user_ptr_id.replace("\"","")),"\t","A","\t",reputation,"\t", gold,"\t", silver,"\t", bronze
	else:
		user_head = False
		continue

