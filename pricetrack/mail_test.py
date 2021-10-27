from scrapy.mail import MailSender
mailer = MailSender()
# also smtplib would work 


#mailer = MailSender.from_settings(settings)
mailer.send(to=[""], subject="test subject", body="Some body")#, cc=["another@example.com"])
