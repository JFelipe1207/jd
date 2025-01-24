import random
import string
def main():
    tamanho = int(input("Informe o tamanho da senha: "))
    todos_os_caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(todos_os_caracteres) for _ in range(tamanho))
    print(f"Senha gerada: {senha}")
main()
