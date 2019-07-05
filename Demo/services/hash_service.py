from flask import Flask
from flask import request
from currencies_protocol import *
import requests
import hashlib

app = Flask(__name__)
services_dir = '127.0.0.1'
verif_service_port = '5001' 
verification_service_dir =  services_dir + ":" + verif_service_port
currencies_protocols = [Bitcoin, Ethereum]

class HashService():
	verification_service = None
	
	def __init__(self, verif_service):
		global verification_service
		verification_service = verif_service
		self.app = app
		self.services_dir = '127.0.0.1'
		self.port = '5000'

	@app.route('/service', methods=['GET'])
	def service():
		client_id = request.args.get('client_id')
		hash_string = request.args.get('hash_string')

		global verification_service
		if verification_service.validate_credentials(client_id):
			client_output = ''
			client_output += 'Valid credentials\n'
			digested_hash = HashService.apply_hash(hash_string)
			client_output += 'Obtained hash: {}\n'.format(digested_hash)
			client_output += 'Checking currencies...\n'
			for currency_class in currencies_protocols:
				values_results = Currency.check_currencies(currencies_protocols, digested_hash)
			client_output += values_results
			return str(client_output)
		else:
			return 'Invalid credentials. Exitting'

	@staticmethod
	def apply_hash(hashing_str):
		result = hashlib.md5(hashing_str.encode())

		return result.hexdigest()

if __name__ == '__main__':
	from verification_service import VerificationService
	vs = VerificationService()
	hs = HashService(vs)
	hs.app.run(host=hs.services_dir, port=hs.port, debug=True)
