def start_program(data: dict):
  assert isinstance(data, dict), 'Invalid JSON'
  assert data, 'No data found'
  
  print('Loaded successfully!')

if __name__ == '__main__':
  json = {"user": 1234}
  start_program(data=json)
  print(__debug__)
