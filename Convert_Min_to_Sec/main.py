def convert(min):
    sec = min * 60
    return sec

minutes = int(input("Please enter the number of minutes you want to convert: "))
print(f"{minutes} minutes = {convert(minutes)} seconds")