import os
import shutil 

#global var

witcam = False
witcam_number = 0

#functions

def include(sort_type):

	answer = False

	print("Include " + sort_type + " (y/n)")

	type_answer = input()

	if type_answer == "y":
		os.makedirs("unsorted/" + sort_type)
		os.makedirs("to_sort/" + sort_type)
		answer = True

	return answer

def make_folders():
	#makes parent unsorted folder
	os.makedirs("unsorted")
	os.makedirs("to_sort")

	#makes data folders
	os.makedirs("unsorted/slates")
	os.makedirs("to_sort/slates")
	


make_folders()

include("hdri")
include("setref")
include("lidar")
include("reference")

#check if witcam / which witcam used

if include("witness") == True :

	print("Enter number of witcams")
	witcam_number = input()
	for x in range(int(witcam_number)):
		current = x + 1
		
		print("Enter witcam" + str(current) + " name")
		witcam_name = input()
		os.makedirs("unsorted/witness/" + witcam_name)
		os.makedirs("to_sort/witness/" + witcam_name)









