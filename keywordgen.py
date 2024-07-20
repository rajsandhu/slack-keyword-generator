# Define the lists
list_1 = [
    "web developer", "webdev", "software engineer", "SE", "developer", 
    "solutions architect", "analyst", "engineer", "frontend", "front-end", 
    "front end", "backend", "back-end", "back end", "fullstack", "full-stack", 
    "full stack", "data", "cloud"
]

list_2 = ["junior", "jr", "jr.", "contract", "freelance", "freiberufler", "freiberuf", "freiberuflisch"]

list_3 = ["internship", "intern", "praktikum", "praktikant"]

# Generate combinations by adding list_2 terms to the beginning of each term in list_1
combinations_list_2 = []
for item in list_1:
    for prefix in list_2:
        combinations_list_2.append(prefix + " " + item)

# Generate combinations by adding list_3 terms to the end of each term in list_1
combinations_list_3 = []
for item in list_1:
    for suffix in list_3:
        combinations_list_3.append(item + " " + suffix)

# Combine both lists of combinations
full_combinations_list = combinations_list_2 + combinations_list_3

# Print the full list of combinations
for combo in full_combinations_list:
    print(combo)
