import os
import shutil 

#NOTES TO SELF

#DOC NOTES

#need to double check exactly how setref / hdri / witcam is structured in final slates folder
#need to create raw / jpg file split for setref / hdri


#DOC NOTES
#please utilize this script with the folder structure created in dump.py
#make sure not to use unusual naming conventions such as including a "." in folder names

#global variables
slates_list = []


#functions

#checks if slate exists
def slate_exists(currentSlate, list_slates):

	slateExists = False

	for x in list_slates:

		if x == currentSlate:
			slateExists = True
			break
		else:
			continue

	return slateExists


#checks if file is .DS store
def DS_store(folder):

	if folder == ".DS_Store":
		return True
	else:
		return False
	
	


#gets slate from folder name
def get_slate(folder):
	slate = ""

	for x in folder:
		if(x != "_"):
			slate += x
		else:
			break

	return slate

def add_slate(slate):
	os.makedirs("sorted/slates/"+ slate)
	slates_list.append(slate)

def add_slate_check(slate, list_slates):
	#creates first slate, adds to slates list
	if not list_slates:
		add_slate(slate)

	else:
	#checks to see if slate exists, adds if not
		if not slate_exists(slate, list_slates):
			add_slate(slate)



def add_witcam_slate_check(slate, list_slates, camera, path):
	if not list_slates:
		add_witcam_slate(slate, list_slates, camera, path)

	else:
		if not slate_exists(slate, list_slates):
			add_witcam_slate(slate,list_slates, camera, path)

def add_witcam_slate(slate,list_slates, camera, path):
	list_slates.append(slate)
	os.mkdir(path + "/" + slate + "_witness_" + camera)

def add_subfolder_check(type_sort):
	if os.path.exists("sorted/slates/" + slate + "/" + type_sort):
		return
	else:
		os.makedirs("sorted/slates/" + slate + "/" + type_sort)


def sort_file_type(path):
	file_list = os.listdir(path)

	os.makedirs(path + "/jpg")
	os.makedirs(path + "/raw")

	for file in file_list:
		if not DS_store(file):

			fileName, fileExt = os.path.splitext(file)
	
			if fileExt == ".jpg" or fileExt == ".jpeg" or fileExt == ".JPG" or fileExt == ".JPEG" :
				shutil.move(path + "/" + file , path + "/jpg")
			
			else:
				shutil.move(path + "/" + file , path + "/raw")
	





#create parent slate folder
os.makedirs("sorted/slates")

#sort datasheets

datasheet_path = "unsorted/slates"

datasheet_obj = os.scandir(datasheet_path)

for entry in datasheet_obj:

	if not DS_store(entry.name):
		slate = entry.name

		add_slate_check(slate, slates_list)

		add_subfolder_check("wrangler_sheets")


		shutil.move(datasheet_path + "/" + slate, "sorted/slates/" + slate + "/wrangler_sheets" )

print("Datasheets sorted")	

#sort setref

setref_path = "unsorted/setref"

setref_obj = os.scandir(setref_path)

#PUT CHECK HERE TO SEE IF THERE IS ANYTHING IN FOLDER

for entry in setref_obj:
	if not DS_store(entry.name):
		folder = entry.name

		#find slate token
		slate = ""

		
		slate = get_slate(folder)

		add_slate_check(slate, slates_list)

		add_subfolder_check("setref")

		sort_file_type(setref_path + "/" + folder)

		shutil.move(setref_path + "/" + folder, "sorted/slates/" + slate + "/setref" )

print("setref sorted")

#sort hdri

hdri_path = "unsorted/hdri"

hdri_obj = os.scandir(hdri_path)

#PUT CHECK HERE TO SEE IF THERE IS ANYTHING IN FOLDER

for entry in hdri_obj:



	if not DS_store(entry.name):
		folder = entry.name

		#find slate token
		slate = ""
	
		slate = get_slate(folder)

		add_slate_check(slate, slates_list)

		add_subfolder_check("hdri")

		sort_file_type(hdri_path + "/" + folder)

		shutil.move(hdri_path + "/" + folder, "sorted/slates/" + slate + "/hdri")

print("hdri sorted")

# needs to sort into slates folder 
#need to put individual files into folders in structure SLATE_witness_cam

witcam_path = "unsorted/witness"

witcam_cam_obj = os.scandir(witcam_path)


#pre sort witcam

for entry in witcam_cam_obj:

	if not DS_store(entry.name):
		camera = entry.name

		witcam_slates_list = []

		witcam_file_obj = os.scandir(witcam_path + "/" + camera)

		path = witcam_path + "/" + camera

		for entry in witcam_file_obj:

			file = entry.name

			slate = ""

			if not DS_store(file):

				slate = get_slate(file)

				add_slate_check(slate, slates_list)

				#checks for duplicates, creates and adds witcam to folders
				add_witcam_slate_check(slate, witcam_slates_list, camera, path)

				add_subfolder_check("witness")
				add_subfolder_check("witness/" + camera)

				new_folder_name = slate + "_witness_" + camera

				shutil.move(path + "/" + file, path + "/" + new_folder_name)

#sort witcam into slates

witcam_cam_obj_2 = os.scandir(witcam_path)

for entry in witcam_cam_obj_2:

	if not DS_store(entry.name):

		camera = entry.name

		witcam_folder_obj = os.scandir(witcam_path + "/" + camera)

		path = witcam_path + "/" + camera

		for entry in witcam_folder_obj:

			folder = entry.name

			slate = get_slate(folder)

			if not DS_store(folder):

				shutil.move(path + "/" + folder, "sorted/slates/" + slate + "/witness/" + camera)



