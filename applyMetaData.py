from exif import Image
import csv

headers = []
rows = [][]

with open(csvProperties.csv, 'r') as csvProperties:
	reader = csv.DictReader(file)
	headers = reader.read()
	for index, row in reader:
		for value in row:
			rows[index][


with open("pics/000016170002.jpg", "rb") as photo1File:
	photo1 = Image(photo1File)

with open("pics/000016170003.jpg", "rb") as photo2File:
	photo2 = Image(photo2File)


	allPhotos = [photo1, photo2]


	for index, image in enumerate(allPhotos):
		
		if image.has_exif:
			image.make = 
