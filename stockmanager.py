class stockmanager():

	def get_all_stocks(self):
		result = []

		from stock import stock
		high_url='https://www.nseindia.com/content/CM_52_wk_High_low.csv'
		import csv
		import urllib2

		req = urllib2.Request(high_url, headers={'User-Agent' : "Magic Browser"}) 
		response = urllib2.urlopen( req )
		cr = csv.reader(response)


		high_dict = {}
		for row in cr:
			if len(row) < 2: continue
			if row[1] != 'EQ': continue
			#print row
			high_dict[row[0]]= row[2]

		import datetime
		for i in range(3):
			d = datetime.datetime.now() - datetime.timedelta(days=i)
			try:
				ltp_url='https://www.nseindia.com/archives/equities/mkt/MA'+d.strftime("%d")+d.strftime("%m")+d.strftime("%y")+'.csv'
				req = urllib2.Request(ltp_url, headers={'User-Agent' : "Magic Browser"}) 
				response = urllib2.urlopen( req )
				break
			except urllib2.HTTPError:
				continue
		cr = csv.reader(response)

		ltp_dict = {}
		import industry
		for row in cr:
			if len(row) != 6: continue
			if row[2] != 'EQ': continue
			if row[1] not in industry.watchlist: continue
			if row[1] not in high_dict: continue
			s = stock(name=row[1],high52=int(float(high_dict[row[1]])),ltp=int(float(row[3])), tradevalue=int(float(row[4])))
			result.append(s)

		return result

	def get_near_high52(self, max=20):
		stocks = self.get_all_stocks()
		sorted_stock = sorted(stocks, key = lambda stock: stock.high52gap)

		for i in range(max):
			print sorted_stock[i].name, sorted_stock[i].ltp, sorted_stock[i].high52, sorted_stock[i].high52gap, sorted_stock[i].tradevalue
