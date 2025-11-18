#!/usr/bin/env python3
"""
Task Automation Hub - Python Edition
Professional automation toolkit for everyday tasks
Author: Auto-generated
Date: 2025-11-19
"""

import sys
import os
from pathlib import Path

# Add modules to path
sys.path.append(str(Path(__file__).parent / 'modules'))

from file_organizer import FileOrganizer
from email_sender import EmailAutomation
from web_scraper import WebScraper
from system_monitor import SystemMonitor
from backup_manager import BackupManager
from task_scheduler import TaskScheduler

class TaskAutomationHub:
    def __init__(self):
        self.version = "1.0.0"
        self.tasks = {
            '1': ('File Organizer', self.run_file_organizer),
            '2': ('Email Automation', self.run_email_automation),
            '3': ('Web Scraper', self.run_web_scraper),
            '4': ('System Monitor', self.run_system_monitor),
            '5': ('Backup Manager', self.run_backup_manager),
            '6': ('Task Scheduler', self.run_task_scheduler),
            '0': ('Exit', self.exit_app)
        }

    def display_banner(self):
        """Display application banner"""
        banner = f"""
╔══════════════════════════════════════════════════════════╗
║        🤖 TASK AUTOMATION HUB v{self.version}              ║
║        Professional Python Automation Toolkit            ║
╚══════════════════════════════════════════════════════════╝
        """
        print(banner)

    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("📋 AVAILABLE AUTOMATION TASKS:")
        print("="*60)
        for key, (name, _) in self.tasks.items():
            icon = '🚪' if key == '0' else '📁' if key == '1' else '📧' if key == '2' else '🌐' if key == '3' else '💻' if key == '4' else '💾' if key == '5' else '⏰'
            print(f"  [{key}] {icon} {name}")
        print("="*60)

    def run_file_organizer(self):
        """File organization automation"""
        print("\n" + "="*60)
        print("📁 FILE ORGANIZER")
        print("="*60)

        source = input("\nEnter source directory path: ").strip()
        dest = input("Enter destination directory path: ").strip()

        print("\nOrganization type:")
        print("  [1] By Extension")
        print("  [2] By Date")
        print("  [3] By Size")
        org_type = input("Choose (1-3): ").strip()

        organizer = FileOrganizer(source, dest)

        if org_type == '1':
            organizer.organize_by_extension()
        elif org_type == '2':
            organizer.organize_by_date()
        elif org_type == '3':
            organizer.organize_by_size()
        else:
            print("❌ Invalid choice")

    def run_email_automation(self):
        """Email automation"""
        print("\n" + "="*60)
        print("📧 EMAIL AUTOMATION")
        print("="*60)

        print("\nSMTP Servers:")
        print("  [1] Gmail (smtp.gmail.com)")
        print("  [2] Outlook (smtp-mail.outlook.com)")
        print("  [3] Yahoo (smtp.mail.yahoo.com)")
        print("  [4] Custom")

        choice = input("Choose SMTP server (1-4): ").strip()
        servers = {
            '1': ('smtp.gmail.com', 587),
            '2': ('smtp-mail.outlook.com', 587),
            '3': ('smtp.mail.yahoo.com', 587)
        }

        if choice in servers:
            smtp_server, smtp_port = servers[choice]
        else:
            smtp_server = input("Enter SMTP server: ").strip()
            smtp_port = int(input("Enter SMTP port: ").strip())

        sender = input("\nYour email: ").strip()
        import getpass
        password = getpass.getpass("Your password/app password: ")

        recipients = input("Recipient email(s) (comma-separated): ").strip().split(',')
        recipients = [r.strip() for r in recipients]

        subject = input("Email subject: ").strip()
        print("Email body (type 'END' on new line to finish):")
        body_lines = []
        while True:
            line = input()
            if line == 'END':
                break
            body_lines.append(line)
        body = '\n'.join(body_lines)

        email_bot = EmailAutomation(smtp_server, smtp_port, sender, password)
        email_bot.send_email(recipients, subject, body)

    def run_web_scraper(self):
        """Web scraping automation"""
        print("\n" + "="*60)
        print("🌐 WEB SCRAPER")
        print("="*60)

        url = input("\nEnter target URL: ").strip()

        print("\nData to extract:")
        print("  [1] All text content")
        print("  [2] Headings (h1-h6)")
        print("  [3] All links")
        print("  [4] Images")
        print("  [5] Tables")
        print("  [6] Custom CSS selector")

        choice = input("Choose (1-6): ").strip()

        scraper = WebScraper(url)
        if not scraper.fetch_page():
            return

        css_selector = None
        if choice == '6':
            css_selector = input("Enter CSS selector: ").strip()

        print("\nOutput format:")
        print("  [1] CSV")
        print("  [2] JSON")
        print("  [3] Text")
        format_choice = input("Choose (1-3): ").strip()
        output_format = {'1': 'csv', '2': 'json', '3': 'txt'}.get(format_choice, 'txt')

        scraper.scrape_and_save(choice, css_selector, output_format)

    def run_system_monitor(self):
        """System monitoring"""
        print("\n" + "="*60)
        print("💻 SYSTEM MONITOR")
        print("="*60)

        cpu_threshold = int(input("\nCPU alert threshold (%): ").strip() or "80")
        ram_threshold = int(input("RAM alert threshold (%): ").strip() or "85")
        interval = int(input("Monitoring interval (seconds): ").strip() or "60")

        print("\nAlert method:")
        print("  [1] Console output")
        print("  [2] Log to file")
        alert_choice = input("Choose (1-2): ").strip()
        alert_method = 'file' if alert_choice == '2' else 'console'

        monitor = SystemMonitor(cpu_threshold, ram_threshold, alert_method, interval)
        monitor.monitor()

    def run_backup_manager(self):
        """Backup management"""
        print("\n" + "="*60)
        print("💾 BACKUP MANAGER")
        print("="*60)

        source = input("\nSource directory to backup: ").strip()
        dest = input("Backup destination: ").strip()

        print("\nBackup type:")
        print("  [1] Full backup")
        print("  [2] Incremental (only changes)")
        print("  [3] Mirror sync")
        backup_choice = input("Choose (1-3): ").strip()
        backup_type = {'1': 'full', '2': 'incremental', '3': 'mirror'}.get(backup_choice, 'full')

        print("\nCompression:")
        print("  [1] ZIP")
        print("  [2] TAR.GZ")
        print("  [3] No compression")
        comp_choice = input("Choose (1-3): ").strip()
        compression = {'1': 'zip', '2': 'tar', '3': 'none'}.get(comp_choice, 'zip')

        retention = int(input("\nRetention (days, 0 for keep all): ").strip() or "30")

        manager = BackupManager(source, dest, compression, retention)
        manager.run_backup(backup_type)

    def run_task_scheduler(self):
        """Task scheduler"""
        print("\n" + "="*60)
        print("⏰ TASK SCHEDULER")
        print("="*60)

        script_path = input("\nPython script to schedule: ").strip()

        print("\nSchedule type:")
        print("  [1] Every X minutes")
        print("  [2] Every X hours")
        print("  [3] Daily at specific time")
        print("  [4] Weekly on specific day")

        choice = input("Choose (1-4): ").strip()

        scheduler = TaskScheduler(script_path)
        scheduler.setup_schedule(choice)

    def exit_app(self):
        """Exit application"""
        print("\n👋 Thank you for using Task Automation Hub!")
        print("Visit: github.com/yourusername/task-automation-hub\n")
        sys.exit(0)

    def run(self):
        """Main application loop"""
        self.display_banner()

        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip()

            if choice in self.tasks:
                _, task_func = self.tasks[choice]
                try:
                    task_func()
                    input("\n✅ Press Enter to continue...")
                except KeyboardInterrupt:
                    print("\n\n⚠️  Task interrupted by user")
                    input("Press Enter to continue...")
                except Exception as e:
                    print(f"\n❌ Error: {e}")
                    input("Press Enter to continue...")
            else:
                print("\n❌ Invalid choice! Please try again.")

def main():
    app = TaskAutomationHub()
    app.run()

if __name__ == "__main__":
    main()
