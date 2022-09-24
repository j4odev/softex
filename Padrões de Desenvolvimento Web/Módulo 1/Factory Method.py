from abc import ABC, abstractmethod

class Logistics:
  def createMachine(self):
    pass

  def ClienteComputer(self):
    Client = self.createMachine()

    result = f"Máquinas estão sendo preparadas...\n{Client.Computer()}"

    return result

class Usuario(Logistics):
  def __init__(self, name):
    self.name = name
  
  def createMachine(self):
    return Pc(self.name)

class Servidor(Logistics):
  def __init__(self, name):
    self.name = name
  
  def createMachine(self):
    return Server (self.name)

class Factory(ABC):
  @abstractmethod
  def Computer(self):
    pass

class Pc(Factory):
  def __init__(self, name):
    self.name = name
    self.ram = "4GB" 
    self.hdd = "240GB"
    self.type = "PC"
    self.cpu = "3.5GHz"
  
  def Computer(self):
    result = (f"Maquina usuário: {self.name,self.type, self.ram,self.hdd, self.cpu}")
    return result

class Server (Factory):
  def __init__(self, name):
    self.name = name
    self.ram = "16GB" 
    self.hdd = "512GB"
    self.type = "Server"
    self.cpu = "4.5GHz" 
  
  def Computer(self):
    result = (f"Maquina do servidor:{self.name,self.type, self.ram,self.hdd, self.cpu}")
    return result

def client_code(logistics: Logistics):
  print(f"App Servido, {logistics.__class__.__name__}.",
        f"{logistics.ClienteComputer()}")

if __name__ == "__main__":
  client_code(Usuario('Configurações:'))
  print("\n")
  client_code(Servidor('Configurações:'))
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security