import os

def find_large_files(start_folder, size_limit_mb=100):
    size_limit_bytes = size_limit_mb * 1024 * 1024

    for foldername, subfolders, filenames in os.walk(start_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > size_limit_bytes:
                    print(f"{os.path.abspath(file_path)}  -->  {file_size / (1024*1024):.2f} MB")
            except FileNotFoundError:
                pass  # skips files that disappear during scan

# Example usage
folder_to_scan = r"D:\"
find_large_files(folder_to_scan)
