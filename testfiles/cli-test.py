import subprocess

f=open("cli-test-rslt.txt","w+")

#Expected Flag Validation (Testing Established Flags)
cmds = ["-h","--help","-n NEW","--new NEW","-S NEW","--startserver NEW","b NEW","--build NEW","-bs NEW"]

for i in cmds:
	try:
		subprocess.check_call("python3 pssg.py "+str(i), shell=True)
	except subprocess.CalledProcessError:
		pass


#Unexpected Flag Checker (Only h, &, and s should show)
for i in range(32,127):
	try:
		subprocess.check_call("python3 pssg.py -"+chr(i), shell=True)
	except subprocess.CalledProcessError:
		pass
	else:
		print("Valid: "+chr(i),file=f)

f.close()
