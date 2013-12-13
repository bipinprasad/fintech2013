'''
Created on Nov 10, 2013

@author: Bipin
'''
import string
import time
import ystockquote

def printBuyAndHoldPortfolioValuation(portfolio, startDate, endDate):
    printPortfolioValuationDifferences([portfolio, portfolio], [startDate, endDate], 'Buy and Hold Strategy')

def printPortfolioValuationDifferences(portfolios, dts, strategyName):
    print strategyName
    numPortfolios = min(len(portfolios), len(dts))
    time.sleep(2.0)
    firstVal = valuePortfolio(portfolios[0],dts[0]) 
    time.sleep(2.0)
    lastVal  = valuePortfolio(portfolios[numPortfolios-1],dts[numPortfolios-1])
    vals = [firstVal, lastVal]
    print '\t%s to %s : $ %f --> $ %f %f %%' %(dts[0], dts[numPortfolios-1], firstVal, lastVal, 100.0*(lastVal-firstVal)/firstVal)
    numVals = len(vals)
    #for i in range(numVals):
    #    print '\t%s : $ %f   %f %%' %(dts[i], vals[i], 100*(vals[i]-vals[0])/vals[0])
    # print '\t%s : $ %f   %.2f%%' %(dts[0], vals[0], 100*(vals[0]-vals[0])/vals[0])
    # print '\t%s : $ %f   %.2f%%' %(dts[numVals-1], vals[numVals-1], 100*(vals[numVals-1]-vals[0])/vals[0])
    
def valuePortfolio(portfolio, dt):
    '''
    @ToDo: Error Handling
    '''
    
    portfolioVal = 0.0
    for symbol in portfolio:
        qty = portfolio[symbol]
        retVal = ystockquote.get_historical_prices(symbol, dt, dt)
        if retVal:
            quote  = retVal[dt]
            if quote:
                try:
                    closePrice = float(string.strip(quote['Close']))
                    portfolioVal += qty * closePrice
                except:
                    print 'Cannot convert closing price %s to float for symbol %s, quote=%s' % (quote['Close'], quote)
            else:
                print 'WARNING: No price retrieved from Yahoo Finance for symbol=%s, date=%s, retVal=%s' % (symbol, dt, retVal)
        else:
            print 'WARNING: No price retrieved from Yahoo Finance for symbol=%s, date=%s' % (symbol, dt)

                
    return portfolioVal
        

def main():
    dt = '2013-11-05'
    retVal = ystockquote.get_historical_prices('AAPL', dt, dt)
    quote = retVal['2013-11-05']
    print '%s: Close=%s, quote=%s' % (dt, quote['Close'], quote)

if __name__ == '__main__':
    main()