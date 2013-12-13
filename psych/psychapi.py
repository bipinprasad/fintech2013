'''
Created on Nov 9, 2013

@author: Bipin
'''
import threading
import Queue
import urllib2 as urllib
import string

PSYCH_SIGNAL_APIKEY = 'e84a4635a4112f3d81d5559214b0abbd'
ALL_SENTIMENT_CSV_FILE_PATTERN = 'allnysesentiment-%d%02d.csv'

threadLock = threading.Lock()

class MyThread (threading.Thread):
    def __init__(self, inq, queue, year, month, day):
        threading.Thread.__init__(self)
        self.inq = inq
        self.queue = queue
        self.year = year
        self.month = month
        self.day = day
        
    def run(self):
        # print 'Starting thread for symbol: %s' % self.symbol
        # threadLock.acquire()
        while True:
            if self.inq.empty():
                break
            try:
                symbol = self.inq.get(block=False)
                if not symbol:
                    break
            except:
                break
            sentiment = getSymbolMeanSentiment(symbol, self.year, self.month, self.day)
            record    = (symbol, sentiment)
            self.queue.put(record)
        #print 'Putting on queue %s:%f' % record
        # threadLock.release()
        #print 'Ending thread for symbol: %s' % self.symbol
        
def getSymbolMeanSentiments(symbols, year, month, day=8):
    sentiments = dict()
    inq   = Queue.Queue()
    queue = Queue.Queue()
    
    allThreads = list()
    validSymbols = [x for x in symbols if x]
    for symbol in validSymbols:
        inq.put(symbol)
        
    for _ in range(min(len(validSymbols),50)):
        t = MyThread(inq, queue, year, month, day=day)
        t.start()
        allThreads.append(t)
    
    for _ in range(len(validSymbols)):    
        symbol,sentiment = queue.get(block=True)
        sentiments[symbol] = sentiment
        #print 'Read from queue %s,%f' % (symbol,sentiment)
    for t in allThreads:
        t.join()
    
    return sentiments

def getSymbolDailySentiment(symbol, year, month, day=8):
    url = 'https://psychsignal.com/api/sentiments?api_key={YOUR_API_KEY}&symbol={SYMBOL}&from={START_DATE}&to={END_DATE}&period={PERIOD}&format={FORMAT}'
    url = 'https://psychsignal.com/api/sentiments?api_key=%s&symbol=%s&from=%d-%02d-%02d&to=%d-%02d-%02d&period=d&format=csv' % (PSYCH_SIGNAL_APIKEY, symbol, year, month, day, year, month, day)
    u = urllib.urlopen(url)
    for line in u:
        print line,
    u.close()
    
def getSymbolMeanSentiment(symbol, year, month, day=8):
    '''
    Return the signal - buy - sell
    '''
    startYear  = year
    startMonth = month-1
    if startMonth < 1:
        startYear = year - 1
        startMonth = 1
    
    url = 'https://psychsignal.com/api/sentiments?api_key=%s&symbol=%s&from=%d-%02d-%02d&to=%d-%02d-%02d&period=d&format=csv' % (PSYCH_SIGNAL_APIKEY, symbol, startYear, startMonth, day, year, month, day)
    
    lineCnt = 0
    sumBullish = 0.0
    u = urllib.urlopen(url)
    for line in u:
        line = string.strip(line)
        if not line:
            continue
        fields = line.split(',')
        try:
            bullish = float(fields[2]) - float(fields[3])
            sumBullish += bullish
            lineCnt += 1
        except:
            pass
    u.close()
    return sumBullish / lineCnt if lineCnt else 0

def createNyseSentimentFile(symbols, year, month):
    allSentimentCsvFile = ALL_SENTIMENT_CSV_FILE_PATTERN % (year, month)
    f = open(allSentimentCsvFile, 'w')
    sentiments = getSymbolMeanSentiments(symbols, year, month)
    for symbol,sentiment in sentiments.items():
        s = '%s,%s' % (symbol, sentiment)
        print s
        f.write('%s\n' % s)
        # if i > 20:
        #     break
    f.close()
    
def createHistoricalMeanSentimentFiles(symbols):
    #for year in range(1990, 2013):
    #    for month in range(1,13):
    #        createNyseSentimentFile(year, month, symbols)
    for month in range(1,12):
        createNyseSentimentFile(symbols, 2013, month)

def getSymbolsWithNonZeroSentiments(year, startMonth, endMonth):
    nonZeroSymbols = set()
    zeroSymbols = set()
    
    for month in range(startMonth, endMonth+1):
        allSentimentCsvFile = ALL_SENTIMENT_CSV_FILE_PATTERN % (year, month)
        f = open(allSentimentCsvFile, 'r')
        for line in f:
            fields = string.strip(line).split(',')
            if len(fields) < 2:
                continue
            symbol = string.strip(fields[0])
            sentiment_str = string.strip(fields[1])
            if symbol and sentiment_str:
                try:
                    sentiment = float(sentiment_str)
                except:
                    print 'Cannot convert sentiment %s to float for symbol %s' % (sentiment_str, symbol)
                if abs(sentiment-0.0) > 0.00001:
                    nonZeroSymbols.add(symbol)
                else:
                    zeroSymbols.add(symbol)
        f.close()
    return nonZeroSymbols - zeroSymbols

def main():
    createMonthlySymbolFiles = False
    createAllNonZeroSymbolFile      = True
    
    if createMonthlySymbolFiles:
        from main.main import allNyseSymbols
        createHistoricalMeanSentimentFiles(allNyseSymbols)
    
    if createAllNonZeroSymbolFile:
        nonZeroSymbols = getSymbolsWithNonZeroSentiments(2013, 1, 11)
        f = open('nonzerosymbols.txt', 'w')
        for symbol in sorted(nonZeroSymbols):
            f.write('%s\n' % symbol)
        f.close()
    
    # getSymbolDailySentiment('AAPL')


if __name__ == '__main__':
    main()