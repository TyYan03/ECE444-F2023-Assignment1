import utils

def test_reversed():
  flag = true
  if utils.reversed(0) != 0:
    flag = false
  if utils.reversed(92381) != 18329:
    flag = false
  if utils.reversed(9) != 9:
    flag = false
  if utils.reversed(12345) != 54321:
    flag = false
  if utils.reversed(012) != 21:
    flag = false

  if flag:
    print("5/5 Tests Successful")
  else:
    print("Failed")

def test_formatted():
  flag = true
  if utils.formatter(8) != (1000, 10):
    flag = false
  if utils.formatter(1245) != (10011011101, 2335):
    flag = false
  if utils.formatter(2) != (10, 2):
    flag = false
  if utils.formatter(999) != (1111100111, 1747):
    flag = false
  if utils.formatter(012) != (1100, 14):
    flag = false

  if flag:
    print("5/5 Tests Successful")
  else:
    print("Failed")
