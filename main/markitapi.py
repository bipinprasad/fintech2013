'''
Created on Nov 10, 2013

@author: Bipin
'''
import time
import urllib2 as urllib
import string

def getPortfolioValueOnDate(portfolio, dt):
    url = 'http://example.markit.com/TestApi/SampleRequest/xml?count=3&echo=example'
    data = 'symbols=%s' % ','.join(portfolio.key())
    u = urllib.urlopen(url, data=data)
    for line in u:
        line = string.strip(line)
        print 'Tradier response line =%s' % line
    u.close()


def main():
    pass

if __name__ == '__main__':
    main()