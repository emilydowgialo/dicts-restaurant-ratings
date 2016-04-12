"""
Returns restaurant name and rating in one formatted line

"""
import sys


restaurants_info={}
sorted_scores=[]

file_scores = open("scores.txt")

for scores in file_scores:
	#push all the elements into our list 
	#remove the \n
	scores = scores.rstrip()
	sorted_scores.append(scores)

# sorting restaurant names alphabetically
sorted_scores=sorted(sorted_scores)

for entry in sorted_scores:
	info_pair = entry.split(",")


	for restaurant in info_pair:
		#len(restaurant)
		#we need to search the string and find ':'
		#and then split the string at the ':' creating two variables
		if ":" in restaurant:
			index_number = restaurant.index(":")
			
			restaurant_name = restaurant[:index_number]
			restaurant_rating = restaurant[index_number+1:]

			
			print restaurant_name, "is rated at", restaurant_rating
			#print restaurant_rating
			#restaurants_output[restaurant_name] = restaurant_rating

#print(restaurants_output)