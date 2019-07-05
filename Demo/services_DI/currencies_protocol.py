import re

class Currency:
	def __init__(self, currency_regex, currency_value_US):
		self.valid_regex = currency_regex
		self.value = currency_value_US
		self.status = False
		self.name = None

	def validate_hash(self, hash_digest):
		if re.match(self.valid_regex, hash_digest):
			self.status = True
			return self.status

	def __str__(self):
		repr_str = '='*5 + self.name + '='*5 + '<br/>'
		repr_str += 'value: $US {}'.format(str(self.value) if self.status else 0)
		return repr_str

	@staticmethod
	def check_currencies(currencies_list, hash_to_validate):
		output = ''
		for currency_class in currencies_list:
			currency_instance = currency_class()
			currency_instance.validate_hash(hash_to_validate)
			output += currency_instance.__str__()
			output += '<br/>'

		return output

class Ethereum(Currency):
	def __init__(self):
		super().__init__('000.*', 283.12)
		self.name = 'Ethereum'

class Bitcoin(Currency):
	def __init__(self):
		super().__init__('111.*', 10090.50)
		self.name = 'Bitcoin'


if __name__ == "__main__":
	eth1 = Ethereum(r'000.*')
	eth1.validate_hash('000ABC')
	bit1 = Bitcoin(r'22.*')
	bit1.validate_hash('22#gABC')
	print(eth1, bit1, sep='<br/>')
