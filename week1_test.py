import requests,csv
resp = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = resp.json()

with open('todos.csv', 'w') as f:
    writer = csv.DictWriter(f,fieldnames=todos[0].keys())
    writer.writeheader()
    writer.writerows(todos)