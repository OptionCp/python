from sys import argv

script, userName = argv
prompt = '> '
print(f"Hi {userName}, I'm the {script} script.")
print("there are some questions")
print(f"what food you like")
likes = input(prompt)
print(f"which one is your favriate sport")
sport = input(prompt)

print(f"ok {userName}, you like {likes} and faviate sport is {sport}")