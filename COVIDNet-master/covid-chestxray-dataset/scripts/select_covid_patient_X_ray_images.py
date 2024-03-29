'''
This code finds all images of patients of a specified VIRUS and X-Ray view and stores selected image to an OUTPUT directory
+ It uses metadata.csv for searching and retrieving images name
+ Using ./images folder it selects the retrieved images and copies them in output folder
Code can be modified for any combination of selection of images
'''

import pandas as pd
import shutil
import os
# Selecciona toda la combina de pacientes con covid-19 mediante X-ray
# Select
virus = "COVID-19" # Virus que estamos buscando
x_ray_view = "PA" # vision de X-ray

metadata = "../metadata.csv" # Meta info
imageDir = "../images" # Directory of images
outputDir = '../output' # Output directory to store selected images

metadata_csv = pd.read_csv(metadata)

# loop over the rows of the COVID-19 data frame
for (i, row) in metadata_csv.iterrows():
	if row["finding"] != virus or row["view"] != x_ray_view:
		continue

	filename = row["filename"].split(os.path.sep)[-1]
	filePath = os.path.sep.join([imageDir, filename])
	shutil.copy2(filePath, outputDir)
