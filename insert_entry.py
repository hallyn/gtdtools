#!/usr/bin/python

# Copyright (C) 2009-2017 Serge Hallyn <serge@hallyn.com>

import sys
import time
import datetime
import string

debug = False

def process_bydate(line):
	day = int(line[0])
	desc = string.join(line[1:])
	filename = "%02d" % day
	if debug:
		print("opening (by date) %s" % filename)
	f = open(filename, "a")
	f.writelines(["XXX %s XXX\n" % desc])
	f.close()

dayhash = { 'M': 1, 'Mon': 1,'Monday': 1,
	'T': 2, 'Tue': 2, 'Tuesday': 2,
	'W': 3, 'Wed': 3, 'Wednesday': 3,
	'R': 4, 'Tr': 4, 'Thur': 4, 'Thurs': 4, 'Thursday': 4,
	'F': 5, 'Fri': 5, 'Friday': 5,
	'Sat': 6, 'Saturday': 6,
	'Sun': 7, 'Sunday': 7 }

def process_monthly(line):
	day = line[0]
	wk = line[1]
	start = line[2]
	end = line[3]
	desc = string.join(line[4:])
	today = time.localtime()
	y = today[0]
	m = today[1]
	firstdayofmonth = int(datetime.datetime(y, m, 1).strftime("%w"))
	if debug:
		print("firstdayofmonth is %d" % firstdayofmonth)
	tmp = dayhash[day] - firstdayofmonth + 1
	if debug:
		print("tmp is now %d" % tmp)
	if (firstdayofmonth > dayhash[day]):
		tmp += 7
	tmp += (int(wk)-1)*7
	filename = "%02d" % tmp
	if debug:
		print("my line was : %s" % str(line))
		print("so i'm opening : %s" % filename)
	f = open(filename, "a")
	f.writelines(["XXX %s-%s: %s XXX\n" % (start, end, desc)])
	f.close()

months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]

def process_annual(line):
	if debug:
		print("here I am with %s " % line)
	month = line[0]
	date = line[1]
	desc = string.join(line[2:])
	today = time.localtime()
	y = today[0]
	m = today[1]
	if months[m-1] != month:
		return
	filename = "%02d" % int(date)
	if debug:
		print("my line was : %s" % str(line))
		print("so i'm opening : %s" % filename)
	f = open(filename, "a")
	f.writelines(["XXX %s XXX\n" % (desc)])
	f.close()

def process_weekly(line):
	day = line[0]
	start = line[1]
	end = line[2]
	desc = string.join(line[3:])
	today = time.localtime()
	y = today[0]
	m = today[1]
	firstdayofmonth = int(datetime.datetime(y, m, 1).strftime("%w"))
	if debug:
		print("firstdayofmonth is %d" % firstdayofmonth)
	tmp = dayhash[day] - firstdayofmonth + 1
	if debug:
		print("tmp is now %d" % tmp)
	if (firstdayofmonth > dayhash[day]):
		tmp += 7
	if debug:
		print("tmp is now %d" % tmp)
	while tmp <= 31:
		filename = "%02d" % tmp
		if debug:
			print("my line was : %s" % str(line))
			print("so i'm opening : %s" % filename)
		f = open(filename, "a")
		f.writelines(["XXX %s-%s: %s XXX\n" % (start, end, desc)])
		f.close()
		tmp += 7

a = sys.argv
type = a[1]
if type == 'M':
	process_monthly(a[2:])
elif type == 'D':
	process_bydate(a[2:])
elif type == 'W':
	process_weekly(a[2:])
elif type == 'A' or type == 'Y':
	process_annual(a[2:])
else:
	print("I don't know how to handle this entry: %s" % str(sys.argv[1:]))
