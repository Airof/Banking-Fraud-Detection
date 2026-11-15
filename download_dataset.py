# download_dataset.py
import os
import sys
import urllib.request

DATA_DIR = "./data"
CSV_FILENAME = "creditcard.csv"
CSV_PATH = os.path.join(DATA_DIR, CSV_FILENAME)
DATASET_URL = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"


def show_progress(block_num, block_size, total_size):
    """Displays download progress in the terminal."""
    downloaded = block_num * block_size
    if total_size > 0:
        percent = min(100.0, downloaded * 100.0 / total_size)
        mb_downloaded = downloaded / (1024 * 1024)
        mb_total = total_size / (1024 * 1024)
        sys.stdout.write(
            f"\rDownloading: {percent:5.1f}% ({mb_downloaded:.1f} MB / {mb_total:.1f} MB)"
        )
        sys.stdout.flush()


def main():
    # 1. Check if the dataset already exists on the PC
    if os.path.exists(CSV_PATH):
        file_size_mb = os.path.getsize(CSV_PATH) / (1024 * 1024)
        print(f"Dataset already exists locally at: {os.path.abspath(CSV_PATH)} ({file_size_mb:.1f} MB)")
        return

    # 2. Download the dataset if it does not exist
    print("Dataset not found locally. Starting download...")
    os.makedirs(DATA_DIR, exist_ok=True)

    try:
        urllib.request.urlretrieve(DATASET_URL, CSV_PATH, reporthook=show_progress)
        print(f"\nDownload complete! Saved to: {os.path.abspath(CSV_PATH)}")
    except Exception as e:
        if os.path.exists(CSV_PATH):
            os.remove(CSV_PATH)
        print(f"\nDownload failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()