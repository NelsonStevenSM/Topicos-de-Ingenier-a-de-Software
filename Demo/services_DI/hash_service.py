import flask
from flask import Flask
from flask import request, redirect, url_for
from currencies_protocol import *
from verification_service import VerificationService
from simple_injector import *
import requests
import hashlib

verification_service = None
app = Flask(__name__)
currencies_protocols = [Bitcoin, Ethereum]

class HashServiceContainer(Container):
	def __init__(self):
		super().__init__()
		self.currency_generator = Generator(Currency)
		self.verification_generator = Generator(VerificationService)
		self.flask_generator = Generator(Flask)
		
		self.add_generators([self.verification_generator, self.currency_generator, self.flask_generator])

class HashService():
	verification_service = None
	
	def __init__(self, hash_service_container):
		global app, verification_service
		verification_service = hash_service_container.verification_generator()
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
			client_output += 'Valid credentials <br/>'
			digested_hash = HashService.apply_hash(hash_string)
			client_output += 'Obtained hash: {}</br>'.format(digested_hash)
			client_output += 'Checking currencies...</br>'
			for currency_class in currencies_protocols:
				values_results = Currency.check_currencies(currencies_protocols, digested_hash)
			client_output += values_results
			return str(client_output)
		else:
			return 'Invalid credentials. Exitting'

	@app.route('/test', methods=['GET', 'POST'])
	def render_page():
		if flask.request.method == 'GET':
			return HashService.string_from_file('../page/test.html')
		elif flask.request.method == 'POST':
			user_id = str(request.form['user_id'])
			string_to_hash = str(request.form['hashing_string'])

			return redirect(url_for('service', client_id=user_id, hash_string=string_to_hash))

	@staticmethod
	def apply_hash(hashing_str):
		result = hashlib.md5(hashing_str.encode())

		return result.hexdigest()

	@staticmethod
	def string_from_file(file_path):
		with open(file_path, 'r') as file:
			data = file.read().replace('\n', '')
		return data

if __name__ == '__main__':
	hs_container = HashServiceContainer()
	hs = HashService(hs_container)
	hs.app.run(host=hs.services_dir, port=hs.port, debug=True)
