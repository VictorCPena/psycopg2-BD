import psycopg2

# Criando Conexão com o banco de Dados

while True:
    try:
        host = input('Digite o Host: ')
        user = input('Digite o Username: ')
        password = input('Digite o Password: ')
        database = input('Digite o Database: ')
        port = input('Digite a Port: ')
        conn = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
        break
    except:
        print('Erro na Conexão! os Dados Colocados Não Estão Certos')
        bd = str(input("Deseja Tentar Novamente?(sim/não) "))
        bd = bd.lower()
        if bd == 'sim':
            print('Ok, digite novamente(verifique se os dados colocados estão certos)')
        else:
            print('Ok, saindo...')
            conn.close()
            print("A conexão com o banco foi encerrada.")
            exit()
            break

# Fazendo os Trabalhos no Banco de Dados

cur = conn.cursor()

print('Qual operação deseja fazer?')
while True:
    print('Create, Insert, Select, Update, Delete? (para sair digite "N")')
    print('Se quiser escrever em SQL digite "SQL"')
    bd = input('')
    try:
        if bd == 'Create' or 'create':
            print('Digite o nome que deseja para a Tabela')
            c = input('')
            print('Agora digite seus Parâmetros e seu tipo(ex: varchar, int...)')
            p = input('')
            cur.execute(f'CREATE TABLE {c}({p})')
            conn.commit()
    except:
        print('Tem algo errado')
        db = str(input('Deseja Tentar Novamente?(S/N)'))
        db = db.lower()
        if db == 'sim' or 's':
            print('Ok, digite os valores novamente')
        else:
            break

    try:
        if bd == 'Insert' or 'insert':
            print('Digite o nome da tabela')
            b = input('')
            print('Digite seus Parâmetros')
            p = input('')
            print('Agora digite os valores para os Parâmetros passados acima: ')
            print('Escreva as Palavras entre Parênteses')
            v = input('')
            cur.execute(f'INSERT INTO {b}({p}) VALUES ({v})')
            conn.commit()
    except:
        print('Tem algo errado')
        db = str(input('Deseja Tentar Novamente?(S/N)'))
        db = db.lower()
        if db == 'sim' or 's':
            print('Ok, digite os valores novamente')
        else:
            break

    try:
        if bd == 'Select' or 'select':
            print("Digite o nome da Tabela")
            res = input('')
            cur.execute(f'SELECT * FROM {res}')
            resultado = cur.fetchall()
            print(resultado)
    except:
        print('Tem algo errado')
        db = str(input('Deseja Tentar Novamente?(S/N)'))
        db = db.lower()
        if db == 'sim' or 's':
            print('Ok, digite os valores novamente')
        else:
            break

    try:
        if bd == 'Update' or 'update':
            print('Digite em SQL o Update que deseja fazer: ')
            b = input('')
            cur.execute(b)
            conn.commit()
    except:
        print('Tem algo errado')
        db = str(input('Deseja Tentar Novamente?(S/N)'))
        db = db.lower()
        if db == 'sim' or 's':
            print('Ok, digite novamente(verifique se o SQL certo)')
        else:
            break

    try:
        if bd == 'Delete' or 'delete':
            print('Digite em SQL o que deseja Deletar')
            print('Para Deletar Tabelas use o Comando "DROP TABLE + O nome da Tabela que Deseja Deletar"')
            d = input('')
            cur.execute(d)
            conn.commit()
    except:
        print('Tem algo errado')
        db = str(input('Deseja Tentar Novamente?(S/N)'))
        db = db.lower()
        if db == 'sim' or 's':
            print('Ok, digite novamente(verifique se o SQL certo)')
        else:
            break

    try:
        if bd == 'SQL' or 'sql':
            print('digite o SQL')
            s = input('')
            cur.execute(s)
            conn.commit()
    except psycopg2.errors.DuplicateTable:
        print('Opa Tupla já feita')
        db = str(input('Deseja Criar outra?(S/N)'))
        db = db.lower()
        if db == 'sim' or 's':
            print('Ok, digite o SQL')
        else:
            break
    except:
        print('Algo que você escreveu está errado, Tente Novamente')
        db = str(input('Deseja Tentar Novamente?(S/N)'))
        db = db.lower()
        if db == 'sim' or 's':
            print('Ok, digite novamente(verifique se o SQL está certo)')
        else:
            break

    if bd == 'N' or 'n':
        print('ok, saindo...')
        break
    else:
        print('Operação Feita com Sucesso!')
        print('Deseja fazer outra operação?(S/N)')
        o = input('')
        o = o.lower()
        if o == 'sim' or 's':
            continue
        else:
            print('Ok, Saindo...')
            conn.close()
            print("A conexão com o Banco foi Encerrada.")
            break
