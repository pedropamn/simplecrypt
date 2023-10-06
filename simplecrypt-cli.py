import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

try:
    arg = sys.argv[1]
except IndexError as e:
    print("Sem args")

if arg == '-f':
    argContent = sys.argv[2]
elif arg == '-d':
    argContent = sys.argv[2]
elif arg == '':
    print("No args")