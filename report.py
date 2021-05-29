import csv
import json

mentees = open("Mentees_Report_Task.csv")   #I open CSV file and I save it under mentees variable
reader = csv.DictReader(mentees)            #Under reader variable I access CSV file for reading

list_mentees = []                           #Empty list for summing up of all the rows of CSV

for row in reader:                          #Loop adds every row of CSV in list_mentees list
    list_mentees.append(row)

number_count = len(list_mentees)            #Count the number of mentees

lang = []                                   #Empty list for language count

for y in list_mentees:                      #Loop to add all the mentioned languages in a lang list
    language = (y['language'])
    if language not in lang:                #Condition checks if the language is already mentioned
        lang.append(language)               #If not, il will be added to the lang list

all_names = 0                                                                   #Counter for all letter in all names and last names
longest = ''                                                                    #Variable with empty string of the longest name, empty bcs every name will have letter count bigger than 0
shortest = list_mentees[0]['first_name'] + ' ' + list_mentees[0]['last_name']   #Variable with the first name and last name of the list list_mentees

for z in list_mentees:                                                          #Loop through the mentees to calculate the statistics
    first_name = (z['first_name'])
    last_name = (z['last_name'])
    mentee_name = first_name + ' ' + last_name                                  #Under the mentee_name I join first name and last name with space in the middle
    length = len(mentee_name)                                                   #I save length of mentee_name under length variable
    all_names = all_names + length                                              #By looping I add every length of joined name to all_names counter

    if len(longest) < length:                                                   #If the longest variable is smaller, it gets replaced by the new (higher) value
        longest = mentee_name

    if len(shortest) > length:                                                  #If the shortest variable is bigger, it gets replaced by the new (smaller) value
        shortest = mentee_name

average = int(all_names / number_count)                 #Computation of average letter per name, we get 15.08 letter per name
                                                        #I round it because we cannot have 0,02 letters
json_report = {'number_of_trainees': number_count,      #Dictionary with answers to all qustions from task
               'all_languages_used': lang,
               'average_number_of_letters': average,
               'longest_name': longest,
               'shortest_name': shortest}

print(json.dumps(json_report, ensure_ascii=False, indent=2))
