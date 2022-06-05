'''
423. Reconstruct Original Digits from English
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
'''
def reconstructDigits(word):
    count = [0] * 10

    for letter in word:
      if letter == 'z':
        count[0] += 1
      if letter == 'o':
        count[1] += 1
      if letter == 'w':
        count[2] += 1
      if letter == 'h':
        count[3] += 1
      if letter == 'u':
        count[4] += 1
      if letter == 'f':
        count[5] += 1
      if letter == 'x':
        count[6] += 1
      if letter == 's':
        count[7] += 1
      if letter == 'g':
        count[8] += 1
      if letter == 'i':
        count[9] += 1

    count[1] -= count[0] + count[2] + count[4]
    count[3] -= count[8]
    count[5] -= count[4]
    count[7] -= count[6]
    count[9] -= count[5] + count[6] + count[8]

    output = ""
    for i in range(len(count)):
        output += count[i]*str(i)
    return output

print("Input: fviefuro    Output:",reconstructDigits("fviefuro"))
print("Input: owoztneoer  Output:",reconstructDigits("owoztneoer"))