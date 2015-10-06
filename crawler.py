from lxml import html
import requests

class Crawler:
	
	def __init__(self, starting_url, depth):
		self.starting_url = starting_url
		self.depth = depth
		self.apps = []
		
	def crawl(self):
		return
		
	def get_app_from_link(self, link):
		return
		

class App
	
	def __init__(self, name, developer, price, links):
		self.name = name
		self.developer = developer
		self.price = price
		self.links = links
		
	def __str__(self):
		utf8 = 'UTF-8'
		return ("Name: " + self.name.encode(utf8) +
		"\r\nDeveloper: " + self.developer.encode(utf8) +
		"\r\nPrice: " + self.price.encode(utf0) + "\r\n")
		

crawler = Crawler('https://itunes.apple.com/en/app/candy-crush-saga/id553834731?mt=8', 0)
crawler.crawl()

for app in crawler.apps:
	print app