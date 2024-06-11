class User:
    def __init__(self,nome,idade,cpf,cep,senha):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cep = cep
        self.senha = senha

class Admin(User):
    def __init__(self, nome, idade, cpf, cep,cnpj,senha):
        super().__init__(nome, idade, cpf, cep,senha)
        self.cnpj = cnpj
        self.secretario = []

    def autenticar(self,senha):
        return self.senha == senha
    
    def adicionar_secretario(self,secretario):
        self.secretario.append(secretario)
        print(f'secretario(a) {secretario.nome} adicionado(a).')

class Secretario(User):
    def __init__(self, nome, idade, cpf, cep, senha,id):
        super().__init__(nome, idade, cpf, cep, senha)
        self.id = id
        self.pacientes = []
        self.medicos = []
        self.agenda_medica = []

    def autenticar(self,senha):
        return self.senha == senha
    
    def adicionar_pacientes(self,paciente):
        self.pacientes.append(paciente)
        print(f'Paciente {paciente.nome} adicionado.')
        
    def adicionar_medicos(self,medico):
        self.medicos.append(medico)
        print(f'Médico {medico.nome} adicionado.')

    def busca_pacientes(self, nome):
        for paciente in self.pacientes:
            if paciente.nome == nome:
                return paciente
        return None   
    def busca_medicos(self, nome):
        for medico in self.medicos:
            if medico.nome == nome:
                return medico
        return None    
    
    def marcar_compromisso(self, compromisso):
        self.agenda_medica.append(compromisso)
        print(f'Compromisso {compromisso} marcado.')

    def alterar_dados_do_paciente(self, nome, novos_dados):
        paciente = self.buscar_pacientes(nome)
        if paciente:
            for chave, valor in novos_dados.items():
                setattr(paciente, chave, valor)
            print(f'Dados do paciente {nome} atualizados.')
        else:
            print(f'Paciente {nome} não encontrado.')
