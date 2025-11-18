"""
Simple test script for Task Scheduler
Ye script scheduler ke saath test karne ke liye hai
"""

from datetime import datetime

def main():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n{'='*50}")
    print(f"✅ Test Script Executed Successfully!")
    print(f"⏰ Time: {timestamp}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()
