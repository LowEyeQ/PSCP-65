"""iPhone 13 Again"""
def iphone():
    """iPhone 13 Again"""
    model = input()
    capacity = input()
    if model == "iPhone 13":
        iphonethirteen(capacity)
    elif model == "iPhone 13 mini":
        iphonemini(capacity)
    elif model == "iPhone 13 Pro":
        iphonethirteenpro(capacity)
    elif model == "iPhone 13 Pro Max":
        iphonethirteenpromax(capacity)
    else:
        print("Not Available")

def iphonethirteen(capacity):
    """iPhone 13"""
    if capacity == "128 GB":
        print(29900)
    elif capacity == "256 GB":
        print(33900)
    elif capacity == "512 GB":
        print(41900)
    else:
        print("Not Available")

def iphonemini(capacity):
    """iPhone 13 mini"""
    if capacity == "128 GB":
        print(25900)
    elif capacity == "256 GB":
        print(29900)
    elif capacity == "512 GB":
        print(37900)
    else:
        print("Not Available")

def iphonethirteenpro(capacity):
    """iPhone 13 Pro"""
    if capacity == "128 GB":
        print(38900)
    elif capacity == "256 GB":
        print(42900)
    elif capacity == "512 GB":
        print(50900)
    elif capacity == "1 TB":
        print(58900)
    else:
        print("Not Available")

def iphonethirteenpromax(capacity):
    """iPhone 13 Pro Max"""
    if capacity == "128 GB":
        print(42900)
    elif capacity == "256 GB":
        print(46900)
    elif capacity == "512 GB":
        print(54900)
    elif capacity == "1 TB":
        print(62900)
    else:
        print("Not Available")
iphone()
