alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in alphabet:
    print (i)

usertry = input("Enter your number:  ")
usertry = int(usertry)
print("The letter of the alphabet for you would be {}".format(alphabet[usertry]))
