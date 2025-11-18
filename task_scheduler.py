"""
Task Scheduler Module
Schedule Python scripts to run automatically
"""

import schedule
import time
import subprocess
import sys
from datetime import datetime
from pathlib import Path

class TaskScheduler:
    def __init__(self, script_path):
        self.script_path = Path(script_path)
        self.task_count = 0

        if not self.script_path.exists():
            print(f"❌ Script not found: {script_path}")
            sys.exit(1)

    def run_task(self):
        """Execute scheduled task"""
        self.task_count += 1
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f"\n{'='*60}")
        print(f"🚀 Running Task #{self.task_count}")
        print(f"⏰ Time: {timestamp}")
        print(f"{'='*60}\n")

        try:
            result = subprocess.run(
                [sys.executable, str(self.script_path)],
                capture_output=True,
                text=True,
                timeout=300
            )

            if result.stdout:
                print(result.stdout)

            if result.returncode == 0:
                print("\n✅ Task completed successfully")
            else:
                print(f"\n❌ Task failed with exit code {result.returncode}")
                if result.stderr:
                    print(f"Error: {result.stderr}")

        except subprocess.TimeoutExpired:
            print("⏱️  Task timeout after 5 minutes")
        except Exception as e:
            print(f"❌ Error: {e}")

    def setup_schedule(self, choice):
        """Setup schedule based on user choice"""
        print("\n⏰ TASK SCHEDULER\n")

        if choice == '1':
            minutes = int(input("Enter interval in minutes: ").strip() or "30")
            schedule.every(minutes).minutes.do(self.run_task)
            print(f"✅ Scheduled to run every {minutes} minutes")
        elif choice == '2':
            hours = int(input("Enter interval in hours: ").strip() or "1")
            schedule.every(hours).hours.do(self.run_task)
            print(f"✅ Scheduled to run every {hours} hours")
        elif choice == '3':
            time_str = input("Enter time (HH:MM format, 24-hour): ").strip() or "09:00"
            schedule.every().day.at(time_str).do(self.run_task)
            print(f"✅ Scheduled to run daily at {time_str}")
        elif choice == '4':
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            print("\nDays: 1=Monday, 2=Tuesday, ..., 7=Sunday")
            day_num = int(input("Choose day (1-7): ").strip() or "1")
            time_str = input("Enter time (HH:MM): ").strip() or "09:00"

            day = days[day_num - 1]
            getattr(schedule.every(), day).at(time_str).do(self.run_task)
            print(f"✅ Scheduled to run every {day.capitalize()} at {time_str}")

        print("\n⚙️  Scheduler running... (Press Ctrl+C to stop)\n")

        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\n🛑 Scheduler stopped")
            print(f"📊 Total tasks executed: {self.task_count}")
