#-*- utf-8 -*-
#urlretrieve

import sys, urllib,os
path="/home/wang/tmp1/"
def reporthook(a,b,c): 
    # ',' at the end of the line is important!
    print "% 3.1f%% of %d bytes\r" % (min(100, float(a * b) / c * 100), c),
    #you can also use sys.stdout.write
    #sys.stdout.write("\r% 3.1f%% of %d bytes" 
    #                 % (min(100, float(a * b) / c * 100), c)
    sys.stdout.flush()
for url in sys.argv[1:]:
     i = url.rfind('/')
     file = url[i+1:]
     filename=os.path.join(path,file)
     print url, "->", filename
     urllib.urlretrieve(url, filename, reporthook)
