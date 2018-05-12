import ccxt
from pprint import pprint
import time
from numpy import NaN

Exchanges = []
Names = []

counterPart = 'ETH'
baseCurrency = 'BTC'
pair = counterPart+'/'+baseCurrency
limit = 3
highLimit = 0.2
lowLimit = 0.001
#print (ccxt.exchanges)
lengthLimit = 10
length = 0
for i in ccxt.exchanges:
    exchange = getattr(ccxt,i)()
    try:
        #print (exchange.fetch_order_book(pair,limit))
        exchange.fetch_order_book(pair,limit)
        Names.append(str(i))
        Exchanges.append(exchange)
        length = length + 1
        if length > lengthLimit:
            break
        #break
    except:
        pass
gatewaysLength = len(Exchanges)


MES = [{} for i in Exchanges]
bids = [NaN for i in Exchanges]
bidsVolum = [NaN for i in Exchanges]
asks = [NaN for i in Exchanges]
asksVolum = [NaN for i in Exchanges]

for i in range(gatewaysLength):
    try:
        mes = Exchanges[i].fetch_order_book(pair,limit)
        MES[i] = mes
        #print (mes)
        bidPrice = mes['bids'][0][0]
        askPrice = mes['asks'][0][0]
        if bidPrice < highLimit and bidPrice > lowLimit:
            bids[i] = bidPrice
            bidsVolum[i] = mes['bids'][0][1]
        else:
            bids[i] = NaN
            bidsVolum[i] = NaN
        if askPrice < highLimit and askPrice > lowLimit:
            asks[i] = askPrice
            asksVolum[i] = mes['asks'][0][1]
        else:
            asks[i] = NaN
            asksVolum[i] = NaN
    except:
        MES[i] = {}
        bids[i] = NaN
        asks[i] = NaN
        print (Names[i] + ' has error')


#print (bids)
#print (asks)


highestBid = max(bids)
lowestAsk = min(asks)
sellIndex = bids.index(highestBid)
buyIndex = asks.index(lowestAsk)

profit = highestBid/lowestAsk-1.
tradeVolum = min([ bidsVolum[sellIndex] , asksVolum[buyIndex] ])
print ('there are '+ str(gatewaysLength) + ' exchanges ')
print ('buy '+ str(tradeVolum)+ 'ETH at ' + Names[buyIndex] + ' and sell at '+ Names[sellIndex] + ' profit: ' + str(profit) )






