import os
import sys
import requests
import datetime
import logging

date_inicial = datetime.date.today()
date_final = date_inicial
stone_code = None

logging.basicConfig(filename='STONE'+date_inicial.strftime('%Y%m%d')+'.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

params = {
    'Authorization': 'xxxx',
    'X-Authorization-Raw-Data': 'xxxx',
    'X-Authorization-Encrypted-Data': 'xxxx',
    'Accept': 'application/xml'
}
    
def stone_massive_download():
    try:
        data = list_stones_code()
        date_inicial = sys.argv[2]
        date_final = sys.argv[3]
        os.chdir(sys.argv[4])
        days_range = datetime.datetime.strptime(date_final, '%Y%m%d') - datetime.datetime.strptime(date_inicial, '%Y%m%d')
    except Exception as e:
        print('\nPor favor Forncer os argumentos na ordem Data inicial, Data final, directory exemplo:\n20190627 20190627 c:\stone', e)
        return None
    
    for i in range(0, days_range.days+1, 1):
        current_date = datetime.datetime.strptime(date_inicial, '%Y%m%d')+ datetime.timedelta(i)
        current_date = current_date.strftime('%Y%m%d')
        for codes in data:
            code, filename, days = codes.split(',')
            response = requests.get(f'https://conciliation.stone.com.br/conciliation-file/v2.2/{current_date}?affiliationCode={code}', headers=params)
            file_name = current_date+filename.strip()
            write_file(response, current_date, filename, code)
    
def stone_recovery_code():
    try:
        data = list_stones_code()
        date_inicial = sys.argv[2]
        date_final = sys.argv[3]
        stone_code = sys.argv[4]
        days_range = datetime.datetime.strptime(date_final, '%Y%m%d') - datetime.datetime.strptime(date_inicial, '%Y%m%d')
        os.chdir(sys.argv[5])
    except Exception as e: 
        print('\nPor favor Forncer os argumentos na ordem Data inicial, Data final e Stone Code exemplo:\n20190627 20190627 999999999 c:\stone', e)
        return None

    for codes in data:
        code, filename, days = codes.split(',')
        if code == stone_code:
            for i in range(0, days_range.days+1, 1):
                current_date = datetime.datetime.strptime(date_inicial, '%Y%m%d')+ datetime.timedelta(i)
                current_date = current_date.strftime('%Y%m%d')
                response = requests.get(f'https://conciliation.stone.com.br/conciliation-file/v2.2/{current_date}?affiliationCode={code}', headers=params)
                file_name = current_date+filename.strip()
                write_file(response, current_date, filename, code)
            
def diary_download():
    try:
        data = list_stones_code()
        os.chdir(sys.argv[2])
    except Exception as e:
        print('\n Erro ao executar download diário', e)
        return None

    for codes in data:
        code, filename, days = codes.split(',')
        current_date = date_inicial - datetime.timedelta(int(days))
        current_date = current_date.strftime('%Y%m%d')
        response = requests.get(f'https://conciliation.stone.com.br/conciliation-file/v2.2/{current_date}?affiliationCode={code}', headers=params)
        write_file(response, current_date, filename, code)

def list_stones_code():
    os.chdir('C:/Users/Miqueas/Desktop/Python/stone-files')
    with open('stone-codes.txt', 'r') as stonecodes:
        data = list(stonecodes)
    return data

def write_file(response, current_date, filename, code):
    file_name = current_date+filename.strip()
    if response.status_code == requests.codes.ok:
        with open(file_name+'.xml', 'w') as outfile:
            outfile.write(response.text)
            logging.info('Download with success Stone code:{} Date:{} filename:{} Status request: {}'.format(code, current_date, file_name, response.status_code))
    else:
        logging.error('Error while Download Stone code:{} Date:{} filename:{} Status request: {} message: {}'.format(code, current_date, file_name, response.status_code, response.text))


if sys.argv[1] == 'r':
    stone_recovery_code()
elif sys.argv[1] == 'rm':
    stone_massive_download()
elif sys.argv[1] == 'n':
    diary_download()


