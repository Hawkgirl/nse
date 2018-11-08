class stock():
	def __init__(self, *arg, **kwargs):
		
		if 'name' in kwargs: 
			self._name=kwargs['name']
		if 'ltp' in kwargs:
			self._ltp=kwargs['ltp']
		if 'high52' in kwargs:
			self._high52=kwargs['high52']
		

        @property
        def name(self):
            return self._name

        @property
        def ltp(self):
            return self._ltp

	@property
	def high52(self):
	    return self._high52
