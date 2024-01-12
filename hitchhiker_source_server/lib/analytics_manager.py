import os
import mimetypes
import hashlib
import time

class AnalyticsManager:
    def __init__(self, dir, max_storage_mb=1):
        self.dir = dir
        self.max_storage_mb = max_storage_mb

    def remove_old_files(self):
        print("Removing old files to limit storage to {} MB".format(self.max_storage_mb))

        # Get list of files with their paths and sizes
        files = [(file, os.path.join(self.dir, file), os.path.getsize(os.path.join(self.dir, file)))
                for file in self.list_of_files()]

        # Sort files by modification time, newest first
        files.sort(key=lambda x: os.path.getmtime(x[1]), reverse=True)

        # Calculate total size and remove files if necessary
        total_size = sum(file[2] for file in files)
        max_storage_bytes = self.max_storage_mb * 1024 * 1024

        for file, file_path, file_size in files:
            if total_size <= max_storage_bytes:
                break  # Stop if total size is within the limit
            try:
                self.remove_file(file)
                total_size -= file_size
                print(f"Removed file: {file}")
            except Exception as e:
                print(f"Error removing file: {e}")

        print("Old file removal complete.")

    def list_of_files(self):
        # List all files in the directory excluding '.' and '..'
        return [entry for entry in os.listdir(self.dir) if os.path.isfile(os.path.join(self.dir, entry))]

    def remove_file(self, filename):
        # Delete the specified file
        try:
            os.remove(os.path.join(self.dir, filename))
        except Exception as e:
            print(f"Error removing file: {e}")

    def details(self, filename):
        # Get details of the specified file
        try:
            file_path = os.path.join(self.dir, filename)
            file_type, _ = mimetypes.guess_type(file_path)
            with open(file_path, 'rb') as file:
                blob = file.read()
            md5_hash = hashlib.md5(blob).hexdigest()
            return {
                'file_id': md5_hash,
                'file_name': filename,
                'type': file_type if file_type else 'unknown',
                'blob': blob
            }
        except Exception as e:
            print(f"Error getting file details: {e}")
            return None
