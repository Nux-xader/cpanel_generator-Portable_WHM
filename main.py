import requests, random, sys, os

log_file = "log_portable_whm.txt"
headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36"}
subDo = [
	"orgfree.com", "6te.net", "ueuo.com", "eu5.org", "noads.biz", 
	"coolpage.biz", "freeoda.com", "freevar.com", "freetzi.com", "xp3.biz"
	]


class Whm:
	def __init__(self):
		self.templateResult = """
===============================================
Control Panel
Username : {}
Password : {}
===============================================
===============================================
FTP Account
FTP Server/Host: {}
FTP Login/Username: {}
FTP PassWord: {}
===============================================
"""
		try:
			self.sess = requests.Session()
			self.sess.get("https://freewebhostingarea.com")
		except:
			print(" [!] Please Check Your Internet Connection")
			sys.exit()

	def checkAvalibe(self, name, domain):
		dummy_sess = self.sess
		payload = {"thirdLevelDomain":name, "domain":domain, "action": "check_domain"}
		html = dummy_sess.post(
			"https://freewebhostingarea.com/cgi-bin/create_account.cgi", 
			data=payload, headers=headers).text
		if "Account already" in html:
			return False
		else:
			return True

	def checkAvalibe(self, email, domainName):
		dummy_sess = self.sess
		psswd = self.randomChar(random.randint(10, 16))
		payload = {
			"action": "validate", 
			"domainName": domainName, 
			"email": email, 
			"password": psswd, 
			"confirmPassword": psswd,
			"agree": "1"}
		html = dummy_sess.post(
			"https://newserv.freewha.com/cgi-bin/create_ini.cgi", 
			data=payload, headers=headers).text
		if "was successfully activated" in html:
			# usernameCP = html.split("<strong>Username:</strong>")[-1].split('<br>')[0].replace('\n', '')
			# passwordCP = html.split("<strong>Password:</strong>")[-1].split('</p>')[0].replace('\n', '')
			return self.templateResult.format(domainName, psswd, domainName, domainName, psswd)
		else:
			return False


	def randomChar(self, length, num=True):
		char = "qwertyuioplkjhgfdsazxcvbnmZXCVBNMLKJHGFDSAQWERTYUIOP"
		if num: char+="1234567890"
		return "".join([random.choice(char) for i in range(length)])



def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
 █▀█ █▀█ █▀█ ▀█▀ ▄▀█ █▄▄ █░░ █▀▀
 █▀▀ █▄█ █▀▄ ░█░ █▀█ █▄█ █▄▄ ██▄
 
 █░█░█ █░█ █▀▄▀█
 ▀▄▀▄▀ █▀█ █░▀░█  V1.0.0

 Contact         : https://wa.me/+6281251389915
 About Developer : https://github.com/Nux-xader
 ________________________________________________
""")

data = Whm().checkAvalibe("nuxxader", "eu5.org")
open('xx.html', 'w').write(data)