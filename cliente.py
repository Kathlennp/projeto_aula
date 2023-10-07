# classe cliente
class cliente:
    def __init__(self):
      self.nome = ""
      self.sobrenome = ""
      self.endereco = ""
      self.numero_celular = ""
      self.email = ""
      self.sexo = ""

    def pedir_informacoes(self):
     self.nome = input("Qual seu nome?: ") 
     self.sobrenome = input("Qual o seu sobrenome?: ") 
     self.endereco = input("Qual seu endereço?: ")
     self.numero_celular = input("Qual seu número de celular?: ")
     self.email = input("Qual o seu e-mail?: ")
     self.sexo = input("Qual o seu sexo?: ")

    """def retornar_informacoes(self):
      print("Nome:", self.nome)
      print("Sobrenome:", self.sobrenome)
      print("Endereço:", self.endereco)
      print("Número de celular:", self.numero_celular)
      print("Email:", self.email)
      print("Sexo:", self.sexo)"""

cliente1 = cliente()
cliente1.pedir_informacoes()










