#!/usr/bin/env python3
"""
Scheduler for Automated Stock Rating System
Runs rating updates on a schedule
"""

import schedule
import time
from datetime import datetime
import subprocess
import sys
import os


class StockRatingScheduler:
    """Schedule automated stock rating updates"""

    def __init__(self):
        self.script_path = os.path.join(os.path.dirname(__file__), 'auto_stock_rater.py')

    def run_rating_update(self):
        """Execute the rating script"""
        print(f"\n{'='*80}")
        print(f"Scheduled Rating Update - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*80}\n")

        try:
            # Run the auto_stock_rater script
            result = subprocess.run(
                [sys.executable, self.script_path],
                capture_output=True,
                text=True
            )

            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)

            print(f"\n{'='*80}")
            print(f"Update Complete - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{'='*80}\n")

        except Exception as e:
            print(f"Error running scheduled update: {e}")

    def schedule_daily_updates(self, time_str: str = "09:30"):
        """Schedule daily updates at market open"""
        print(f"📅 Scheduling daily updates at {time_str} (market open)")
        schedule.every().day.at(time_str).do(self.run_rating_update)

    def schedule_weekly_updates(self, day: str = "monday", time_str: str = "09:30"):
        """Schedule weekly updates"""
        print(f"📅 Scheduling weekly updates on {day.capitalize()} at {time_str}")

        if day.lower() == "monday":
            schedule.every().monday.at(time_str).do(self.run_rating_update)
        elif day.lower() == "tuesday":
            schedule.every().tuesday.at(time_str).do(self.run_rating_update)
        elif day.lower() == "wednesday":
            schedule.every().wednesday.at(time_str).do(self.run_rating_update)
        elif day.lower() == "thursday":
            schedule.every().thursday.at(time_str).do(self.run_rating_update)
        elif day.lower() == "friday":
            schedule.every().friday.at(time_str).do(self.run_rating_update)

    def schedule_interval_updates(self, hours: int = 4):
        """Schedule updates every N hours"""
        print(f"📅 Scheduling updates every {hours} hours")
        schedule.every(hours).hours.do(self.run_rating_update)

    def run_scheduler(self):
        """Run the scheduler loop"""
        print("\n🤖 Stock Rating Scheduler Started")
        print("Press Ctrl+C to stop\n")

        # Run immediately on startup
        print("Running initial update...")
        self.run_rating_update()

        # Then run on schedule
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute


def main():
    """Main execution"""
    import argparse

    parser = argparse.ArgumentParser(description='Schedule automated stock rating updates')
    parser.add_argument('--mode', choices=['daily', 'weekly', 'interval', 'once'],
                       default='daily', help='Scheduling mode')
    parser.add_argument('--time', default='09:30', help='Time for daily/weekly updates (HH:MM)')
    parser.add_argument('--day', default='monday', help='Day for weekly updates')
    parser.add_argument('--hours', type=int, default=4, help='Hours for interval updates')

    args = parser.parse_args()

    scheduler = StockRatingScheduler()

    if args.mode == 'once':
        print("Running one-time update...")
        scheduler.run_rating_update()
    elif args.mode == 'daily':
        scheduler.schedule_daily_updates(args.time)
        scheduler.run_scheduler()
    elif args.mode == 'weekly':
        scheduler.schedule_weekly_updates(args.day, args.time)
        scheduler.run_scheduler()
    elif args.mode == 'interval':
        scheduler.schedule_interval_updates(args.hours)
        scheduler.run_scheduler()


if __name__ == "__main__":
    main()
