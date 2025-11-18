"""
Backup Manager Module
Create and manage backups with compression
"""

import shutil
from pathlib import Path
from datetime import datetime, timedelta
import zipfile
import tarfile

class BackupManager:
    def __init__(self, source_dir, backup_dir, compression_type, retention_days):
        self.source_dir = Path(source_dir)
        self.backup_dir = Path(backup_dir)
        self.compression_type = compression_type
        self.retention_days = retention_days

        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def get_backup_name(self):
        """Generate backup name"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return f"backup_{timestamp}"

    def create_zip_backup(self, backup_path):
        """Create ZIP backup"""
        print("📦 Creating ZIP backup...")
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in self.source_dir.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(self.source_dir.parent)
                    zipf.write(file_path, arcname)
                    print(f"  ✓ Added: {file_path.name}")

        print(f"\n✅ Backup created: {backup_path}")
        print(f"📊 Size: {backup_path.stat().st_size / (1024**2):.2f} MB")

    def create_tar_backup(self, backup_path):
        """Create TAR.GZ backup"""
        print("📦 Creating TAR.GZ backup...")
        with tarfile.open(backup_path, 'w:gz') as tar:
            tar.add(self.source_dir, arcname=self.source_dir.name)

        print(f"\n✅ Backup created: {backup_path}")
        print(f"📊 Size: {backup_path.stat().st_size / (1024**2):.2f} MB")

    def create_uncompressed_backup(self, backup_path):
        """Create uncompressed backup"""
        print("📦 Creating uncompressed backup...")
        shutil.copytree(self.source_dir, backup_path)

        file_count = sum(1 for _ in backup_path.rglob('*') if _.is_file())
        print(f"\n✅ Backup created: {backup_path}")
        print(f"📊 Files copied: {file_count}")

    def create_full_backup(self):
        """Create full backup"""
        backup_name = self.get_backup_name()

        if self.compression_type == 'zip':
            backup_path = self.backup_dir / f"{backup_name}.zip"
            self.create_zip_backup(backup_path)
        elif self.compression_type == 'tar':
            backup_path = self.backup_dir / f"{backup_name}.tar.gz"
            self.create_tar_backup(backup_path)
        else:
            backup_path = self.backup_dir / backup_name
            self.create_uncompressed_backup(backup_path)

        return backup_path

    def clean_old_backups(self):
        """Clean old backups"""
        if self.retention_days == 0:
            print("\n♾️  Retention: Keep all backups")
            return

        print(f"\n🧹 Cleaning backups older than {self.retention_days} days...")
        cutoff_date = datetime.now() - timedelta(days=self.retention_days)

        removed = 0
        for backup in self.backup_dir.glob('backup_*'):
            backup_time = datetime.fromtimestamp(backup.stat().st_mtime)
            if backup_time < cutoff_date:
                if backup.is_dir():
                    shutil.rmtree(backup)
                else:
                    backup.unlink()
                print(f"  🗑️  Removed: {backup.name}")
                removed += 1

        print(f"✅ Cleaned {removed} old backup(s)")

    def run_backup(self, backup_type):
        """Run backup process"""
        print(f"\n📂 Source: {self.source_dir}")
        print(f"📂 Destination: {self.backup_dir}\n")

        if not self.source_dir.exists():
            print(f"❌ Source directory not found!")
            return

        if backup_type == 'full' or backup_type == 'mirror':
            self.create_full_backup()
        elif backup_type == 'incremental':
            # Simplified incremental
            backups = list(self.backup_dir.glob('backup_*'))
            if not backups:
                print("ℹ️  No previous backup found. Creating full backup...")
                self.create_full_backup()
            else:
                self.create_full_backup()

        self.clean_old_backups()
