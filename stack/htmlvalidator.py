import codecs
import re
from stack.Stack import Stack


def readfile(file):
    lines = []
    for line in codecs.open(file, 'r').readlines():
        if not line == '':
            line = re.sub(r'\s+', '', line, re.UNICODE).strip()
            lines.append(line)
    return ''.join(lines)

#def validatebalance(lines):
#    for line in lines:


linestr = readfile('test.html')
lines = re.findall(r'<.+?>', linestr)
tagstack = Stack()
ge = '<'
goe='</'
ls = '>'
for line in lines:
    if line.startswith(ge) and not line.startswith(goe, 0, 2):
        tag = re.search('%s(.*)%s' % (ge, ls), line).group(1)
        tagstack.push(tag)
    elif line.startswith(goe, 0, 2):
        stag = tagstack.pop()
        tag = re.search('%s(.*)%s' % (goe, ls), line).group(1)
        if not stag == tag:
            print ('Html is not properly created: %s' %(stag))

#validatebalance(lines)
