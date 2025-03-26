# program to read from a file
# strName = "c:\\temp\\ratings.txt"
strName = "ratings.txt"

try:
    file = open(strName, "r")
    field1 = ""; field2 = ""; field3 = ""
    field4 = ""; field5 = ""; field6 = ""; field7 = ""

    # Initialize variables
    total_rating = 0
    count = 0
    male_voters = 0
    female_voters = 0
    age_40_49_voters = 0
    recent_ratings_count = 0

    # Lists that will be used to store ages
    ages = []  
    male_ages = [] 
    female_ages = []  
    
    # Skip the header row
    next(file)

    for line in file:
       
        fields = line.rstrip().split(",")
        field1 = fields[0].strip()  # Member ID
        field2 = float(fields[1].strip())  # Rating
        field3 = fields[2].strip()  # Crew involvement
        field4 = fields[3].strip()  # Date rated
        field5 = fields[4].strip()  # Gender
        field6 = int(fields[5].strip())  # Age
        field7 = fields[6].strip()  # Demographics

        # Calculate the total rating and count voters
        total_rating += field2
        count += 1

        # Count male/female voters and collect ages
        ages.append(field6)
        if field5 == "M":
            male_voters += 1
            male_ages.append(field6)
        elif field5 == "F":
            female_voters += 1
            female_ages.append(field6)

        # Count voters in the 40-49 range
        if 40 <= field6 <= 49:
            age_40_49_voters += 1

        # Check if the rating was posted in a recent date 
        month, day = map(int, field4.split("/"))  # Assuming MM/DD format
        if month >= 1 and month <= 2:  # Considering January and February as recent
            recent_ratings_count += 1

        # Print the current line's fields
        print(field1 + "\t" + str(field2) + "\t" + field3 + "\t" +
              field4 + "\t" + field5 + "\t" + str(field6) + "\t" + field7)

    # Calculate the average rating, rounded to one decimal place
    average_rating = round(total_rating / count, 1)

    # Get the age ranges by gender and overall
    overall_age_range = max(ages, default=0) - min(ages, default=0)
    male_age_range = max(male_ages, default=0) - min(male_ages, default=0)
    female_age_range = max(female_ages, default=0) - min(female_ages, default=0)

    # Calculate the ratio of recent ratings to total ratings
    recent_ratings_ratio = recent_ratings_count / count

    # Calculate the ratios
    male_age_ratio = male_age_range / max(male_voters, 1)
    female_age_ratio = female_age_range / max(female_voters, 1)


    # Output the results
    print()
    print("Average movie rating: ", average_rating)
    print("Number of male voters: ", male_voters)
    print("Number of female voters: ", female_voters)
    print("Number of voters aged 40-49: ", age_40_49_voters)
    print("\n---------------------------------------------------\n")
    print("Overall Age Range: ", overall_age_range)
    print(f"Male Age Range Ratio: {male_age_ratio:.2f}")
    print(f"Female Age Range Ratio: {female_age_ratio:.2f}")
    print("\n---------------------------------------------------\n")


    # AI: can we predict when the movie was released
    if recent_ratings_ratio >= 0.75:
        print("It seems the movie was most likely released within the last 2 years") # If the ratio is greater than or equal 
                                                                                    # to .75 we assume the movie is newer
    elif 0.50 < recent_ratings_ratio < 0.75:
        print("SIt seems the movie was most likely released within the last 10 years") #If the ratio is between .5 and .75 
                                                                                    # we assume the movie is within the decade
    else:
        print("It seems the movie was most likely released within the last 15 years or older") # If the ratio is less than 
                                                                                            # .5 we assume the movie is within the last 15 years or more
    
    print("\n---------------------------------------------------\n")


    # AI: can we predict the genre?
    if male_age_ratio > female_age_ratio:
        print("It seems the genre of the movie being rated is Action or Adventure\n") # Assuming men are dominating the votes
    else:
        print("It seems the genre of the movie being rated is Romance\n") # Assuming woman are dominating the votes
    
    print("\n---------------------------------------------------\n")

    file.close()

except IOError:
    print("File appears to not exist!")
