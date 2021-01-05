import requests
import json
import tarefa

def buscar_dados():
    request = requests.get(f"http://localhost:3002/api/todo")
    todo = json.loads(request.content)
    print(todo)
    print(todo[0]['titulo'])

def cadastrar_dados(tarefa):
    requests.post("http://localhost:3002/api/todo", data=json.dumps(tarefa.__dict__))

def editar_dados(id, tarefa):
    requests.put(f"http://localhost:3002/api/todo?id={id}", data=json.dumps(tarefa.__dict__))

def remover_dados(id):
    requests.delete(f"http://localhost:3002/api/todo?id={id}")

if __name__ == '__main__':
    buscar_dados()
