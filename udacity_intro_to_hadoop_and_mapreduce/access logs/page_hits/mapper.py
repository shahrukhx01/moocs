#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

path_strip = "http://www.the-associates.co.uk"
for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, id, username, date, zone, method, asset, protocol, status, size = data
	if (path_strip in asset):
		asset = asset.replace(path_strip, '')
	if len(asset.strip()) > 0:        
		print "{0}\t{1}".format(asset, 1)

