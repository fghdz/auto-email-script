
# Python 自动邮件发送脚本

支持纯文本和HTML格式，适配25端口，包含宝塔面板计划任务教程。

## 功能特点

- ✅ 纯文本邮件发送
- ✅ HTML邮件发送
- ✅ 支持25端口
- ✅ 自定义发件人名称
- ✅ 完整的异常处理
- ✅ 宝塔面板计划任务集成

## 快速开始

### 1. 修改配置

编辑脚本文件，修改SMTP配置：

```python
SMTP_SERVER = "smtp.example.com"  # SMTP服务器地址
SMTP_PORT = 25                     # SMTP端口
SMTP_USER = "your_email@example.com"      # 登录用户名
SMTP_PASSWORD = "your_password"            # 邮箱密码
```

### 2. 发送纯文本邮件

```python
python send_text_email.py
```

### 3. 发送HTML邮件

```python
python send_html_email.py
```

## 脚本文件

| 文件 | 说明 |
|------|------|
| `send_text_email.py` | 纯文本邮件脚本 |
| `send_html_email.py` | HTML邮件脚本 |

## 宝塔面板计划任务配置

1. 上传脚本到 `/www/wwwroot/email_scripts/`
2. 在宝塔面板添加计划任务
3. 选择「Shell脚本」，填写执行命令：

```bash
#!/bin/bash
cd /www/wwwroot/email_scripts
/usr/bin/python3 send_text_email.py
```

## SMTP服务器配置参考

| 邮箱服务商 | SMTP服务器 | 端口 |
|-----------|----------|------|
| 腾讯企业邮 | smtp.exmail.qq.com | 25 |
| 阿里云企业邮 | smtp.mxhichina.com | 25 |
| QQ邮箱 | smtp.qq.com | 25 |
| 163邮箱 | smtp.163.com | 25 |

## 注意事项

- 云服务器默认封禁25端口，可能需要申请解封或改用587端口
- 部分邮箱需要使用授权码而非登录密码
- `sendmail()` 第一个参数必须使用 `from_email`，不能用 `SMTP_USER`


```

这样你的 GitHub 仓库就创建好了。
