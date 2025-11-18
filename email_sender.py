"""
Email Automation Module
Send automated emails with attachments
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

class EmailAutomation:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_emails, subject, body, attachments=None):
        """Send email with optional attachments"""
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = ', '.join(recipient_emails)
            message['Subject'] = subject

            message.attach(MIMEText(body, 'plain'))

            if attachments:
                for file_path in attachments:
                    if Path(file_path).exists():
                        with open(file_path, 'rb') as attachment:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(attachment.read())
                            encoders.encode_base64(part)
                            part.add_header(
                                'Content-Disposition',
                                f'attachment; filename= {Path(file_path).name}'
                            )
                            message.attach(part)
                        print(f"✓ Attached: {Path(file_path).name}")

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)

            print(f"\n✅ Email sent to {len(recipient_emails)} recipient(s)!")
            return True

        except Exception as e:
            print(f"❌ Error sending email: {e}")
            return False
