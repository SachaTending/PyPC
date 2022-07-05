from . import BIOSFIRMWARE
import threading, glob, sys

osscancomplete = False
osscanresult = ""
osscanerrorcode = "print('ERROR 500\\nOS Has been crashed!\\nPlease check OS crash code!')"

def osloader():
	def osscan():
		global osscancomplete
		global osscanresult
		disks = glob.glob("disks/*")
		for i in disks:
			try:
				file = open(i + "/mbr.py")
				osscanresult = file.read()
				file.close()
			except:
				print(f"...{i[6:]} Not contains mbr...", end="")
		if osscanresult == "":
			osscanresult = 'print("\\nERROR 404\\nNo OSes founded\\nPlease restart script\\r\\r\\r")'
		osscancomplete = True
	th = threading.Thread(target=osscan)
	th.start()
	sys.stdout.write("Scanning for OSes")
	while osscancomplete == False:
		sys.stdout.flush()
		sys.stdout.write("....")
	print('')
	try:
		exec(osscanresult)
	except Exception as e:
		print(f"OS CRASH CODE: {e}")
		exec(osscanerrorcode)

def run(osloader=osloader):
	BIOSFIRMWARE.bios(osloader)