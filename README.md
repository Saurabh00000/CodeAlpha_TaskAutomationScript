# 🤖 Task Automation Hub

**Professional Python Automation Toolkit** - Apne daily tasks ko automate karein!

## ✨ Features

### 1. 📁 File Organizer
- Files ko automatically organize kare extension, date, ya size ke basis pe
- Downloads folder cleanup
- Smart categorization (Images, Documents, Videos, etc.)

### 2. 📧 Email Automation
- Bulk emails bhejein with attachments
- Gmail, Outlook, Yahoo support
- Scheduled email reminders
- Professional email templates

### 3. 🌐 Web Scraper
- Websites se data extract karein
- Product prices monitor karein
- News, articles scrape karein
- CSV, JSON, TXT output support

### 4. 💻 System Monitor
- Real-time CPU, RAM monitoring
- Disk space alerts
- Network statistics
- Custom threshold alerts

### 5. 💾 Backup Manager
- Automatic file backups
- ZIP/TAR.GZ compression
- Incremental backups
- Retention policy management

### 6. ⏰ Task Scheduler
- Scripts ko schedule karke run karein
- Daily, weekly, monthly scheduling
- Cron-like functionality
- Background execution

## 🚀 Installation

### Step 1: Python Install karein
```bash
# Windows pe Python 3.8+ chahiye
# Download from: https://www.python.org/downloads/
```

### Step 2: Dependencies Install karein
```bash
pip install -r requirements.txt
```

### Step 3: Run karein
```bash
python main.py
```

## 📖 Usage Examples

### File Organizer
```bash
# Main application run karein
python main.py

# Option [1] select karein
# Source folder: C:\Users\YourName\Downloads
# Destination: C:\Users\YourName\Organized
# Type: By Extension
```

### Email Automation
```bash
# Option [2] select karein
# SMTP: Gmail (option 1)
# Your email: your.email@gmail.com
# App Password enter karein (not regular password)
# Recipients: recipient1@email.com, recipient2@email.com
```

**Gmail App Password kaise banaye:**
1. Google Account settings me jaye
2. Security > 2-Step Verification enable karein
3. App Passwords banaye
4. "Mail" select karein
5. Generated password use karein

### Web Scraper
```bash
# Option [3] select karein
# URL: https://example.com
# Data type: Links (option 3)
# Format: JSON (option 2)
```

### System Monitor
```bash
# Option [4] select karein
# CPU threshold: 80%
# RAM threshold: 85%
# Interval: 60 seconds
# Ctrl+C press karke stop karein
```

### Backup Manager
```bash
# Option [5] select karein
# Source: C:\ImportantFiles
# Destination: D:\Backups
# Type: Full backup (option 1)
# Compression: ZIP (option 1)
# Retention: 30 days
```

### Task Scheduler
```bash
# Option [6] select karein
# Script path: C:\scripts\my_automation.py
# Schedule: Every 30 minutes (option 1)
# Background me run hoga
```

## 📁 Project Structure

```
task-automation-hub/
│
├── main.py                 # Main application entry point
├── modules/
│   ├── file_organizer.py   # File organization module
│   ├── email_sender.py     # Email automation module
│   ├── web_scraper.py      # Web scraping module
│   ├── system_monitor.py   # System monitoring module
│   ├── backup_manager.py   # Backup management module
│   └── task_scheduler.py   # Task scheduling module
│
├── requirements.txt        # Python dependencies
└── README.md              # Documentation (this file)
```

## 🔧 Configuration

### Gmail SMTP Settings
- Server: smtp.gmail.com
- Port: 587
- Security: TLS
- **Important**: App Password use karein, regular password nahi

### Outlook SMTP Settings
- Server: smtp-mail.outlook.com
- Port: 587
- Security: TLS

### Yahoo SMTP Settings
- Server: smtp.mail.yahoo.com
- Port: 587
- Security: TLS

## 💡 Tips & Best Practices

### File Organizer
- Pehle test folder pe try karein
- Important files ka backup rakhein
- Organize karne se pehle folder structure check karein

### Email Automation
- Gmail me 2-Step Verification enable karein
- App Password use karein (security ke liye)
- Test email pehle apne email pe bhejein

### Web Scraper
- Website ke robots.txt check karein
- Rate limiting use karein (zyada requests na bhejein)
- Legal content hi scrape karein

### System Monitor
- Background me run kar sakte hai
- Log files regularly check karein
- Thresholds apni system ke according set karein

### Backup Manager
- Regular backups schedule karein
- Multiple locations me backup rakhein
- Backup integrity verify karein

### Task Scheduler
- Scripts ko pehle manually test karein
- Error handling add karein scripts me
- Log files maintain karein

## 🐛 Troubleshooting

### Email nahi ja raha?
- App Password use kar rahe ho?
- 2-Step Verification enabled hai?
- Internet connection check karein
- SMTP settings verify karein

### Web Scraper fail ho raha?
- Internet connection check karein
- URL correct hai?
- Website accessible hai?
- Dependencies install hai?

### File Organizer error de raha?
- Path correct hai?
- Permissions check karein
- Disk space available hai?
- Special characters in path nahi hone chahiye

### System Monitor crash ho raha?
- psutil package installed hai?
- Admin/sudo permissions chahiye ho sakta hai
- Python version 3.8+ hai?

## 🔒 Security Notes

- Passwords ko code me hardcode na karein
- App Passwords use karein regular passwords ke bajaye
- Sensitive data ko encrypt karein
- Log files ko secure location me rakhein
- Scripts ko trusted sources se hi run karein

## 📝 Future Enhancements

- [ ] GUI interface (Tkinter/PyQt)
- [ ] Cloud backup support (Google Drive, Dropbox)
- [ ] Database integration
- [ ] Advanced scheduling (cron expressions)
- [ ] Email templates
- [ ] Notification system (SMS, Telegram)
- [ ] Multi-language support
- [ ] Web dashboard

## 🤝 Contributing

Contributions welcome hai! Pull requests bhej sakte ho.

## 📄 License

MIT License - Free to use and modify

## 👨‍💻 Author

**Task Automation Hub**
- GitHub: [Your GitHub Profile]
- Email: [Your Email]

## 🙏 Acknowledgments

- Python community
- Open source libraries ke maintainers
- All beta testers and contributors

## 📞 Support

Questions ya issues ke liye:
- GitHub Issues create karein
- Email karein
- Documentation padhein

---

**Happy Automating! 🚀**

_Apna time save karein, automation ko kaam karne do!_
