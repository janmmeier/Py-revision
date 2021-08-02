friends = ["Kevin", "Karen", "John", "Liis", "Jim"]
#Items in list start from 0 = Kevin, 1 = Karen, 2 = John and so on.
print(friends)
print(friends[3]) #Grabs 4th item on the list
print(friends[1:]) #Grabs items from the second one
print(friends[0:3]) #Grabs items from 0 to 3

lucky_numbers = [4, 8, 15, 24, 42, 56, 68, 99]
friends.extend(lucky_numbers) #adds lucky numbers to the friends list
#.append() - adds something to the end of the list
#.insert(1, "Kelly") - adds an item to the list at the needed position
#.remove("jim") - removes items
#.clear() - cleares the list
#.pop() - removes a random item from the list
print(friends.index("Kevin")) #checks if item is in the list and where is it located
#.sort() - sorts the list in alphabetical order
#.reverse()
#friends2 = friends.copy() - copies the list

coordinates = (4, 5) #Tuple is like a list but you cant change whats in a tuple w commands
coordinates_list = [(4, 5), (1, 80), (34032, 12930)]
print(coordinates[0])

