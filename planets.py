def weight_on_planets():
   # write your code here
   userInput = input("What do you weigh on earth? ")
   userWeight = float(userInput)

   # User weight under alternate gravitation pulls
   marsWeight = userWeight * 0.38
   jupiterWeight = userWeight * 2.34

   # Print new weights
   print("\n"
         "On Mars you would weigh", marsWeight, "pounds.\n"
         "On Jupiter you would weigh", jupiterWeight, "pounds.")

if __name__ == '__main__':
    weight_on_planets()