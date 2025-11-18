"""
System Monitor Module
Monitor CPU, RAM, Disk, and Network usage
"""

import psutil
import time
from datetime import datetime
import platform

class SystemMonitor:
    def __init__(self, cpu_threshold, ram_threshold, alert_method, interval):
        self.cpu_threshold = cpu_threshold
        self.ram_threshold = ram_threshold
        self.alert_method = alert_method
        self.interval = interval
        self.log_file = f"system_monitor_{datetime.now().strftime('%Y%m%d')}.log"

    def get_system_info(self):
        """Get system information"""
        return {
            'platform': platform.system(),
            'processor': platform.processor(),
            'ram_total': f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
        }

    def get_cpu_usage(self):
        """Get CPU usage"""
        return psutil.cpu_percent(interval=1)

    def get_ram_usage(self):
        """Get RAM usage"""
        memory = psutil.virtual_memory()
        return {
            'percent': memory.percent,
            'used': f"{memory.used / (1024**3):.2f} GB",
            'available': f"{memory.available / (1024**3):.2f} GB",
            'total': f"{memory.total / (1024**3):.2f} GB"
        }

    def get_disk_usage(self):
        """Get disk usage"""
        partitions = []
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                partitions.append({
                    'device': partition.device,
                    'total': f"{usage.total / (1024**3):.2f} GB",
                    'used': f"{usage.used / (1024**3):.2f} GB",
                    'free': f"{usage.free / (1024**3):.2f} GB",
                    'percent': usage.percent
                })
            except PermissionError:
                continue
        return partitions

    def log_message(self, message):
        """Log message"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}\n"

        if self.alert_method == 'file':
            with open(self.log_file, 'a') as f:
                f.write(log_entry)

        print(log_entry.strip())

    def check_thresholds(self, cpu_usage, ram_usage):
        """Check thresholds"""
        alerts = []

        if cpu_usage > self.cpu_threshold:
            alerts.append(f"⚠️  CPU ALERT: {cpu_usage}% (Threshold: {self.cpu_threshold}%)")

        if ram_usage > self.ram_threshold:
            alerts.append(f"⚠️  RAM ALERT: {ram_usage}% (Threshold: {self.ram_threshold}%)")

        return alerts

    def monitor(self):
        """Main monitoring loop"""
        print("\n💻 SYSTEM MONITOR - Starting...\n")

        sys_info = self.get_system_info()
        print(f"System: {sys_info['platform']} | RAM: {sys_info['ram_total']}")
        print(f"Processor: {sys_info['processor']}\n")
        print("⚙️  Monitoring... (Press Ctrl+C to stop)\n")

        try:
            while True:
                timestamp = datetime.now().strftime('%H:%M:%S')

                cpu = self.get_cpu_usage()
                ram = self.get_ram_usage()

                print(f"[{timestamp}] CPU: {cpu}% | RAM: {ram['percent']}% ({ram['used']}/{ram['total']})")

                alerts = self.check_thresholds(cpu, ram['percent'])
                for alert in alerts:
                    self.log_message(alert)

                if not alerts:
                    print("  ✅ All systems normal")

                time.sleep(self.interval)

        except KeyboardInterrupt:
            print("\n\n🛑 Monitoring stopped")
