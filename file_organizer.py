"""
File Organizer Module
Organize files by extension, date, or size
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

class FileOrganizer:
    def __init__(self, source_dir, dest_dir):
        self.source_dir = Path(source_dir)
        self.dest_dir = Path(dest_dir)

        self.categories = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
            'Code': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.php', '.json'],
            'Executables': ['.exe', '.msi', '.apk', '.deb', '.rpm', '.dmg'],
            'Others': []
        }

    def create_directories(self):
        """Create category directories"""
        for category in self.categories.keys():
            category_path = self.dest_dir / category
            category_path.mkdir(parents=True, exist_ok=True)

    def get_category(self, file_extension):
        """Get file category by extension"""
        for category, extensions in self.categories.items():
            if file_extension.lower() in extensions:
                return category
        return 'Others'

    def organize_by_extension(self):
        """Organize files by extension"""
        if not self.source_dir.exists():
            print(f"❌ Source directory not found: {self.source_dir}")
            return

        self.create_directories()
        files_moved = 0

        for file_path in self.source_dir.iterdir():
            if file_path.is_file():
                category = self.get_category(file_path.suffix)
                dest_folder = self.dest_dir / category

                try:
                    shutil.move(str(file_path), str(dest_folder / file_path.name))
                    print(f"✓ Moved: {file_path.name} → {category}")
                    files_moved += 1
                except Exception as e:
                    print(f"❌ Error moving {file_path.name}: {e}")

        print(f"\n✅ Organized {files_moved} files!")

    def organize_by_date(self):
        """Organize files by date"""
        if not self.source_dir.exists():
            print(f"❌ Source directory not found: {self.source_dir}")
            return

        files_moved = 0
        for file_path in self.source_dir.iterdir():
            if file_path.is_file():
                mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                date_folder = mod_time.strftime('%Y-%m-%d')
                dest_folder = self.dest_dir / date_folder
                dest_folder.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.move(str(file_path), str(dest_folder / file_path.name))
                    print(f"✓ Moved: {file_path.name} → {date_folder}")
                    files_moved += 1
                except Exception as e:
                    print(f"❌ Error: {e}")

        print(f"\n✅ Organized {files_moved} files by date!")

    def organize_by_size(self):
        """Organize files by size"""
        if not self.source_dir.exists():
            print(f"❌ Source directory not found: {self.source_dir}")
            return

        size_categories = {
            'Small (< 1MB)': 1024 * 1024,
            'Medium (1-10MB)': 10 * 1024 * 1024,
            'Large (10-100MB)': 100 * 1024 * 1024,
            'Very Large (> 100MB)': float('inf')
        }

        for category in size_categories.keys():
            (self.dest_dir / category).mkdir(parents=True, exist_ok=True)

        files_moved = 0
        for file_path in self.source_dir.iterdir():
            if file_path.is_file():
                file_size = file_path.stat().st_size

                for category, max_size in size_categories.items():
                    if file_size < max_size:
                        dest_folder = self.dest_dir / category
                        try:
                            shutil.move(str(file_path), str(dest_folder / file_path.name))
                            size_mb = file_size / (1024 * 1024)
                            print(f"✓ Moved: {file_path.name} ({size_mb:.2f}MB) → {category}")
                            files_moved += 1
                        except Exception as e:
                            print(f"❌ Error: {e}")
                        break

        print(f"\n✅ Organized {files_moved} files by size!")
