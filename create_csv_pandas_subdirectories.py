import csv
from datetime import date
import glob
import os
import pandas as pd

# CREATE NEW CSV OF CONCATENATED PROOFS FROM EACH INDIVIDUAL CSV FILE

todays_date = str(date.today())

descriptor = input("Please enter a one word descriptor you would like to add to your filename. (If you would not like to add a descriptor, hit ENTER): ")

newfilename = "ProofMode_Collection_" + todays_date + "_" + descriptor + ".csv"

header = ['File Hash SHA256', 'Locale', 'SafetyCheckCtsMatch',
       'Location.Provider', 'IPv6', 'IPv4', 'Location.Accuracy',
       'Location.Latitude', 'Language', 'NetworkType', 'Network',
       'Manufacturer', 'DataType', 'Hardware', 'ScreenSize', 'Wifi MAC',
       'Notes', 'DeviceID', 'Location.Longitude', 'Location.Bearing',
       'SafetyCheckBasicIntegrity', 'Location.Time', 'File Modified',
       'CellInfo', 'SafetyCheck', 'Location.Altitude', 'SafetyCheckTimestamp',
       'Proof Generated', 'File Path', 'Location.Speed', 'Unnamed: 30']

with open(newfilename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(header)

# READ IN FILES

desired_date = input('What is the date for the files? Enter in YYYY-MM-DD format: ')
name_of_download = input('Type in the exact name of the folder you downloaded: ')
PATH = 'ProofModeFiles\\' + desired_date + '\\' + name_of_download
EXT = '.csv'
separator = ','

## READ IN NEW PROOF

from csv import reader

# for proof_file in glob.glob(folder_name + "\\*" + file_type):

for path, subdir, files in os.walk(PATH):
    print("Path: ", path)
    print("Subdir: ", subdir)
    print("Files: ", files)
    for proof_file in glob.glob(path + "\\*" + EXT):
        print("Hello World")
        current_proof = open(proof_file, newline='')
        current_proof_df = pd.read_csv(current_proof)
        second_row = current_proof_df.iloc[0 , :]

        with open(newfilename, 'a+', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(second_row)