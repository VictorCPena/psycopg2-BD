import psycopg2

# Criando Conexão com o banco de Dados

bd = str(input("Deseja Fazer uma Conexão com banco de Dados?(sim/não)"))
bd = bd.lower()
if bd == "sim":
    print("Ok")
else:
    print("Ok, saindo...")
    exit()

host=input('Digite o host: ')
user=input('Digite o username: ')
password=input('Digite o password: ')
database=input('Digite o database: ')
port=input('Digite a port: ')

try:
 conn = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
except psycopg2.OperationalError:
    print('erro na conexão, tente novamente(verifique se os dados colocados estão certos)')
    exit()

print('Conectado com sucesso.')

cursor = conn.cursor()

# Criando o SQL(digite em SQL)


def sql_criar():
    print("digite seu Código SQL Novamente: ")
    conn
    sql_tentativa = input()
    cursor.execute(sql_tentativa)
    conn.commit()
    print(cursor.statusmessage)


try:
 print("digite seu Código SQL: ")
 sql = input()
 data = cursor.execute(sql)
except psycopg2.errors.SyntaxError:
    print("algo que você está errado, tente novamente")
    conn.commit()
    sql_criar()


# Fechando Conexão


conn.close()
