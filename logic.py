import datetime
import logging
import configparser  # импортируем библиотеку для чтения ini-файлов
import pyodbc

config = configparser.ConfigParser()
config.read("settings.ini")

driver = config["DB"]["driver"]
server = config["DB"]["server"]
database = config["DB"]["database"]
uid = config["DB"]["uid"]
pwd = config["DB"]["pwd"]


def cnxn():
    cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
    return cnxn

def connect():
    cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
    cursor = cnxn.cursor()
    return cursor

class DB():
    def my_logger(message):

        time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        with open('app.log', 'a', encoding='utf-8') as f:
            f.write(str(time) + ' ' + message + '\n')
        print('записано в лог: ' + time + ' ' + message + '\n')

        with open('\\\\uniweb\\ftp_mm\dead_shops\\app.log', 'a', encoding='utf-8') as f:
            f.write(str(time) + ' ' + message + '\n')
        print('записано в сетевой лог (\\\\uniweb\\ftp_mm\dead_shops\\app.log): ' + time + ' ' + message + '\n')

    # На вход принимает строку с примерным именем магазина
    # Выбирает соответствующие магазины в базе
    # Возвращает словарь вида {row.ShopId: row.HostName}
    def finder(name):
        dict = {}

        DB.my_logger('Запрошено имя "' + name + '"')

        # connecting
        # cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
        # cursor = cnxn.cursor()
        # print(type(cursor))
        cursor = cnxn().cursor()
        #cursor = connect()
        # доделать проаерку на пустю строку ('') и т.д., что бы не грохнуть случайно хостнэймы всей таблицы!
        if name == '' or name == 'MM-' or name == 'MM' or name == 'M' or name == '-':
            print('Ошибка. В названии абсолютно всех магазинов присутствует такой набор.')
            return 'FAIL!'
        else:
            cursor.execute("SELECT ShopId, HostName FROM Terminals WHERE HostName LIKE '%" + name + "%'")
            while True:
                row = cursor.fetchone()
                if not row:
                    break
                dict.update({row.ShopId: row.HostName})

        return dict

    def confimer(shopid):
        # connecting
        cursor = cnxn().cursor()

        cursor.execute("SELECT HostName FROM Terminals WHERE ShopId = " + shopid)
        row = cursor.fetchone()
        hostname = row.HostName

        return hostname

    def deleter(dict, shopid):

        # Добавить проверку на ввод магазина только из списка!
        # Добавить проверку на цифры
        # Добавить проверку на удаление более 1 магазина!

        for key, value in dict.items():
            if key == shopid:
                DB.my_logger('Найдено ' + str(key) + ' ' + value)

        hostname = dict[shopid]
        #print(hostname)

        # connecting
        cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
        cursor = cnxn.cursor()



        # editing table
        # example of SQL code
        # UPDATE Terminals set HostName = null WHERE HostName like '%MFMS-5%'
        # !!!
        cursor.execute("UPDATE Terminals set HostName = '' WHERE ShopId = " + str(shopid))
        cnxn.commit()
        DB.my_logger('У магазина ' + str(shopid) + ' удален HostName ' + dict[shopid])
        DB.my_logger('Запрос для проверки в базе: ')
        DB.my_logger('SELECT [Id], [ShopId], [HostName], [Errors], [SoftwareVersion], [SyncAlgorithm], [SerialNumber], [Location\], [AppConfigId], [AppConfigTimestamp] FROM [uMarketOnline].[dbo].[Terminals] where ShopId = ' + str(shopid))
        return hostname