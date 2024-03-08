nric = input('Enter an NRIC number: ')

# Type your code below
first_letter = "STFG"
if len(nric) == 9 and nric[0].upper() in first_letter and nric[1:8].isdigit() and  nric[8].isalpha():
  weight = 0
  if nric[0].upper() in "TG":
    weight = 4
  weight = weight + int(nric[1])*2 + int(nric[2])*7  + int(nric[3])*6 + int(nric[4])*5 + int(nric[5])*4 + int(nric[6])*3 + int(nric[7])*2
  weight = weight % 11
  if nric[0].upper() in "ST":
    weight += 11
  check_chr = "XWUTRQPNMLKJZIHGFEDCBA"
  if nric[8].upper() == check_chr[weight]:
    print("NRIC is valid.")
  else: 
    print("NRIC is invalid.")
else:
  print("NRIC is invalid.")