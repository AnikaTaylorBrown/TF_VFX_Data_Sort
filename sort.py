import os
import shutil 


#DOC NOTES
#please utilize this script with the folder structure created in dump.py
#make sure not to use unusual naming conventions such as including a "." in folder / file names

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
	for x in folder:
		if x == ".":
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
	os.makedirs("slates/"+ slate)
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

#create parent slate folder
os.makedirs("slates")


#sort setref

setref_path = "unsorted/setref"

setref_obj = os.scandir(setref_path)



for entry in setref_obj:

		folder = entry.name

		#find slate token
		slate = ""

		#check if .DS Store File
		if not DS_store(folder):
	
			slate = get_slate(folder)

			add_slate_check(slate, slates_list)

			shutil.move(setref_path + "/" + folder, "slates/" + slate)



#sort hdri

hdri_path = "unsorted/hdri"

hdri_obj = os.scandir(hdri_path)



for entry in hdri_obj:

		folder = entry.name

		#find slate token
		slate = ""

		#check if .DS Store File
		if not DS_store(folder):
	
			slate = get_slate(folder)

			add_slate_check(slate, slates_list)


			shutil.move(hdri_path + "/" + folder, "slates/" + slate)



# needs to sort into slates folder 
#need to put individual files into folders in structure SLATE_witness_cam

witcam_path = "unsorted/witness"

witcam_cam_obj = os.scandir(witcam_path)


#pre sort witcam

for entry in witcam_cam_obj:

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

			shutil.move(path + "/" + file, path + "/" + slate + "_witness_" + camera)

























