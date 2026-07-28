string = "hi"
while True:
  try:
    print(string + 3)
    break
  except TypeError:
    print("except block")
print("hi")
