def bbox_norm(data):
  xs = []
  ys = []

  for x, y in (data):
    xs.append(x)
    ys.append(y)


  x_min = min(xs)
  x_max = max(xs)
  y_min = min(ys)
  y_max = max(ys)

  return [x_min,y_min,x_max,y_max]