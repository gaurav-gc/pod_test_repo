# Challenge 1
print("Challenge 1: All possible laptops\n")

print("Question 1: You are given a list containing the laptop names. Print the names of each the laptops separately.")
all_laptops = ["Apple MacBook Pro", "Asus Zenbook", "Dell XPS", "Lenovo IdeaPad", "Apple MacBook Air", "Sony Viao"]


# TODO: Write code to print all laptop names
print("All laptops names:")
# create a variable count for checking list indices
count = 0
# loop through the laptop names in the list
for name in all_laptops:
    # print each laptop name separately with each loop cycle
    print(all_laptops[count])
    # increase count by 1 to check the next index when cycle thourh loop again
    count = count + 1

print()

# Challenge 2

print("Challenge 2: Buy a laptop")
print("Below is a dictionary of the top 2 laptops of 2020 as reviewed by Tech Crunch. \
    Go through the dictionary and print out the following 3 pieces of information about the laptops: \
    \n1. The url for the Apple Macbook Pro \
    \n2. All possible prices of the 16-inch MacBook Pro. \
    \n3. All the color options for Dell XPS 13. \
    \n4. The description of Dell XPS.\n")

laptops = [
        {
            "productName": "Apple Macbook Pro",
            "url": "https://www.apple.com/macbook-pro-13/",
            "types": [
                {
                    "id": "1",
                    "screen_size": "13-inch",
                    "cpu": ["1.4GHz quad-core 8th-generation Intel Core i5 processor", "2.0GHz quad-core 10th-generation Intel Core i5 processor"],
                    "ram": ["8GB","16GB"],
                    "storage": ["256GB SSD","512 GB SSD"],
                    "colors": ["space gray", "silver"],
                    "price": [1299, 1499, 1799]
                },
                {
                    "id": "2",
                    "screen_size": "16-inch",
                    "cpu": ["2.6GHz 6-core 9th-generation Intel Core i7 processor", "2.3GHz 8-core 9th-generation Intel Core i9 processor"],
                    "ram": ["16GB"],
                    "storage": ["512 GB SSD", "1 TB SSD"],
                    "colors": ["space gray", "silver"],
                    "price": [2399, 2799]
                }
            ],
            "description": "If you're after the latest and greatest laptop from Apple, we suggest you look into the 2020 model of the MacBook Pro. The headline Touch Bar – a thin OLED display at the top of the keyboard which can be used for any number of things, whether that be auto-suggesting words as you type or offering Touch ID so you can log in with just your fingerprint – is of course included. It's certainly retained Apple's sense of style, but it comes at a cost. This is a pricey machine, so you may want to consider one of the Windows alternatives. But, if you're a steadfast Apple diehard, this is definitely the best laptop for you!"
        },
        {
            "id": "2",
            "productName": "Dell XPS",
            "url": "https://www.dell.com/en-us/shop/dell-laptops/sr/laptops/xps-laptops?~ck=bt",
            "types": [
                {
                    "id": "3",
                    "screen_size": "13-inch",
                    "cpu": ["11th Generation Intel Core i3-1115G4 Processor", "11th Generation Intel Core i5-1135G7 Processor"],
                    "ram": ["8GB"],
                    "storage": ["256GB SSD","512 GB SSD", "1 TB SSD"],
                    "colors": ["Platinum silver exterior, black interior", "Platinum silver exterior, black interior"],
                    "price": [999, 1099, 1149, 1249]
                },
                {
                    "id": "4",
                    "screen_size": "15-inch",
                    "cpu": ["10th Generation Intel Core i5-10300H"],
                    "ram": ["8GB", "16GB", "32GB", "64GB"],
                    "storage": ["256 GB SSD", "512 GB SSD", "1 TB SSD", "2 TB SSD"],
                    "colors": ["Frost White with White Palmrest", "Frost White with White Palmrest"],
                    "price": [1199, 1299, 1399, 1749, 1999, 2299]
                }
            ],
            "description": "The Dell XPS is an absolutely brilliant laptop. The 2020  version rocks an 11th-generation Intel Core i3, i5 or i7 processor and a bezel-less ‘Infinity Edge’ display. This Dell XPS continues to be the most popular Windows laptop in the world. What’s more, there’s a wide range of customization options, so you can really make the Dell XPS the best laptop for your needs. "
        }
]

    # \n4. The description of Dell XPS.

# TODO: Write code to print out the MacBook Pro url 
print('#1')
# print url for Macbook Pro by accessing its list index and the url key value
print(laptops[0]['url'])
print()
# TODO: Write code to print all possible prices of the 16-inch MacBook Pro.
print('#2')
# print price list for the 16-inch Macbook Pro by accessing its list index, types key value list index, and prices key value which returns a list
print(laptops[0]['types'][1]['price'])
print()
# TODO: Write code to print all the color options for Dell XPS 13.
print('#3')
# print color options for the Dell XPS 13 by accessing its list index, types key value list index, and colors key value which returns a list (challenge code provided lists the same color twice for each Dell)
print(laptops[1]['types'][0]['colors'])
print()
# TODO: Write code to print the description of Dell XPS laptop.
print('#4')
# print description of Dell XPS by accessing its list location and the description key value
print(laptops[1]['description'])
print()

print("Question 2: Out of Stock laptops")
print("Suppose that the 13-inch MacBook Pro in space gray color is sold out. Also, the same laptop with 1 TB storage is out of stock as well. Update the list of dictionaries such that these options are removed. Print the updated dictionary.")

# TODO: Update the laptops dictionary.
# remove 'space gray' from list value for key colors of a dictionary in the list value for the key types in a dictionary in the list laptops
# removing 'space gray' color from 13-inch MacBook Pro
laptops[0]['types'][0]['colors'].remove("space gray")
# remove '1 TB SSD' from list value for key storage of a dictionary in the list value for the key types in a dictionary in the list 
# removing 1 TB storage option from the MacBook Pro which was only available on the 16-inch
laptops[0]['types'][1]['storage'].remove('1 TB SSD')

# TODO: Print the new dictionary.
print()
# print the updated dictionary for the MacBook Pro
print(laptops[0])
print()

print("Question 3: listing all the prices")
print("Time to look at the range of prices. Print out all possible computer prices")

# TODO: print out all possible prices for the laptops
print()
# create a variable count for checking list indices as we cycle through a loop
count = 0
# loop through each element in the list laptops
for devices in laptops:
    # create a variable count2 for checking list indices as we cycle through a loop
    count2 = 0
    # loop through the list value of the key types for each time we loop through the list laptops
    for sizes in laptops[count]['types']: 
        # print the list of prices for each product name and type of laptop
        print(f"{laptops[count]['productName']}, {laptops[count]['types'][count2]['screen_size']}: {laptops[count]['types'][count2]['price']}")
        # add to variable count2 to check the next index with the next cycle of the loop
        count2 = count2 + 1
        # add to variable count2 to check the next index with the next cycle of the loop
    count = count +1

print()
