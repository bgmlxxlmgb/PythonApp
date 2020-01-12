import urllib2
def downloadOneFileWithUrlLib2(url):
    f = urllib2.urlopen(url)
    data = f.read()
    print data
if __name__ == "__main__":
    url_01='https://www.toutiao.com/ch/news_hot/'
    downloadOneFileWithUrlLib2(url_01)