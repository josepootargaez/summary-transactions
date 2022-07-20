from collections import Counter
import csv
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import StringIO
import smtplib
from decouple import config

async def CalculateTransaction(correo='',file='',response=''):
    try:
        contents = await file.read()
        decoded = contents.decode()
        buffer = StringIO(decoded)
        csvReader = csv.DictReader(buffer)
        balance = 0
        totalCredit= 0
        averageCredit = 0
        totalDebit= 0
        averageDebit = 0
        transactions= [];
        for rows in csvReader:
            if rows["Transaction"] and rows["Date"]:        
                balance = balance + float(rows["Transaction"])  
                index = rows["Date"].split('/');
                index =index[0];
                transactions.append(index);
                if rows["Transaction"].count('+') >= 1:
                    totalCredit= totalCredit +1
                    averageCredit = averageCredit + float(rows["Transaction"])
                if rows["Transaction"].count('-') >= 1:
                    totalDebit= totalDebit +1
                    averageDebit = averageDebit + float(rows["Transaction"])
        averageCredit = averageCredit / totalCredit;
        averageDebit = averageDebit / totalDebit;
        conteo=Counter(transactions)
        resultado={}
        for clave in conteo:  
            valor=conteo[clave]
            if valor != 0:
                x = datetime.datetime(2022, int(clave), 1)
                resultado[x.strftime("%B")] = valor
        await emails(correo,averageCredit,averageDebit,balance,resultado)
        buffer.close()
        return {"success": "true"}
    except:
        return {"error":"format invalid"}


async def emails(correo="",averageCredit=0,averageDebit=0,balance=0,resultado={}):
    month=''
    for res in resultado:
        month= f"{month} <p>Number of transactions in {res}: {resultado[res]}</p>"
    msg = MIMEMultipart()
    msg['From'] = config("EMAIL_MAIL");
    msg['To'] = correo.correo
    msg['Subject'] = "Summary transactions account"
    style='''<style>
        body{
            background: rgb(249, 248, 248);
            color: rgb(56, 73, 103);
            font-weight: bold;
        }
        .head{
            background: rgb(0, 199, 177);
            padding: 10px;
        }
        .mt-15{
            margin-top:15px
        }
        .p-10{
            padding: 10px;
        }
    </style>''';
    html = f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transactions</title>
    
</head>
{style}
<body>
    <div class="head">
        <h2>Summary transactions account</h2>
    </div>
           <div class="p-10">
                <p>balance: {balance}</p>
                <p>Average debit amount: {averageDebit}</p>
                <p>Average credit amount: {averageCredit}</p>
                {month}
           </div>
    <div class="head mt-15">
        <p>More information : Contact Us</p>
    </div>
</body>
</html>
    '''
    msg.attach(MIMEText(html, "html"))
    # Convert it as a string
    s = smtplib.SMTP(config("EMAIL_SMTP"),config("EMAIL_PORT"))
    s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
    s.starttls() #Puts connection to SMTP server in TLS mode
    s.ehlo()
    s.login(config("EMAIL_MAIL"), config("EMAIL_PASSWORD"))

    s.sendmail(config("EMAIL_MAIL"), correo.correo, msg.as_string())

    s.quit()
