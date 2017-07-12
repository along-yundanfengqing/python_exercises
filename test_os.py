import os
import sys, urllib,os
def reporthook(a,b,c): 
    # ',' at the end of the line is important!
    print "% 3.1f%% of %d bytes\r" % (min(100, float(a * b) / c * 100), c),
    #you can also use sys.stdout.write
    #sys.stdout.write("\r% 3.1f%% of %d bytes" 
    #                 % (min(100, float(a * b) / c * 100), c)
    sys.stdout.flush()
def download(path,url):
     i = url.rfind('/')
     file = url[i+1:]
     filename=os.path.join(path,file)
     print url, "->", filename
     urllib.urlretrieve(url, filename, reporthook)


url=[{"month":10,"days":11,"url":"http://timehut.qiniucdn.com/cn/pictures/original/201703/80912/1f1c3ef132754e9fbffa5c511f919ba22ebda677e4c3aaf2538480c1b01d1693.jpg"},{"month":27,"days":15,"url":"http://.qiniucdn.com/cn/pictures/original/201703/80912/1f1c3ef132754e9fbffa5c511f919ba22ebda677e4c3aaf2538480c1b01d1693.jpg"},{"month":27,"days":15,"url":"http://timehut.qiniucdn.com/cn/pictures/201405/181324/54E29562D0C64C748B36840CD9D8FC5A.jpg"},{"month":10,"days":15,"url":"http://timehut.qiniucdn.com/cn/pictures/original/201703/80912/1f1c3ef132754e9fbffa5c511f919ba22ebda677e4c3aaf2538480c1b01d1693.jpg"}]
errorlist=[]
for i in url:
    month=i['month']
    days=i['days']
    path=str(month)+'/'+str(days)
    try:
        if  os.path.exists(path):
            download(path,i['url'])
        else:
            os.makedirs(path)
            download(path,i['url'])
    except Exception as e:
        errorlist.append(i)
        print e
print 'url %s' % url
print 'errorlist %s '% errorlist

    

