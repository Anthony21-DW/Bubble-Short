def shortBubble(arr, desc = 'asc'):
  for i in range(len(arr) - 1 ):
    for j in range(len(arr) - i - 1):
      if desc == 'asc':
        if arr[j] > arr[j + 1]:
          arr[j],arr[j+1] = arr[j +1], arr[j]
        elif desc == 'dec':
          if arr[j] < arr[j + 1]:
          arr[j],arr[j+1] = arr[j +1], arr[j]
  return arr

    
