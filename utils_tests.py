from utils import utils

def test_reversed():
  flag = True
  if utils.reversed(0) != 0:
    flag = False
  if utils.reversed(92381) != 18329:
    flag = False
  if utils.reversed(9) != 9:
    flag = False
  if utils.reversed(12345.4) != -1:
    flag = False
  if utils.reversed("12") != -1:
    flag = False

  if flag:
    print("5/5 Tests Successful")
  else:
    print("Failed")

def test_formatted():
  flag = True
  if utils.formatter(8) != (1000, 10):
    flag = False
  if utils.formatter(1245) != (10011011101, 2335):
    flag = False
  if utils.formatter(999) != (1111100111, 1747):
    flag = False
  if utils.formatter(2.3) != (-1, -1):
    flag = False
  if utils.formatter("12") != (-1, -1):
    flag = False

  if flag:
    print("5/5 Tests Successful")
  else:
    print("Failed")

test_reversed()
test_formatted()
