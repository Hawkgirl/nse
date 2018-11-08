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

		ltp_url='https://www.nseindia.com/archives/equities/mkt/MA071118.csv'
		req = urllib2.Request(ltp_url, headers={'User-Agent' : "Magic Browser"}) 
		response = urllib2.urlopen( req )
		cr = csv.reader(response)

		ltp_dict = {}
		for row in cr:
			if len(row) < 3: continue
			if row[2] != 'EQ': continue
			if row[1] not in high_dict: continue
			s = stock(name=row[1],high52=high_dict[row[1]],ltp=row[3])
			result.append(s)

		return result
