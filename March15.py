#Today im doing day 7 because i was behind for a couple of the classes
#Today I learned how to do Nesting
print ("Are you a superfan of 'The Big Bang Theory' or a fake fan? ")
print()
print("Answer these questions to find out.")
Glasses = input("Does someone wear glasses? ")
if Glasses == "yes":
  print("Correct!")
else:
  print("Wrong!")
  WhoGlasses = input("And who wears glasses? ")
  if WhoGlasses == "Ipek":
    print("You got it")
  else:
    print("Try again!")
