saldototal = 0

def cadastrar():
    nome =input("informe seu nome:")
    while(len(nome)<3):
        print ( "O nome possui menos de tres letras" )
        nome =input("Informe seu nome, no mínimo 3 letras: ")
    sobrenome = input("Informe seu sobrenome : ")
    while(len(sobrenome)<3):
        print ( "O sobrenmoe possui menos de tres letras" )
        sobrenome =input("Informe seu sobrenome, no mínimo 3 letras: ")
    endereco = input("Informe seu endereço : ")
    senha = input("Sua senha: ")
    while ((len(senha)<5 ) or (senha.isalnum() == True or senha.isalpha() == True )):
        senha = input("Digite novamente a senha:")
    celular = int(input("Informe seu número de telefone : "))
    cpf = int(input("Informe seu CPF : "))
    contador  =  0
    while(contador == 0):
        email = input("Informe seu E-mail : ")
        if "@" in email :
            print("E-mail cadastrado")
            contador = 1

def  opcoes():
    sacar  =  0
    saldoTotal  =  0
    caixa  =  1
    contaTransferencia  =  0
    while  caixa  ==  1 :
    
        print ( "Digite 1 para efetuar um deposito!" )
        print ( "Digite 2 para efetuar um saque!" )
        print ( "Digite 3 para exibir saldo!" )
        print ( "Digite 4 para efetuar download!" )
        print ( "Digite 5 para encerrar conta!" )    
        operacao  =  int ( input ( "Operação:"))
    
    if  operacao  ==  1 :
        depositar  =  int ( input ( "Digite o valor do depósito:" ))
        while  depositar  <  0 :
             depositar  =  int ( input ( "O depósito deve ser de mais de 0R $:" ))
             print ( "Seu saldo atual é:" , saldototal )
    else :
        saldototal  =  depositar  +  saldototal
        print ( "Seu saldo atual é:" , saldototal )
    if  operacao  ==  2 :
        sacar  =  float ( input ( "Digite o valor do saque:" ))
        while  sacar  >  saldototal :
            print ( "Voce não possui saldo suficiente para este saque! Insira um valor menor que:" , saldototal , "" )
        operacao  =  int ( input ( "Escolha outra operação:" ))
    else :
        saldototal  =  saldototal  -  sacar
        print ( "Seu saldo atual é:" , saldototal )      
    if  operacao  ==  3 :
            print ( "Seu saldo atual é:" , saldototal )    
    if  operacao  ==  4 :
     conta_transferencia  =  int ( input ( "Digite o endereço de conta para qual efetuar a transferência:" ))
     transferencia  =  int ( input ( "Digite o valor a ser transferido:" ))
    if  transferencia  >  saldototal :
         print ( "voce não possui saldo suficiente para essa tranferencia! Insira um valor menor que:" , saldototal , "" )
    else :
          saldototal  =  saldototal  -  transferencia 
          conta_transferencia  =  conta_transferencia  +  transferencia 
          print ( "tranferencia concluida com succeso:" )
          print ( "Seu novo saldo é de:" , saldototal )
    if  operacao  ==  5 :
        print ( "Operação encerrada!" )
        caixa  =  0 
            
def  novaParte ():
    operacao_2  =  0
    novoCadastro  =  0
    while ( novoCadastro  ==  0 ):
        print ( "Digite 1 para consultar um cliente" )
        print ( "Digite 2 para consultar uma lista de clientes" )
        print ( "Digite 3 para deletar um cliente" )
        print ( "Digite 4 para atualizar dados de um cliente específico" )
        print ( "Digite 5 para encerrar" )
        operacao_2  =  int ( input ( "escolha a operação:" ))
        if  operacao_2  ==  1 :
            numerocliente =  int ( input ( "Qual o numero do cliente no cadastro:" ))
            print ( "Nome cliente:" , nome [ numerocliente ])  
            print ( "Sobrenome cliente:" , sobrenome [ numerocliente ])
            print ( "Cpf cliente:" , cpf [ numerocliente ])
            print ( "E-mail do cliente:" , email [ numerocliente ])
            print ( "Endereço do cliente:" , endereco [ numerocliente ])
            print ( "Numero do cliente:" , celular [ numerocliente ])
            print ( "Senha do cliente:" , senha [ numerocliente ])
        if  operacao_2  ==  2 :
            print ( "Lista de clientes:" , nome )
        if  operacao_2  ==  3 :
            númeroexcluir  =  int ( input ( "Escreva o numero do cliente que voce deseja excluir:" ))
            del ( nome [ númeroexcluir ])
            del ( sobrenome [ númeroexcluir ])
            del ( cpf[ númeroexcluir ])
            del ( email [ númeroexcluir ])
            del ( endereco [ númeroexcluir ])
            del ( numero [ númeroexcluir ])
            del ( senha [ númeroexcluir ])
        
        if  operacao_2  ==  4 :
            cadastrolNovo  =  0
            numeroCliente = int ( input ( "Escreva o numero de cadastro do cliente que voce deseja modificar:" ))
            nome . insert ( numerocliente , ( input ( "Insira seu nome:" )))  
            while(len(nome)<3):
                 print ( "O nome possui menos de tres letras" )
                 nome =input("Informe seu nome, no mínimo 3 letras: ")
            sobrenome . inserir ( numerocliente , ( input ( "Insira seu sobrenome:" )))
            while(len(sobrenome)<3):
                print ( "O sobrenmoe possui menos de tres letras" )
                sobrenome =input("Informe seu sobrenome, no mínimo 3 letras: ")
            celular . insert ( numerocliente , ( input ( "Digite um número para contato:" )))
            cpf . insert ( numerocliente , ( input ( "Insira seu cpf:" )))
            endereco . insert ( numerocliente , ( input ( "insira seu endereço:" )))
            contadorr  =  0
            while(contadorr == 0):
                 email . append ( input ( "Digite seu email: " ))  
                 if "@" in email :
                    print("E-mail cadastrado")
                    contador = 1
            senha . anexar ( input ( "Digite sua senha, ela precisa conter caracteres especiais e numeros:" ))
            while ((len(senha)<5 ) or (senha.isalnum() == True or senha.isalpha() == True )):
                 senha = input("Digite novamente a senha:")
            if  operacao_2  ==  5 :
                novoCadastro =  novoCadastro  +  1
cadastrar ()
opcoes()
novaParte ()     