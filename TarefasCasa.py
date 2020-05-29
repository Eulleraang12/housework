import smtplib
from datetime import date, datetime
import schedule


casa0 = ['euller', '1berto', 'homem ','felipe','jonnyn']

casa1 = ['jonnyn','euller','1berto','homem ','felipe']

casa2 = ['felipe','jonnyn','euller','1berto','homem ']

casa3 = ['homem ','felipe','jonnyn','euller','1berto']

casa4 = ['1berto', 'homem ','felipe','jonnyn','euller']



tarefas = [
           'passar pano (2x) / pia (1x) ',
           'varrer (7x) / teto (1x)',
           'varanda (1x) / balcoes (2x) / mesinha (2x)',          
           'fogao (1x) / vidros (1x)',
           'air fry (1x) / lixo (3x)',
] 


email_to =  ("euller.eng@gmail.com",
            "humberto.almeidda@gmail.com",
            "Gabriel.homem.45@gmail.com",
            "jonathanbrianamorim@gmail.com",
            "jovemflla@hotmail.com"
)

def email(msg):
    email_from = "yagamigasai@gmail.com"

    smtp = "smtp.gmail.com"
    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(email_from, open('senha.txt').read().strip())

    server.sendmail(email_from, email_to, str(msg))

    server.quit()
    print("Sucesso ao enviar o email")

def jobs():
    
    now = datetime.now()
    lista = []

    arquivo = open("salvar.txt","r")
    nome = arquivo.read()
    arquivo.close()

    if nome == 'euller':
        casaT = casa0

        arquivo = open("salvar.txt","w")
        arquivo.write(str(casa0[4]))
        arquivo.close()
    
    if nome == 'jonnyn':
        casaT = casa1

        arquivo = open("salvar.txt","w")
        arquivo.write(str(casa0[3]))
        arquivo.close() 

    if nome == 'felipe':
        casaT = casa2

        arquivo = open("salvar.txt","w")
        arquivo.write(str(casa0[2]))
        arquivo.close() 

    if nome == 'homem ':
        casaT = casa3

        arquivo = open("salvar.txt","w")
        arquivo.write(str(casa0[1]))
        arquivo.close() 

    if nome == '1berto':
    
        casaT = casa4

        arquivo = open("salvar.txt","w")
        arquivo.write(str(casa0[0]))
        arquivo.close() 
        

    for x in range(5):
        msg = '{}  ------->  {}'.format(casaT[x], tarefas[x])
        lista.append(msg)

    enviar = "\t{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format('ENG_HOUSE - TAREFAS DA SEMANA' ,'-'*82,lista[0],\
        '-'*82,lista[1],'-'*82,lista[2],'-'*82,lista[3],'-'*82,lista[4],'-'*82)

    email(enviar)
 
schedule.every().sunday.at('21:09').do(jobs)
# schedule.every().second.do(jobs)



while True:
    schedule.run_pending() 