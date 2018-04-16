import ccxt
from pprint import pprint
import time
huobipro = ccxt.huobipro();
okex = ccxt.okex();
pair = 'ETH/BTC';
limit = 3;

while True:
    DATA = [huobipro.fetch_order_book(pair,limit), okex.fetch_order_book(pair,limit)];
    bids = []
    asks = []
    for data in DATA:
        bids.append(data['bids'][0])
        asks.append(data['asks'][0])

    #print bids, asks
    print 'sell in exchange huobipro and buy in exchange okex, profit:',(1.*bids[0][0] / asks[1][0] - 1.)*100,"%"
    time.sleep(1)
    #pprint (huobipro.fetch_order_book(pair,limit));
    #pprint (okex.fetch_order_book(pair,limit));

    '''
    print huobipro.fetch_order_book(pair,limit);
    print okex.fetch_order_book(pair,limit);
    '''
