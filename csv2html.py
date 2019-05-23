#!/bin/python
#
#  Convert CSV to HTML table
#
#
# CSV for Debug
#
#  sun,mon,tue,wed,thu,fri,sat
#  1,2,3,4,5,6,7
#  on,off,off,on,off,off,off
#  fine,fine,cloudy,rain,fine,fine,fine
#

import sys
import time
import csv

rhder = False
chder = False
usage = False

# options
for opt in sys.argv[1:]:
    if "-h" == opt:
        rhder = True
    elif "-H" == opt:
        chder = True
    else:
        usage = True
        break

if usage is True:
    print "USAGE:\n"
    print "  {} [ -h | -H ]\n".format(sys.argv[0])
    print "  -h : Row Header"
    print "  -H : Colum Header\n"
    print "EXAMPLE:\n"
    print "  cat hoge.csv |  {} -h\n".format(sys.argv[0])
    sys.exit()


# table tag
print("<table>")
for row in csv.reader(iter(sys.stdin.readline, '')):
    print("<tr>")

    if rhder or chder:
        tag = "th"
    else:
        tag = "td"

    for col in row:
        print("<{0}>{1}</{0}>".format(tag, col))
        if rhder is False:
            tag = "td"

    rhder = False
    tag = "td"
    print("</tr>")
print("</table>")
