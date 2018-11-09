class stock():
	def __init__(self, *arg, **kwargs):
		
		if 'name' in kwargs: 
			self._name=kwargs['name']
		if 'ltp' in kwargs:
			self._ltp=kwargs['ltp']
		if 'high52' in kwargs:
			self._high52=kwargs['high52']
		if 'tradevalue' in kwargs:
			self._tradevalue=kwargs['tradevalue']/10000000
		

        @property
        def name(self):
            return self._name

        @property
        def ltp(self):
            return self._ltp

	@property
	def high52(self):
	    return self._high52

	@property
	def tradevalue(self):
	    return self._tradevalue

	@property
	def high52gap(self):
		if self.ltp == 0: return 0
		if self.high52 == self.ltp : return 0
		val = (((float(self.high52 - self.ltp))/float(self.ltp)) * 100)
		return round(val, 2)

