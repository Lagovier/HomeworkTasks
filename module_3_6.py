data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def summ_everything(data):
    summa = 0
    if isinstance(data, (int, float)):
        summa += data
    elif isinstance(data, str):
        summa += len(data)
    elif isinstance(data, (list, set, tuple)):
        for item in data:
            summa += summ_everything(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            summa += summ_everything(key) + summ_everything(value)
    return summa

print(summ_everything(data_structure))
