from unittest import TestCase
from main import diff, clear_and_convert_to_int

class MainTest(TestCase):

	# def test_input_line1(self):
	# 	"""
	# 	Test input [N <= 10^5]
	# 	"""
	# 	self.fail()
	#
	# def test_input_line2(self):
	# 	"""
	# 	Test [K > 0 and K < 10^9]
	# 	Line not repeat a same number
	# 	"""
	# 	self.fail()

	def test_diff_basic(self):
		n,k = 5,2
		q = [1, 5, 3, 4, 2]
		res = diff(k, q)
		self.assertEquals(res, 3)

	def test_diff_10_num(self):
		n,k = 10, 1
		q = [63374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635, 491595254, 879792181, 1069262793]
		res = diff(k, q)
		self.assertEquals(res, 0)

	def test_input000(self):
		n,k = 10, 1
		q = [363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635, 491595254, 879792181, 1069262793]
		res = diff(k, q)
		self.assertEquals(res, 0)

	def test_clear_and_return_list(self):
		data_input = '7 4 13\n'
		output = clear_and_convert_to_int(data_input)
		self.assertEquals(len(output), 3)
		self.assertEquals(output[0], 7)
		self.assertEquals(output[1], 4)
		self.assertEquals(output[2], 13)



