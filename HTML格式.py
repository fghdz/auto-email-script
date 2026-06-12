import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

SMTP_SERVER = "邮箱域名服务.xxx.com"
SMTP_PORT = 25
SMTP_USER = "发件人@xxx.com"
SMTP_PASSWORD = "邮箱密码"

def send_html_email(from_email, to_emails, subject, html_body):
    server = None
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = from_email
        msg['To'] = ', '.join(to_emails)
        msg['Subject'] = Header(subject, 'utf-8')
        
        text_part = MIMEText("您的邮件客户端不支持HTML格式。", 'plain', 'utf-8')
        html_part = MIMEText(html_body, 'html', 'utf-8')
        msg.attach(text_part)
        msg.attach(html_part)
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        
        if SMTP_USER and SMTP_PASSWORD:
            server.login(SMTP_USER, SMTP_PASSWORD)
        
        server.sendmail(from_email, to_emails, msg.as_string())
        
        print("HTML邮件发送成功！")
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

send_html_email(
    from_email="发件人@xxx.com",
    to_emails=["收件人@qq.com"],
    subject="服务器状态通知",
    html_body="""
    <html>
        <body>
            <h2>服务器状态通知</h2>
            <p>服务器运行正常</p>
            <p>CPU使用率：15%</p>
            <p>内存使用率：30%</p>
        </body>
    </html>
    """
)