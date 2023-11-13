import random
from collections import deque

# Definindo a classe Nó
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Função para inserir um novo nó com a chave fornecida na Árvore de Busca Binária
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Função para fazer a travessia em pré-ordem da Árvore de Busca Binária
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Função para fazer a travessia em ordem da Árvore de Busca Binária
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Função para fazer a travessia em pós-ordem da Árvore de Busca Binária
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# Função para fazer a travessia em nível da Árvore de Busca Binária
def levelorder(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].val, end=" ")
        node = queue.popleft()

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

# Função para deletar um nó com uma chave fornecida da Árvore de Busca Binária
def delete(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif(key > root.val):
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root

# Função para encontrar o nó com o valor mínimo
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

# Gerando 20 números aleatórios entre 0 e 100
numbers = random.sample(range(0, 101), 20)
print("Números sorteados: ", numbers)

# Inserindo os números na Árvore de Busca Binária
r = Node(numbers[0])
for number in numbers[1:]:
    r = insert(r, number)

# Imprimindo os números em pré-ordem
print("\nPré-ordem: ")
preorder(r)

# Imprimindo os números em ordem
print("\n\nIn-ordem: ")
inorder(r)

# Imprimindo os números em pós-ordem
print("\n\nPós-ordem: ")
postorder(r)

# Imprimindo os números em nível
print("\n\nEm nível: ")
levelorder(r)

# Removendo 5 elementos aleatórios da Árvore de Busca Binária
numbers_to_remove = random.sample(numbers, 5)
print("\n\nNúmeros a serem removidos: ", numbers_to_remove)

for number in numbers_to_remove:
    r = delete(r, number)

# Imprimindo os números após a remoção
print("\n\nApós a remoção:")

print("\nPré-ordem: ")
preorder(r)

print("\n\nIn-ordem: ")
inorder(r)

print("\n\nPós-ordem: ")
postorder(r)

print("\n\nEm nível: ")
levelorder(r)
