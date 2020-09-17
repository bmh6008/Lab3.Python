# Author: Byongchul Hur bmh6008@psu.edu
# Collaborator: Abbey Kato amk7306@psu.edu
# Collaborator: Chen-Kuan Liao czl5899@psu.edu
# Collaborator: Zhili Hu zjh5265@psu.edu
# Section: 1
# Breakout: 3

def sum_n(n):
  if n==0:
    return 1
  else:
    return n + sum_n(n-1)

def print_n(s, n):
  if n<= 0 :
    return
  else: 
   print_n(s)
   print_n(s,n-1)


def run():
  num = int(input("Enter at int: "))
  print(f"sum is {sum_n(num)}.")
  string = str(input("Enter a string: "))
  print_n(string,num)

  
if __name__ == "__main__":
  run()






