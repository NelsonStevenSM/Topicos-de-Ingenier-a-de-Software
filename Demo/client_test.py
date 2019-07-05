import requests
from sys import argv

class Client():
	def __init__(self, client_id, hash_dir):
		self.client_id = client_id
		self.hash_service = hash_dir

	def hash_string(self, string_to_hash):
		return self.apply_hash_service(string_to_hash)

	def apply_hash_service(self, string_to_hash):
		request_dir = 'http://' + self.hash_service + '/service' + '?client_id=' + str(self.client_id) + '&hash_string=' + string_to_hash

		result = requests.get(request_dir)
		print(result.text)

if __name__ == "__main__":
	services_dir = '127.0.0.1'
	hash_service_port = '5000' 
	user_id = argv[1]
	hashing_string = argv[2]
	c = Client(user_id, services_dir + ":" + hash_service_port)
	c.hash_string(hashing_string)

