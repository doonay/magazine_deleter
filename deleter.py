import datetime
# import logging
import pyodbc


def logger(message):
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    with open('app.log', 'a', encoding='utf-8') as f:
        f.write(str(time) + ' ' + message + '\n')
    print('записано в лог: ' + time + ' ' + message + '\n')

    with open('\\\\uniweb\\ftp_mm\dead_shops\\app.log', 'a', encoding='utf-8') as f:
        f.write(str(time) + ' ' + message + '\n')
    print('записано в сетевой лог (\\\\uniweb\\ftp_mm\dead_shops\\app.log): ' + time + ' ' + message + '\n')


driver = ''
server = ''
database = ''
uid = ''
pwd = ''

shopids = []
shopid = int
hostname = str

cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;") 

while(True):
    host_name = input('Введите HOSTNAME для удаления: ').upper()
    logger('Запрошено: "' + host_name + '"')

    d = {}

    cursor.execute("SELECT ShopId, HostName FROM Terminals WHERE HostName LIKE '%" + host_name + "%'")
    row = cursor.fetchone()
    if not row:
        print('Ничего похожего не найдено!')
        continue
    while row:
        row = cursor.fetchone()
        try:
            d.update({row[0]: row[1]})
            print(row[0], row[1])
        except(TypeError):
            break
    break
print()



while(True):
    try:
        dead_shopID = int(input('Введите номер магазина для удаления: '))
        if (dead_shopID not in d):
            print('Введен номер не из предложенного списка!')
            continue
    except(ValueError):
        print('Введен не номер!')
    else:
        break

while(True):
    answer = input('Удаляем ' + d.get(dead_shopID) + '?:')
    if answer == 'y' or answer == 'yes' or answer == 'д' or answer == 'д':
        cursor.execute("SELECT ShopId, HostName FROM Terminals WHERE ShopId = " + str(dead_shopID))
        row = cursor.fetchone()
        print('Магазин ' + row.HostName + ' успешно удален')
        logger('Магазин ' + row.HostName + ' успешно удален')
        break
    elif answer == 'n' or answer == 'no' or answer == 'н' or answer == 'нет':
        print('Магазин ' + row.HostName + ' оставлен в базе')
        logger('Магазин ' + row.HostName + ' оставлен в базе')
        break
    else:
        continue
logger('-----------------------------ЗАВЕРШЕНИЕ-----------------------------')