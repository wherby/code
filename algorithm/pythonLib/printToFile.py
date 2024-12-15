# https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file
# However, redirecting stdout also works for me. It is probably fine for a one-off script such as this:

import sys

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

for i in range(2):
    print('i = ', i)

sys.stdout = orig_stdout
f.close()