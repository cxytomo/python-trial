database = [
	["tomo","havefun"],
	["ray","lovedog"],
	["mulan","120254"],
	["yurong","xiaoke"],
]
name =raw_input("userName: ")
pwd = raw_input("password:")
if ([name,pwd] in database): 
	print "welcome back " + name
else: 
	print "The username or password you entered is incorrect."