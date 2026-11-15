import os
import urllib.request
import zipfile

# Define local directory and file paths
data_dir = "./data"
csv_filename = "Occupancy_Estimation.csv"
csv_path = os.path.join(data_dir, csv_filename)
zip_path = os.path.join(data_dir, "room_occupancy_estimation.zip")

# Official UCI dataset 864 zip URL
url = "https://archive.ics.uci.edu/static/public/864/room+occupancy+estimation.zip"

# 1. Check if the dataset already exists on your PC
if os.path.exists(csv_path):
    print(f"Dataset already exists locally at: {os.path.abspath(csv_path)}")
else:
    # 2. Download and extract if it does not exist
    print("Dataset not found locally. Downloading from UCI Repository...")
    os.makedirs(data_dir, exist_ok=True)
    
    # Download the zip file
    urllib.request.urlretrieve(url, zip_path)
    print("Download complete. Extracting files...")
    
    # Extract the CSV file
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(data_dir)
        
    # Remove the temporary zip file
    os.remove(zip_path)
    print(f"Dataset successfully saved to: {os.path.abspath(csv_path)}")