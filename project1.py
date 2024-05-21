print("How many kilometers did you have circled today")
km = input()

miles = float(km)/1.60934 #converting from string to float

miles = round(miles, 2)

print(f'Your {km}km ride was {miles}ml')