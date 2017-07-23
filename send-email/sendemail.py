
#!/usr/bin/env python
# -*- encoding: utf-8 -*- 


def sendemail(conf, data):
    """ 
method to send e-mail

conf = [from, pass, urlServer, port]
data = [[to], subj, msg, cc, bcc]

sendemail(conf, data)  -->  send email
    """
    
    # biblioteca permite envio emails
    import smtplib

    # a classe 'email.mime.' aumenta as opcoes disponiveis para email - subject, anexos multimedia, ...
    from email.mime.text import MIMEText

    # smtp = smtplib.SMTP_SSL('enderecoSMTPmail', nrPorta)
    smtp = smtplib.SMTP_SSL(conf[2], conf[3])
    # smtp.login('emailUtilizador', 'palavraChave')
    smtp.login(conf[0], conf[1])


    de = conf[0]
    # para | destinatario tem de ser uma lista msemo que seja apenas um 
    # ['emailUtilizador'] ou ['emailUtilizador1', 'emailUtilizador2']
    para = data[0]


    # adicionando dados (do cabecalho) de envio do email
    # email dividido em partes, dentro do objecto msg - msg, msg[From'], msg['Subject'], ...
    # texto do email em html e codificacao
    msg = MIMEText(data[2], 'html', 'utf-8')
    msg['From'] = de
    # concatena a lista de emails destinatarios do email
    msg['To'] = ', '.join(para) 

    # indica quem recebera uma copia deste email
    #msg['Cc'] = ''
    # indica quem recebera uma copia do email, mas as demais pessoas nao irao ver o email dele na lista dos enviados
    #msg['Bcc'] = ''
    # indica para quem sera respondido o email
    #msg['Reply-To] = ''

    msg['Subject'] = data[1]
    # converte 
    raw = msg.as_string()


    # smtp.sendmail('enderecoEmailEmissor', ['enderecoEmailDestinatario1', ...], mensagem)
    smtp.sendmail(de, para, raw)

    smtp.quit()



if __name__ == '__main__':
    print(sendemail.__doc__)
