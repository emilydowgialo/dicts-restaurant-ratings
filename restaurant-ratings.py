"""
Returns restaurant name and rating in one formatted line

"""
import sys


restaurants_info={}
sorted_scores=[]

ratings_file = open("scores.txt")

for line in ratings_file:
	#push all the elements into our list 
	#remove the \n
	line = line.rstrip()
	
	info_pair=line.split(":")

	restaurant_name = info_pair[0]
	restaurant_rating = int(info_pair[1])
	restaurants_info[restaurant_name]=restaurant_rating
			
#sorting the keys to create an alphabetical list	
sorted_keys = sorted(restaurants_info.keys())
#walk through the list using the key value and print out the message
for key in sorted_keys:
	print key, "is rated at", restaurants_info[key] 

#
# for i, number in restaurants_info.items():
# 	print "%s is rated at %d"%(i,number)


# ######################################################################
# #for further study

user_restaurant = raw_input("Please enter a restaurant name: ")
user_rating = raw_input("Please enter a restaurant rating that is 1-5: ")

restaurants_info[user_restaurant]=user_rating

#sorting the keys to create an alphabetical list	
sorted_keys = sorted(restaurants_info.keys())
#walk through the list using the key value and print out the message
for key in sorted_keys:
	print key, "is rated at", restaurants_info[key] 
