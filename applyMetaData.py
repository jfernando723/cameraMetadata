from exif import Image
from os import listdir, rename
from os.path import isfile, join
from geopy import Point
import csv


oldFileName = []
newFileName = []
csvDataList = []

with open("csvProperties.csv", 'r') as csvProperties:
    reader = csv.DictReader(csvProperties)
    csvDataList = list(reader)

picFiles = [f for f in listdir("pics/") if isfile(join("pics/", f))]
picFiles = sorted(picFiles)

for photoIndex, pic in enumerate(picFiles):
    with open("pics/"+pic, "rb") as photoFile:
        photo = Image(photoFile)

        if photo.has_exif:  # Check if EXIF data exists
            exif_data = dir(photo)

            if("gps_latitude" in reader.fieldnames and "gps_longitude" in reader.fieldnames
                and csvDataList[photoIndex].get("gps_latitude") != "" and csvDataList[photoIndex].get("gps_longitude") != ""):
                try:
                    abs_lat = abs(float(csvDataList[photoIndex].get("gps_latitude")))
                    print("abs_lat: " + str(abs_lat))
                    lat_dir = 'N' if float(csvDataList[photoIndex].get("gps_latitude")) >= 0 else 'S'
                    print("lat_dir: " + str(lat_dir))
                    abs_long = abs(float(csvDataList[photoIndex].get("gps_longitude")))
                    print("abs_long: " + str(abs_long))
                    lon_dir = 'E' if float(csvDataList[photoIndex].get("gps_longitude")) >= 0 else 'W'
                    print("lon_dir: " + str(lon_dir))
                    photo.set("gps_latitude", abs_lat)
                    photo.set("gps_latitude_ref", lat_dir)
                    photo.set("gps_longitude", abs_long)
                    photo.set("gps_longitude_ref", lon_dir)
                except Exception as e:
                    print(f"Error creating point: {e}")
            else:
                print("configuration csv doesn't have 'gps_latitude' and 'gps_longitude', which is like, fine,")


            for headerIndex, header in enumerate(reader.fieldnames):
                if(header == "gps_latitude" or header == "gps_longitude"):
                    continue
                headerValue = str(csvDataList[photoIndex].get(header))
                try:
                    photo.set(header, str(headerValue))  # Set the tag with the new value
                except Exception as e:
                    print(f"Error setting {header}: {e}")
        else:
            print("No EXIF data found in the image.")


