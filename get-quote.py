import random
def primary():
  # print("Hello World!")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  print(quotes[rnd])
  print(quotes[rnd2])
 # print(values='TEST'[last+1])

if __name__== "__main__":
  primary()
