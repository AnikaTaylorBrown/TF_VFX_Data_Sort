import os
import shutil 

#global var

witcam = False
witcam_number = 0

#functions

def make_folders():
	#makes parent unsorted folder
	os.makedirs("unsorted")

	#makes data folders
	os.makedirs("unsorted/slates")
	os.makedirs("unsorted/hdri")
	os.makedirs("unsorted/lidar")
	os.makedirs("unsorted/reference")
	os.makedirs("unsorted/setref")

#check if witcam / which witcam used

print("Include witcams? (y/n)")

witcam_answer = input()

if witcam_answer == "y":
	make_folders()
	os.makedirs("unsorted/witness")

	print("Enter number of witcams")
	witcam_number = input()
	for x in range(int(witcam_number)):
		current = x + 1
		
		print("Enter witcam" + str(current) + " name")
		witcam_name = input()
		os.makedirs("unsorted/witness/" + witcam_name)

elif witcam_answer == "n":
	make_folders()
else :
	print("Invalid input")








