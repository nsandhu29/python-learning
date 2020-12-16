# while loops and for loops
secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    pw = input("What's the secret word?")

animals = ('bear', 'dog', 'bunny', 'cat', 'velociraptor')
for pet in animals:
    if pet == 'dog': continue
    if pet == 'velociraptor': break
    print(pet)
else:
    print('that is all of animals')

# Additional controls
pw1 = ''
while pw1 != secret:
    count += 1
    if count > max_attempt: break
    if count == 3: continue
    pw = input(f"{count}: What's the secret word?")
else:
    auth = True

print("Authorized" if auth else "Calling police...")

