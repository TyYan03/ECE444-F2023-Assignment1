def reversed(n):
  if isinstance(n, int):
    reverse = 0
    while n != 0:
      reverse *= 10
      reverse += n % 10
      n /= 10
  else:
    return -1
  return reverse

def formatter(n):
  if isinstance(n, int):
    store = n
    bin = 0
    while n != 0:
      bin *= 10
      bin += n % 2
      n /= 2

    n = store
    oct = 0
    while n != 0
      oct *= 10
      oct += n % 8
      n /= 8
  else:
    return -1, -1
  return bin, oct
