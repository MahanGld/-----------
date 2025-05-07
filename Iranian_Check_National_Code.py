x = input("Please enter your national code: ")
if not x.isdigit():
   print("You did not enter digits try again...")
else:
 x = list(x)
 y = [int(z) for z in x]
 if len(set(y)) == 1:
    print("Every digits is same false national code!!!!")
 else:
  if len(y)==10 :
     check_num = y[9]
     other_num = y[1:] 
     total = 0
     for i in range (9):
         total += y[i] * (10 - i)
         remainder = total % 11
     if remainder >= 2 :
        expected_num = 11 - remainder
     else:
        expected_num = remainder
     if check_num == expected_num:
        print("The entered national code is valid.")
     else:
        print("The entered national code is not valid try again!!!")

  else:
   print("The entered national code is not valid...")
