from PySSSS import encode
import StringIO
import sys

orig = sys.argv[1]
print "Encrypting [{}]: ".format(orig)

input = StringIO.StringIO(orig)
outputs = []

n = 3
k = 2

for i in xrange(n):
  outputs.append(StringIO.StringIO())

encode(input,outputs,k)

for i in xrange(n):
  print outputs[i].getvalue().encode('hex')


