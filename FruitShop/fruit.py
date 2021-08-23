from frdict import fruits

class Fruit:
	def __init__(self, serial_no = 0, name = "", rate = 0, imp_from = "", imp_date = "", buy_price = ""):
		self.serial_no = serial_no
		self.name = name
		self.rate = rate
		self.imp_from = imp_from
		self.imp_date =  imp_date
		self.buy_price = buy_price
	def set_name(self,name):
		self.name = name
		return "Name assigned Successfully"
	def set_rate(self,rate):
		self.rate = rate
		return "Rate assigned Successfully"
	def set_imp_from(self,imp_from):
		self.imp_from = imp_from
		return "imp_from assigned Successfully"
	def set_imp_date(self,imp_date):
		self.imp_date = imp_date
		return "imp_date assigned Successfully"
