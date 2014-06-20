from PySSSS import decode
import StringIO
import sys

k = len(sys.argv) - 1

outputs = []

for i in xrange(k):
  outputs.append(StringIO.StringIO(sys.argv[i + 1].decode('hex')))

inputs = []
for i in xrange(k):
  inputs.append(outputs[i])

for i in xrange(k):
  inputs[i].seek(0)

output = StringIO.StringIO()
decode(inputs,output)  
print output.getvalue()
