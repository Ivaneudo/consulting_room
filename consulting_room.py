# Classe base User, representando um usuário do sistema
class User:
    def __init__(self, nome, idade, cpf, cep, senha):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cep = cep
        self.senha = senha

    # Método para autenticar um usuário com base em CPF e senha
    def autenticar(self, senha, cpf):
        return self.senha == senha and self.cpf == cpf

# Classe Admin, derivada de User, representando o administrador do sistema
class Admin(User):
    def __init__(self, nome, idade, cpf, cep, cnpj, senha):
        super().__init__(nome, idade, cpf, cep, senha)
        self.cnpj = cnpj
        self.secretarios = []

    # Adiciona um secretário à lista de secretários
    def adicionar_secretario(self, secretario):
        self.secretarios.append(secretario)
        print(f'Secretário(a) {secretario.nome} adicionado(a).')

    # Lista todos os secretários cadastrados
    def listar_secretarios(self):
        if self.secretarios:
            print('Secretários(as):')
            for secretario in self.secretarios:
                print(f'- {secretario.nome}')
        else:
            print('Nenhum secretário(a) cadastrado(a).')

# Classe Secretario, derivada de User, representando um secretário no sistema
class Secretario(User):
    def __init__(self, nome, idade, cpf, cep, senha, num_id):
        super().__init__(nome, idade, cpf, cep, senha)
        self.num_id = num_id
        self.pacientes = []
        self.medicos = []
        self.agenda_medica = []

    # Adiciona um médico à lista de médicos
    def adicionar_medico(self, medico):
        self.medicos.append(medico)
        print(f'Médico {medico.nome} adicionado.')

    # Adiciona um paciente à lista de pacientes
    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print(f'Paciente {paciente.nome} adicionado.')

    # Busca um médico pelo nome
    def busca_medico(self, nome):
        for medico in self.medicos:
            if medico.nome == nome:
                return medico
        return None

    # Busca um paciente pelo nome
    def busca_paciente(self, nome):
        for paciente in self.pacientes:
            if paciente.nome == nome:
                return paciente
        return None

    # Verifica a agenda médica
    def verificar_agenda_medica(self):
        return self.agenda_medica

    # Marca um compromisso na agenda médica
    def marcar_compromisso(self, compromisso):
        self.agenda_medica.append(compromisso)
        print(f'Compromisso {compromisso} marcado.')

    # Marca um exame para um paciente com um médico específico
    def marcar_exame(self, nome_paciente, exame, nome_medico):
        paciente = self.busca_paciente(nome_paciente)
        medico = self.busca_medico(nome_medico)
        if paciente and medico:
            paciente.exames.append(exame)
            medico.exames.append(exame)
            print(f'Exame {exame} marcado para {paciente.nome} com o médico {medico.nome}.')
        else:
            print('Paciente ou Médico não encontrado.')

    # Marca uma consulta para um paciente com um médico específico
    def marcar_consulta(self, nome_paciente, consulta, nome_medico):
        paciente = self.busca_paciente(nome_paciente)
        medico = self.busca_medico(nome_medico)
        if paciente and medico:
            paciente.consultas.append(consulta)
            print(f'Consulta {consulta} marcada para {paciente.nome} com o médico {medico.nome}.')
        else:
            print('Paciente ou Médico não encontrado.')

    # Busca exames de um paciente
    def busca_exames(self, paciente):
        return paciente.exames

    # Busca consultas de um paciente
    def busca_consultas(self, paciente):
        return paciente.consultas

    # Cadastra um convênio para um paciente
    def cadastra_convenio(self, paciente, convenio):
        paciente.convenio = convenio
        print(f'Convênio {convenio} cadastrado para {paciente.nome}.')

    # Busca o convênio de um paciente
    def busca_convenio(self, paciente):
        return paciente.convenio

    # Emite um relatório dos pacientes e médicos cadastrados
    def emitir_relatorio(self):
        print(f'Relatório da secretária {self.nome}')
        print('Pacientes:')
        for paciente in self.pacientes:
            print(paciente.nome)
        print('Médicos:')
        for medico in self.medicos:
            print(medico.nome)

# Classe Medico, derivada de User, representando um médico no sistema
class Medico(User):
    def __init__(self, nome, idade, cpf, cep, senha, medicamentos=None, exames=None):
        super().__init__(nome, idade, cpf, cep, senha)
        self.medicamentos = medicamentos if medicamentos is not None else []
        self.exames = exames if exames is not None else []

    # Realiza cirurgias (função placeholder)
    def realizar_cirurgias(self):
        print(f'{self.nome} está realizando cirurgias.')

    # Realiza exames para um paciente
    def realizar_exames(self, secretario, nome_paciente, exame):
        paciente = secretario.busca_paciente(nome_paciente)
        if paciente:
            paciente.exames.append(exame)
            print(f'Exame {exame} realizado para {paciente.nome}.')
        else:
            print('Paciente não encontrado.')

    # Emite um relatório de exames realizados
    def emitir_relatorio_de_exame(self):
        print(f'Relatório de exame por {self.nome}:')
        for exame in self.exames:
            print(exame)

    # Agenda uma consulta para um paciente
    def agendar_consulta(self, secretario, nome_paciente, consulta):
        paciente = secretario.busca_paciente(nome_paciente)
        if paciente:
            paciente.consultas.append(consulta)
            print(f'Consulta {consulta} agendada para {paciente.nome}.')
        else:
            print('Paciente não encontrado.')

    # Prescreve um medicamento para um paciente, verificando disponibilidade na farmácia
    def prescrever_medicamento(self, secretario, farmacia, nome_paciente, medicamento):
        paciente = secretario.busca_paciente(nome_paciente)
        if paciente:
            if farmacia.verificar_disponibilidade(medicamento):
                paciente.medicamentos.append(medicamento)
                print(f'Medicamento {medicamento} prescrito para {paciente.nome}.')
            else:
                print(f'Medicamento {medicamento} não disponível na farmácia.')
        else:
            print('Paciente não encontrado.')

# Classe Paciente, derivada de User, representando um paciente no sistema
class Paciente(User):
    def __init__(self, nome, idade, cpf, cep, senha):
        super().__init__(nome, idade, cpf, cep, senha)
        self.exames = []
        self.consultas = []
        self.medicamentos = []
        self.convenio = None

# Classe Farmacia, representando uma farmácia que gerencia medicamentos
class Farmacia:
    def __init__(self):
        self.medicamentos = {}

    # Adiciona um medicamento ao estoque da farmácia
    def adicionar_medicamento(self, nome, quantidade):
        if nome in self.medicamentos:
            self.medicamentos[nome] += quantidade
        else:
            self.medicamentos[nome] = quantidade

    # Verifica se um medicamento está disponível na farmácia
    def verificar_disponibilidade(self, nome):
        return self.medicamentos.get(nome, 0) > 0

    # Remove uma quantidade de medicamento do estoque da farmácia
    def remover_medicamento(self, nome, quantidade):
        if self.verificar_disponibilidade(nome):
            if self.medicamentos[nome] >= quantidade:
                self.medicamentos[nome] -= quantidade
                return True
        return False

# Função para adicionar medicamento na farmácia
def operar_farmacia_adicionar(farmacia):
    nome = input("Nome do medicamento: ")
    quantidade = int(input("Quantidade: "))
    farmacia.adicionar_medicamento(nome, quantidade)
    print(f'Medicamento {nome} adicionado à farmácia com {quantidade} unidades.')

# Função para remover medicamento da farmácia
def operar_farmacia_remover(farmacia):
    nome = input("Nome do medicamento: ")
    quantidade = int(input("Quantidade a remover: "))
    if farmacia.remover_medicamento(nome, quantidade):
        print(f'{quantidade} unidade(s) de {nome} removida(s) da farmácia.')
    else:
        print(f'Não foi possível remover {quantidade} unidade(s) de {nome} da farmácia.')

# Função para criar um administrador
def criar_administrador():
    nome = "Admin"
    idade = 35
    cpf = "12345678901"
    cep = "00000000"
    cnpj = "12345678000100"
    senha = "root"
    return Admin(nome, idade, cpf, cep, cnpj, senha)

# Função para criar uma secretária
def criar_secretaria():
    nome = input("Nome da Secretária: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    cep = input("CEP: ")
    num_id = input("Número de Identificação: ")
    senha = input("Senha: ")
    return Secretario(nome, idade, cpf, cep, senha, num_id)

# Função para criar um médico
def criar_medico():
    nome = input("Nome do Médico: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    cep = input("CEP: ")
    senha = input("Senha: ")
    return Medico(nome, idade, cpf, cep, senha)

# Função para criar um paciente
def criar_paciente():
    nome = input("Nome do Paciente: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    cep = input("CEP: ")
    senha = input("Senha: ")
    return Paciente(nome, idade, cpf, cep, senha)

# Inicializa a farmácia
farmacia = Farmacia()
# Inicializa o administrador
admin = criar_administrador()

# Listas para armazenar secretários, médicos e pacientes
secretarios = []
medicos = []
pacientes = []

# Menu principal do sistema
while True:
    print("\nSistema de Gestão Hospitalar")
    print("\n1. Administrador \n2. Secretário(a) \n3. Médico(a) \n4. Paciente \n5. Operar farmacia \n6. Sair")
    escolha = int(input("\nEscolha uma opção: "))

    match escolha:
        case 1:
            cpf = input("\nDigite seu CPF: ")
            senha = input("\nDigite sua senha: ")
            # Verifica se o cpf e a senha são os mesmos cadastrados no admin
            if admin.autenticar(senha, cpf):
                # Menu Administrador
                while True:
                    print("\nBem-vindo Administrador!")
                    print("\nMenu Administrador")
                    print("\n1. Adicionar Secretário(a) \n2. Listar Secretários(as) \n3. Sair")
                    sub_escolha = int(input("\nEscolha uma opção: "))

                    match sub_escolha:
                        case 1:
                            secretario = criar_secretaria()
                            secretarios.append(secretario)
                            admin.adicionar_secretario(secretario)
                        case 2:
                            admin.listar_secretarios()
                        # Interrompe a execução do loop 
                        case 3:
                            print("\nSaindo...")
                            break
                        case _:
                            print("\nOpção inválida.")
            else:
                print("\nCPF ou senha inválidos.")

        case 2:
            cpf = input("\nDigite seu CPF: ")
            senha = input("\nDigite sua senha: ")
            # Olha cada secretario na lista secretarios
            for secretario in secretarios:
                # Verifica se o cpf e a senha são os mesmos cadastrados no secretarios
                if secretario.autenticar(senha, cpf):
                    # Menu Secretário(a)
                    while True:
                        print(f'\nBem-vindo Secretário(a) {secretario.nome}!')
                        print("\nMenu Secretário(a)")
                        print("\n1. Adicionar Médico(a) \n2. Adicionar Paciente \n3. Buscar Médico(a) \n4. Buscar Paciente \n5. Verificar Agenda Médica \n6. Marcar Compromisso \n7. Marcar Exame \n8. Marcar Consulta \n9. Buscar Exames \n10. Buscar Consultas \n11. Cadastrar Convênio \n12. Buscar Convênio \n13. Emitir Relatório \n14. Sair")
                        sub_escolha = int(input("\nEscolha uma opção: "))

                        match sub_escolha:
                            case 1:
                                medico = criar_medico()
                                medicos.append(medico)
                                secretario.adicionar_medico(medico)
                            case 2:
                                paciente = criar_paciente()
                                pacientes.append(paciente)
                                secretario.adicionar_paciente(paciente)
                            case 3:
                                nome = input("Nome do Médico: ")
                                medico = secretario.busca_medico(nome)
                                if medico:
                                    print(f'Médico encontrado: {medico.nome}')
                                else:
                                    print('Médico não encontrado.')
                            case 4:
                                nome = input("Nome do Paciente: ")
                                paciente = secretario.busca_paciente(nome)
                                if paciente:
                                    print(f'Paciente encontrado: {paciente.nome}')
                                else:
                                    print('Paciente não encontrado.')
                            case 5:
                                print(f'Agenda médica: {secretario.verificar_agenda_medica()}')
                            case 6:
                                compromisso = input("Compromisso: ")
                                secretario.marcar_compromisso(compromisso)
                            case 7:
                                nome_paciente = input("Nome do Paciente: ")
                                exame = input("Exame: ")
                                nome_medico = input("Nome do Médico: ")
                                secretario.marcar_exame(nome_paciente, exame, nome_medico)
                            case 8:
                                nome_paciente = input("Nome do Paciente: ")
                                consulta = input("Consulta: ")
                                nome_medico = input("Nome do Médico: ")
                                secretario.marcar_consulta(nome_paciente, consulta, nome_medico)
                            case 9:
                                nome = input("Nome do Paciente: ")
                                paciente = secretario.busca_paciente(nome)
                                if paciente:
                                    print(f'Exames de {paciente.nome}: {secretario.busca_exames(paciente)}')
                                else:
                                    print('Paciente não encontrado.')
                            case 10:
                                nome = input("Nome do Paciente: ")
                                paciente = secretario.busca_paciente(nome)
                                if paciente:
                                    print(f'Consultas de {paciente.nome}: {secretario.busca_consultas(paciente)}')
                                else:
                                    print('Paciente não encontrado.')
                            case 11:
                                nome = input("Nome do Paciente: ")
                                convenio = input("Convênio: ")
                                paciente = secretario.busca_paciente(nome)
                                if paciente:
                                    secretario.cadastra_convenio(paciente, convenio)
                                else:
                                    print('Paciente não encontrado.')
                            case 12:
                                nome = input("Nome do Paciente: ")
                                paciente = secretario.busca_paciente(nome)
                                if paciente:
                                    print(f'Convênio de {paciente.nome}: {secretario.busca_convenio(paciente)}')
                                else:
                                    print('\nPaciente não encontrado.')
                            case 13:
                                secretario.emitir_relatorio()
                            # Interrompe a execução do loop 
                            case 14:
                                print("\nSaindo...")
                                break
                            case _:
                                print("\nOpção inválida.")
                else:
                    print("\nCPF ou senha inválidos.")

        case 3:
            cpf = input("\nDigite seu CPF: ")
            senha = input("\nDigite sua senha: ")
            # Olha cada médico na lista medicos
            for medico in medicos:
                # Verifica se o cpf e a senha são os mesmos cadastrados no medicos
                if medico.autenticar(senha, cpf):
                    # Menu Médico
                    while True:
                        print(f'\nBem-vindo Médico(a) {medico.nome}!')
                        print("\nMenu Médico(a)")
                        print("\n1. Realizar exames \n2. Agendar consulta \n3. Consultar tabela CID \n4. Transcrever medicamentos \n5. Prescrever Medicamento para Paciente \n6. Sair")
                        sub_escolha = int(input("\nEscolha uma opção: "))

                        match sub_escolha:
                            case 1:
                                nome_paciente = input("Nome do Paciente: ")
                                exame = input("Exame: ")
                                medico.realizar_exames(secretario, nome_paciente, exame)
                            case 2:
                                nome_paciente = input("Nome do Paciente: ")
                                consulta = input("Consulta: ")
                                medico.agendar_consulta(secretario, nome_paciente, consulta)
                            case 3:
                                print("\nTabela CID consultada.")
                            case 4:
                                medicamento = input("\nMedicamento: ")
                                medico.medicamentos.append(medicamento)
                                print("\nMedicamento transcrito.")
                            case 5:
                                nome_paciente = input("Nome do Paciente: ")
                                medicamento = input("Medicamento: ")
                                medico.prescrever_medicamento(secretario, farmacia, nome_paciente, medicamento)
                            # Interrompe a execução do loop 
                            case 6:
                                print("\nSaindo...")
                                break
                            case _:
                                print("\nOpção inválida.")
                    break
                else:
                    print("\nCPF ou senha inválidos.")

        case 4:
            cpf = input("\nDigite seu CPF: ")
            senha = input("\nDigite sua senha: ")
            # Olha cada paciente na lista pacientes
            for paciente in pacientes:
                # Verifica se o cpf e a senha são os mesmos cadastrados no admin
                if paciente.autenticar(senha, cpf):
                    # Menu Paciente 
                    while True:
                        print(f'\nBem-vindo Paciente {paciente.nome}!')
                        print("\nMenu Paciente")
                        print("\n1. Verificar exames \n2. Verificar medicamentos \n3. Verificar agenda \n4. Sair")
                        sub_escolha = int(input("\nEscolha uma opção: "))

                        match sub_escolha:
                            case 1:
                                print(f'\nExames: {paciente.exames}')
                            case 2:
                                print(f'\nMedicamentos: {paciente.medicamentos}')
                            case 3:
                                print(f'\nAgenda: {paciente.consultas}')
                            # Interrompe a execução do loop 
                            case 4:
                                print("\nSaindo...")
                                break
                            case _:
                                print("\nOpção inválida.")
                else:
                    print("\nCPF ou senha inválidos.")

        case 5:
            while True:
                # Menu Farmácia
                print("\nMenu de Operação da Farmácia:")
                print("1. Adicionar Medicamento \n2. Remover Medicamento \n3. Voltar ao Menu Principal")

                operacao_farmacia = input("Escolha uma operação: ")

                if operacao_farmacia == "1":
                    operar_farmacia_adicionar(farmacia)
                elif operacao_farmacia == "2":
                    operar_farmacia_remover(farmacia)
                # Interrompe a execução do loop 
                elif operacao_farmacia == "3":
                    break
                else:
                    print("Opção inválida. Por favor, escolha novamente.")
        case 6:
            # Interrompe a execução do loop 
            print("\nSaindo...")
            break

        case _:
            print("\nOpção inválida.")