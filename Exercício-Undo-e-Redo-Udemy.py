lista_tarefas = []
lista_removidas = []

while True:
    tarefa = input("Digite a tarefa")
    if tarefa == 'undo':
        if lista_tarefas:
            lista_removidas.append(lista_tarefas[-1])
            lista_tarefas.pop()
            print('tarefa desfeita')
            print(lista_tarefas)
        else:
            print('Ainda não há tarefas')
        continue
    if tarefa == 'redo':
        if lista_removidas:
            lista_tarefas.append(lista_removidas[-1])
            lista_removidas.pop()
            print('tarefa refeita')
            print(lista_tarefas)
        else:
            print('Ainda não há tarefas desfeitas')       
        continue


    if tarefa == 'quit':
        break
    lista_tarefas.append(tarefa)
    print(lista_tarefas)
print('até logo')