import time, sys

def bios(osloader):
	print("PyBIOS Version 1.0")
	print("Copyrights TendingStream73")
	print("If you need a support, use discord: TendingStream73#5806")

	for i in range(256):
		time.sleep(0.000001)
		print(f"Memory: {i}MB", end="\r")
	time.sleep(0.001)
	print("Memory: UNLIMITED", end="\r\n")
	time.sleep(1)
	for i in f"CPU(such as intrepretator): Python {sys.version}":
		time.sleep(0.0001)
		sys.stdout.write(i)
		sys.stdout.flush()
	print("")
	print("SSD NVME1: Samsung SUPER FAST SSD LIMITED EDITION 2956342985732489573 TB/SEC")
	print("HDD SATA1: Seagate Baracuda SUPER FAST HDD 430979376 MB/SEC")
	print("DVD SATA2: LG DVD-RW 999X Write/Read")
	print("SATA3: None")
	print("SATA4: None")
	print("SATA5: None")
	print("SATA6: None")
	print("GPU: NOVIDEO 5090 RTX SUPER GPU")
	for i in range(11):
		time.sleep(0.5)
		print("Loading os loader" + "."*i, end="\r")
	print()
	osloader()