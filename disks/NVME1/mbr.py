print("Test error 500 code")
class TestError(Exception):
	def __init__(self, errcode, errtext):
		pass

raise TestError(500, "lol")