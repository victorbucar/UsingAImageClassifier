#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Victor Bucar 
# DATE CREATED: 04/05/2020                              
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # defining dictionary and statistics variables
    results_stats = {}
    n_images = len(results_dic)#40#0
    n_correct_dog_match = 0
    n_dog_images = 0
    n_correct_non_dog_match = 0
    n_not_dog_image = 0
    n_correct_breed_match = 0
    
    labels_match = 0 #optional
    
    ## calculate number of dog matches and non matches         
    for key in results_dic:
        # Label match
        if results_dic[key][2] == 1:
            labels_match += 1
        # IS a dog image
        if results_dic[key][3] == 1:
            n_dog_images += 1
            #Correct breed match
            if results_dic[key][2] == 1:
                n_correct_breed_match += 1
            #Correct dog match
            if results_dic[key][4] == 1:
                n_correct_dog_match += 1
        #not a dog
        else:
            if results_dic[key][4] == 0:
                n_correct_non_dog_match += 1
                
                
    
    n_not_dog_image = len(results_dic) - n_dog_images
      
    
    #Statistics calculations

    #Percentage of correctly classified dog
    if n_dog_images > 0:
        per_correctly_class_dog = (n_correct_dog_match / n_dog_images) * 100
    else:
        per_correctly_class_dog = 0    
    ##Percentage of correctly classified non-dog
    if n_not_dog_image > 0:
        per_correctly_class_non_dog = (n_correct_non_dog_match / n_not_dog_image) * 100
    else:
        per_correctly_class_non_dog = 0
    # Percentage of correctly classified dog breeds
    if n_correct_breed_match > 0:
        per_correctly_class_dog_breed = (n_correct_breed_match / n_dog_images) * 100
    else:
        per_correctly_class_dog_breed = 0
    #Percentage of label matches even if not a dog
    if n_images > 0:
        per_label_match = (labels_match /  n_images) * 100
    else:
        per_label_match = 0
        
    #print("Printing statistics\n")
    #print("Classified dogs: ", per_correctly_class_dog)
    #print("Classified non-dogs: ", per_correctly_class_non_dog)
    #print("Classified dog breed: ", per_correctly_class_dog_breed)
    #print("Classified labels: ", per_label_match)
    

    
    #create the dic with all statistics and number
    results_stats["n_images"] = n_images

    results_stats["n_dogs_img"] = n_correct_dog_match
    results_stats["pct_correct_dogs"] = per_correctly_class_dog

    results_stats["n_notdogs_img"] = n_correct_non_dog_match
    results_stats["pct_correct_notdogs"] = per_correctly_class_non_dog

    results_stats["n_correct_breed"] = n_correct_breed_match
    results_stats["pct_correct_breed"] = per_correctly_class_dog_breed
    
    results_stats["n_correct_labels"] = labels_match
    results_stats["pct_label_match"] = per_label_match
    
    
    print(results_stats.items())
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    return results_stats
