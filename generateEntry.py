#!/usr/bin/python

import sys

if len(sys.argv)<2:
    print 'Error: please indicate the number of entry member'

totalMember = int(sys.argv[1])

if len(sys.argv)<3:
    prefix = ''
else:
    prefix = sys.argv[2]

if len(sys.argv)<4:
    zeroFillMax = 2
else:
    zeroFillMax = int(sys.argv[3])

f = open('generated_entry.txt', 'w')
    
print 'Total entry members: '+str(totalMember)
print 'Generating entry ....'
print '************************************************'
print ''

for i in range(1,totalMember+1):
    line ='[img['+prefix+str(i).zfill(zeroFillMax)+'.jpg]]'
    print line
    print ''

    f.write(line+'\n\n')

print ''
print '************************************************'

f.close()
