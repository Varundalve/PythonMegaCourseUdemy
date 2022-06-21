import smtplib

my_email = "udemystudent45@gmail.com"
password = "afnxrchxyhuwtxtj"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="testpython45@gmail.com",
                        msg="Subject:Hello !\n\n This is a test message.")
