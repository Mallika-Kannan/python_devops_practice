import os
import zipfile

def find_large_files(directory, size_limit):
    large_files = []
    for root, dirs, files in os.walk(directory):  # FIXED: dirs instead of dir
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.getsize(file_path) > size_limit:
                    large_files.append(file_path)
            except OSError:
                print(f"⚠️ Could not access {file_path}")
    return large_files


def zip_files(file_list, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in file_list:
            zipf.write(file, arcname=os.path.basename(file))
            print(f"✅ Added {file} to {output_zip}")


def main():
    directory = input("Enter directory path to scan: ").strip()
    size_in_mb = input("Enter minimum file size (in MB): ").strip()
    
    if not size_in_mb.isdigit():
        print("❌ Invalid size. Please enter a number.")
        return
    
    size_limit = int(size_in_mb) * 1024 * 1024
    print(f"\n🔍 Searching for files > {size_in_mb}MB in {directory}...\n")
    
    large_files = find_large_files(directory, size_limit)

    if not large_files:
        print("No large files found.")
    else:
        output_zip = "large_files_archive.zip"
        zip_files(large_files, output_zip)
        print(f"\n📦 Zipped {len(large_files)} files into {output_zip}")


if __name__ == "__main__":
    main()
