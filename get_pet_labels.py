#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Victor Bucar
# DATE CREATED: 04/05/2020                       
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = {}
    
    filename_list = listdir(image_dir)
    pet_labels = []
    
    ## FUNCTION TO TEST THE IMPLEMENTED LOGIC
    pet_labels = create_pet_labels(filename_list)

    # create the dictionary
    for index in range(0,len(filename_list),1):
        if filename_list[index] not in results_dic: ## add if not already in dictionary
            results_dic[filename_list[index]] = [pet_labels[index]]
        else:
            print("** Warning: Key=", filename_list[index], 
               "already exists in results_dic with value =", 
               results_dic[filename_list[index]])
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic

def create_pet_labels(pet_image_list):
    # Sets pet_image variable to a filename 
    #pet_image = ["Boston_terrier_02259.jpg","Basenji_0047346.jpg"]
    pet_labels = []
    for pet in pet_image_list: ## iterate over the files names
        pet_name = ""
        pet = pet.lower().split("_") # get the file name and create a list to extract the dog name
        for name in pet:
            if name.isalpha(): # only add if alphabetic characters
                pet_name += name + " "
        pet_labels.append(pet_name.strip())
    
    return pet_labels