# Sort a Dictionary
# Sort by Keys
def run01():
    # initializing dictionary
    test_dict = {"Gfg": 5, "is": 7, "Best": 2, "for": 9, "geeks": 8}

    # printing original dictionary
    print("The original dictionary is : " + str(test_dict))

    # using items() to get all items
    # lambda function is passed in key to perform sort by key
    res = {key: val for key, val in sorted(test_dict.items(), key=lambda ele: ele[0])}

    # printing result
    print("Result dictionary sorted by keys : " + str(res))

    # using items() to get all items
    # lambda function is passed in key to perform sort by key
    # adding "reversed = True" for reversed order
    res = {key: val for key, val in sorted(test_dict.items(), key=lambda ele: ele[0], reverse=True)}

    # printing result
    print("Result dictionary sorted by keys ( in reversed order ) : " + str(res))


# Sort a Dictionary
# Sort by Values
def run02():
    # initializing dictionary
    test_dict = {"Gfg": 5, "is": 7, "Best": 2, "for": 9, "geeks": 8}

    # printing original dictionary
    print("The original dictionary is : " + str(test_dict))

    # using items() to get all items
    # lambda function is passed in key to perform sort by key
    # passing 2nd element of items()
    res = {key: val for key, val in sorted(test_dict.items(), key=lambda ele: ele[1])}

    # printing result
    print("Result dictionary sorted by values : " + str(res))

    # using items() to get all items
    # lambda function is passed in key to perform sort by key
    # passing 2nd element of items()
    # adding "reversed = True" for reversed order
    res = {key: val for key, val in sorted(test_dict.items(), key=lambda ele: ele[1], reverse=True)}

    # printing result
    print("Result dictionary sorted by values ( in reversed order ) : " + str(res))