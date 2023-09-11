class utils:
  def reversed(n):
    if isinstance(n, int):
      reverse = 0
      while n != 0:
        reverse *= 10
        reverse += n % 10
        n //= 10
    else:
      return -1
    return reverse

  def formatter(n):
    if isinstance(n, int):
      store = n
      mult = 1
      bin = 0
      while n != 0:
        bin += (n % 2) * mult
        n //= 2
        mult *= 10

      mult = 1
      n = store
      oct = 0
      while n != 0:
        oct += (n % 8) * mult
        n //= 8
        mult *= 10
    else:
      return -1, -1
    return bin, oct
