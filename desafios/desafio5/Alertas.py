#1. A Classe Usuario (O Cliente)
class Usuario:
    def __init__(self,nome,email):
        self.nome=nome
        self._email=email
    @property
    def email(self):
        print('Acessando o preço')
        return self._email
    def email(self,novo_preco):
        if  '@' not in novo_preco   :
            print('invalido')
        else:
            self.email=novo_preco
            print('Email válido')
            
            
#2. A Classe CanalEnvio (A Base Abstrata)
from abc import ABC,abstractmethod
class CanalEnvio(ABC):
    @abstractmethod
    def enviar(self,mensagem):
        raise NotImplementedError
    
    
#3. As Classes Email e SMS (As Implementações)
class Email(CanalEnvio):
    def enviar(self,mensagem):
        print(f'📨 Enviando para o servidor de email: {mensagem}')
        
class SMS(CanalEnvio):
    def enviar(self,mensagem):
        print(f'📱 Enviando para o servidor de sms: {mensagem}')
        
#4. A Classe SistemaAlerta (O Gerenciador)
class SistemaAlerta:
    def __init__(self,usuario,canal):
        self.usuario=usuario
        self.canal=canal
    def disparar(self,texto):
        print(f'Seu nome é {self.usuario}')
        self.canal.enviar(texto)

# 5. teste
            
a=Usuario('João','abc@gmail.com')
a.email('abc@gmail.com')

b=Email()
b.enviar('aaaa')
c=SistemaAlerta('Pedro',b)