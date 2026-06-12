import smtplib
from email.mime.text import MIMEText
from email.header import Header

SMTP_SERVER = "邮箱域名服务.xxx.com"
SMTP_PORT = 25
SMTP_USER = "发件人@xxx.com"
SMTP_PASSWORD = "邮箱密码"

def send_text_email(from_email, to_emails, subject, body):
    server = None
    try:
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = from_email
        msg['To'] = ', '.join(to_emails)
        msg['Subject'] = Header(subject, 'utf-8')
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        
        if SMTP_USER and SMTP_PASSWORD:
            server.login(SMTP_USER, SMTP_PASSWORD)
        
        server.sendmail(from_email, to_emails, msg.as_string())
        
        print("纯文本邮件发送成功！")
        return True
        
    except Exception as e:
        print(f"发送失败：{str(e)}")
        return False
        
    finally:
        if server:
            try:
                server.quit()
            except:
                pass

send_text_email(
    from_email="发件人@xxx.com",
    to_emails=["收件人@qq.com"],
    subject="服务器状态通知",
    body="服务器运行正常，CPU使用率15%，内存使用率30%。"
)