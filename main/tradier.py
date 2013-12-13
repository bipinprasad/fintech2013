'''
Created on Nov 9, 2013

@author: Bipin
'''
import urllib2 as urllib
import string

TRADIER_AUTH_KEY = 'Bearer pj1dbQ02ag02nydj0Wp4WjUuAPiz'

def getSymbolClosingPrices(symbols):
    url = 'https://api.tradier.com/v1/markets/quotes'
    data = 'symbols=%s' % ','.join(symbols)
    u = urllib.urlopen(url, data=data)
    for line in u:
        line = string.strip(line)
        print 'Tradier response line =%s' % line
    u.close()

def main():
    getSymbolClosingPrices(['APPL', 'IBM'])
    
if __name__ == '__main__':
    main()