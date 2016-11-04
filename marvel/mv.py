import requests
import hashlib
import webbrowser


class Marvel(object):
	"""
	Esta clase consume el API de MArvel Comics
	"""

	def __init__(self):
		self.public_key = 'a21d0308bdc8c9a0b6f11b22eea16ac0'
		self.private_key = '0c832d15ef1d15d847f6bf5ded4ec34b74a98465'
		self.ts = '1'
		self.ha = hashlib.md5((self.ts+self.private_key+self.public_key).encode()).hexdigest()
		self.url = 'http://gateway.marvel.com/v1/public/'
		# Variables que voy ocupando
		self.personaje = ''

	def get_personaje(self,nombre):
		try:
			self.personaje = requests.get(
					self.url+'characters',
					params={
						'ts':self.ts,
						'apikey':self.public_key,
						'hash':self.ha,
						'name':nombre
					}).json()
			# print(self.personaje)
			description = self.personaje['data']['results'][0]['description']
			return description
		except:
			print('Escribe bien cabron')

	def get_imagen(self):
		# webbrowser.open(self.personaje['data']['results'][0]['thumbnail']['path']+'.'+self.personaje['data']['results'][0]['thumbnail']['extension'])
		return self.personaje['data']['results'][0]['thumbnail']['path']+'.'+self.personaje['data']['results'][0]['thumbnail']['extension']


