print("Welcome to the Cybersecurity Password Strength Checker 🔐")
print("Type 'exit' any time to stop.\n")

while True: # Loop forever so user can test multiple passwords

     password = input("Enter your password (or 'exit' to stop): ")

      # Exit condition
     if password == 'exit':
         print("Exiting program...")
         break

     strength = 0   # reset strength score for each new password

     # Check length
     if len(password) >= 8:
        strength += 1

     # Check for at least one number
     for char in password:
         if char.isdigit():
             strength += 1
             break    # stop checking once found

     # Check for at least one uppercase letter
     for char in password:
         if char.isupper():
             strength += 1
             break

     # Check for at least one special character
     special_characters = "!@#$%^&*()_+-=[]{}|;:'\",.<>/?"
     for char in password:
         if char in special_characters:
             strength += 1
             break

     # Give feedback based on score
     if strength <= 1:
         print("nah very weak password❌ \nTry adding numbers or symbols.")
     elif strength == 2:
         print("meh weak password ⚠️")
     elif strength == 3:
         print("okay not bad 👍")
     else:
         print("perfect! strong password ✅")

     print()   # empty line for cleaner output







    # ----- Sample Input/Output -----
# Enter your password: abcd
# Nah... very weak password ❌
# Try adding numbers or symbols.
#
# Enter your password: Abcd1234
# Okay! Not bad 👍
#
# Enter your password: Abc123!
# Perfect! Strong password ✅
#
# Enter your password: exit
# Exiting program...

