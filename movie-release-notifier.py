import requests
from bs4 import BeautifulSoup
import os

url = "https://www.spicinemas.in/coimbatore/now-showing"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("dt", {"class":"movie__name"})

for x in data:
	print x.text
	if "BAAGHI" in x.text:
		import smtplib 
		sub = "MOVIE RELEASED"
		content = "MOVIE has been released. \nGoto https://www.spicinemas.in/coimbatore/now-showing" 
		FROM = #your email here within " "
		TO = #your email here within " "
		mail = smtplib.SMTP ("smtp.gmail.com", 587) 
		mail.ehlo()
		mail.starttls()
		mail.login(FROM , #your password within " ")
		BODY = '\r\n'.join([
			'TO: %s' %TO,
			'FROM: %s' %FROM,
			'SUBJECT: %s' %sub,
			'',
			content])
		try:
			mail.sendmail (FROM , [TO] , BODY)
			print 'Email sent'
		except Exception, e:
			print 'Error. Could not send the email.'

		mail.close()
