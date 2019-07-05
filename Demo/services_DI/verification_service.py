import time
from flask import Flask
from flask import request
import requests

app = Flask(__name__)

class VerificationService():
	def __init__(self):
		self.app = app
		self.services_dir = '127.0.0.1'
		self.port = '5001'

	@app.route('/service', methods=['GET'])
	def service():
		return VerificationService.validate_clientId(request.args.get('client_id'))

	@staticmethod
	def validate_clientId(client_id):
		if client_id == 'A1':
			return '1'
		else:
			return '0'

	def get_service_dir(self, client_id):
		verification_dir = 'http://'
		verification_dir += self.services_dir
		verification_dir += ":"
		verification_dir += self.port
		verification_dir += '/service?client_id='
		verification_dir += str(client_id)
		print(verification_dir)
		return verification_dir
		
	def validate_credentials(self, client_id):
		service_dir = self.get_service_dir(client_id)
		print(service_dir)
		request_result = requests.get(service_dir)
		verification = int(request_result.text)
		return verification

if __name__ == '__main__':
	vs = VerificationService()
	vs.app.run(host=vs.services_dir, port=vs.port, debug=True)
