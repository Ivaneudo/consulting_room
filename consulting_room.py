class User:
    def __init__(self, nome, idade, cpf, cep, senha):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cep = cep
        self.senha = senha

class Admin(User):
    def __init__(self, nome, idade, cpf, cep, cnpj, senha):
        super().__init__(nome, idade, cpf, cep,senha)
        self.cnpj = cnpj
        self.secretario = []

    def autenticar(self,senha):
        return self.senha == senha
    
    def adicionar_secretario(self, secretario):
        self.secretario.append(secretario)
        print(f'secretario(a) {secretario.nome} adicionado(a).')

class Secretario(User):
    def __init__(self, nome, idade, cpf, cep, senha, num_id):
        super().__init__(nome, idade, cpf, cep, senha)
        self.num_id = num_id
        self.pacientes = []
        self.medicos = []
        self.agenda_medica = []

    def autenticar(self,senha):
        return self.senha == senha
            
    def adicionar_medicos(self, medico):
        self.medicos.append(medico)
        print(f'Médico {medico.nome} adicionado.')

    def adicionar_pacientes(self, paciente):
        self.pacientes.append(paciente)
        print(f'Paciente {paciente.nome} adicionado.')

    def busca_medicos(self, nome):
        for medico in self.medicos:
            if medico.nome == nome:
                return medico
        return None    
    
    def busca_pacientes(self, nome):
        for paciente in self.pacientes:
            if paciente.nome == nome:
                return paciente
        return None   

    def verificar_agenda_medica(self):
        return self.agenda_medica

    def marcar_compromisso(self, compromisso):
        self.agenda_medica.append(compromisso)
        print(f'Compromisso {compromisso} marcado.')
        
    def marcar_exames(self, paciente, exame):
        paciente.exames.append(exame)
        print(f'Exame {exame} marcado para {paciente.nome}.')

    def marcar_consultas(self, paciente, consulta):
        paciente.consultas.append(consulta)
        print(f'Consulta {consulta} marcada para {paciente.nome}.')

    def busca_exames(self, paciente):
        return paciente.exames

    def busca_consultas(self, paciente):
        return paciente.consultas

    def cadastra_convenio(self, paciente, convenio):
        paciente.convenio = convenio
        print(f'Convênio {convenio} cadastrado para {paciente.nome}.')

    def busca_convenio(self, paciente):
        return paciente.convenio

    def emitir_relatorio(self):
        print(f'Relatório da secretária {self.nome}')
        print('Pacientes:')
        for paciente in self.pacientes:
            print(paciente.nome)
        print('Médicos:')
        for medico in self.medicos:
            print(medico.nome)

class Medico(User):
    def __init__(self, nome, idade, cpf, cep, senha, medicamentos = None, exames = None):
        super().__init__(nome, idade, cpf, cep, senha)
        self.medicamentos = medicamentos if medicamentos is not None else []
        self.exames = exames if exames is not None else []
    
    def autenticar(self, senha):
        return self.senha == senha
    
    def logar_no_sistema(self, senha):
        if self.autenticar(senha):
            print(f'{self.nome} logado com sucesso.')
            return True
        else:
            print('Senha incorreta.')
            return False
    
    def realizar_cirurgias(self):
        print(f'{self.nome} está realizando cirurgias.')

    def realizar_exames(self):
        print(f'{self.nome} está realizando exames.')

    def emitir_relatorio_de_exame(self):
        print(f'Relatório de exame por {self.nome}:')
        for exame in self.exames:
            print(exame)
    
    def agendar_consulta(self, consulta):
        print(f'Consulta {consulta} agendada por {self.nome}.')

class Paciente(User):
    def __init__(self, nome, idade, cpf, cep, senha):
        super().__init__(nome, idade, cpf, cep, senha)
        self.exames = []
        self.consultas = []
        self.mediamentos = []
        self.convenio = None

    def autenticar(self, senha):
        return self.senha == senha
    
    def logar_no_sistema(self, senha):
        if self.autenticar(senha):
            print(f'{self.nome} logado com sucesso.')
            return True
        else:
            print('Senha incorreta.')
            return False

def criar_administrador():
    nome = "Admin"
    idade = 16
    cpf = 12345
    cnpj = 123
    cep = 00000000
    senha = "root"
    return Admin(nome, idade, cpf, cnpj, cep, senha)


def criar_secretaria():
    nome = input("Nome da Secretária: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    cep = input("CEP: ")
    num_id = input("Número de Identificação: ")
    senha = input("Senha: ")
    return Secretario(nome, idade, cpf, cep, num_id, senha)


def criar_medico():
    nome = input("Nome do Médico: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")
    cep = input("CEP: ")
    return Medico(nome, senha, cpf, cep)


def criar_paciente():
    nome = input("Nome do Paciente: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")
    cep = input("CEP: ")
    return (nome, senha, cpf, senha)

admin = criar_administrador()

secretarios = []
Medicos = []
Pacientes = []

while True:

    print("\n Menu principal.")
    print("\n 1. Login como Adiministrador \n 2. Login como Secretário(a) \n 3. Login como Médico(a) \n 4. Login como Paciente \n 5. Sair")

    escolha = int(input("\n Escolha uma opção: "))
    match escolha:
        case 1:
            senha = input ("\n Senha do administrador: ")

            if admin.autenticar(senha):
                print("\n Senha inválida")

            else:
                while True:
                    print("\n Bem vindo Administrador!")
                    print("\n Menu Administrador")
                    print("\n 1. Adicionar Secretário(a) \n 2. Ver Secretários(as) \n 3. Voltar")

                    sub_escolha = int(input("\n Escolha uma opção: "))
                    match sub_escolha:
                        case 1:
                            sec = criar_secretaria()
                            secretarios.append(sec)
                            admin.adicionar_secretario(sec)
                            print(f'')
                        case 2:
                            for secretario in secretarios:
                                print(f'\n Secretário: {secretario}')
                        case 3:
                            print("\n Voltando...")
                            break
                        case _:
                            print("\n Opção inválida.")

        case 2:
            senha = input("\n Senha do Secretário(a): ")
            if senha != "sec":
                print("Senha inválida")
            else:
                while True:
                    print("\n Bem vindo Secretário(a)!")
                    print("\n Menu Secretário(a)")
                    print("\n 1. Adicionar Medico(a) \n 2. Adicionar Paciente \n 3. Buscar Medico \n 4. Buscar Paciente  \n 5. Verificar agenda médica \n 6. Marcar compromisso \n 7. Marcar exames \n 8. Marcar consulta \n 9. Buscar exames \n 10. Buscar consultas \n 11. Cadastrar convenio \n 12. Buscar convenio \n 13. Emitir Relatorio \n 14. Sair ")

                    sub_escolha = int(input("\n Escolha uma opção: "))
                    match sub_escolha:
                        case 1:
                            print("\n Médico adicionado")
                        case 2:
                            print("\n Paciente adicionado")
                        case 3:
                            print("\n Médico fulano")
                        case 4:
                            print("\n Paciente ciclano")
                        case 5:
                            print("\n Agenda médica: ")
                        case 6:
                            print("\n Compromisso marcado")
                        case 7:
                            print("\n Exame marcado")
                        case 8:
                            print("\n Consulta marcada")
                        case 9:
                            print("\n Exame buscado")
                        case 10:
                            print("\n Consulta buscada")
                        case 11:
                            print("\n Convênio cadastrado")
                        case 12:
                            print("Convenio do Paciente")
                        case 13:
                            print("\n Relatório emitido")
                        case 14:
                            print("\n Saindo...")
                            break
                        case _:
                            print("\n Opção inválida.")
        case 3:
            senha = input("\n Senha do Médico: ")
            if senha != "doctor":
                print("\n Senha inválida")
            else:
                while True:
                    print("\n Bem vindo Médico(a)!")
                    print("\n Menu Médico(a)")
                    print("\n 1. Realizar exames \n 2. Agendar consulta \n 3. Consultar tabela CID \n 4. Transcrever medicamentos \n 5. Sair")
                    sub_escolha = int(input("\n Escolha uma opção: "))
                    match sub_escolha:
                        case 1:
                            print("\n Exame realizado")
                        case 2:
                            print("\n Consulta agendada")
                        case 3:
                            print("\n Tabela CID consultada")
                        case 4:
                            print("\n Medicamentos transcritos")
                        case 5:
                            print("\n Saindo... ")
                            break


        case 4:
            senha = input("\n Senha do Paciente: ")
            if senha != "paz":
                print("\n Senha inválida")
            else:
                while True:
                    print("\n Bem vindo Paciente!")
                    print("\n Menu Paciente")
                    print("\n 1. Verificar exames \n 2. verificar medicamentos \n 3. verificar agenda \n 4. Sair")
                    sub_escolha = int(input("\n Escolha uma opção: "))
                    match sub_escolha:
                        case 1:
                            print("\n Exames verificados")
                        case 2:
                            print("\n Medicamentos verificados")
                        case 3:
                            print("\n Agenda verificada")
                        case 4:
                            print("\n Saindo...")
                            break

        case 5:
            print("\n Saindo...")
            break

        case _:
            print("\n Opção inválida")