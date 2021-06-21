import datetime
import pyodbc

driver = ''
server = ''
database = ''
uid = ''
pwd = ''

cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
cursor = cnxn.cursor()

hostname = 'semeyniydoctor1'
shopId = 864

print(hostname)
print('Terminals')
cursor.execute("SELECT * FROM Terminals WHERE ShopId = " + str(shopId))
row = cursor.fetchone()

print('ShopId, LastSessionId, HostName, SoftwareVersion, LastEventId, SyncAlgorithm, SerialNumber, Location, AppConfigId')
print(row.ShopId, row.LastSessionId, row.HostName, row.SoftwareVersion, row.LastEventId, row.SyncAlgorithm, row.SerialNumber, row.Location, row.AppConfigId)

print

print('Shops')
cursor.execute("SELECT * FROM Shops WHERE Id = " + str(shopId))
row = cursor.fetchone()

print('Id, Name, CustomersModified, BlacklistModified, Description, Language, PlanogramId, MobileAppPayment, CompanyId, Currency, BonusRate, OperatorGroupId, ProductCountersState, Address, PaymentOptions, ExternalId, VmToken, DiscountsModified, LastCartTotalsTime')
print(row.Id, row.Name, row.CustomersModified, row.BlacklistModified, row.Description, row.Language, row.PlanogramId, row.MobileAppPayment, row.CompanyId, row.Currency,row.BonusRate, row.OperatorGroupId, row.ProductCountersState, row.Address, row.PaymentOptions, row.ExternalId, row.VmToken, row.DiscountsModified, row.LastCartTotalsTime)

print()

#cursor.execute("UPDATE Shops set MobileAppPayment = 'True' WHERE Id = " + str(shopId))
#cnxn.commit()

#shops
#cursor.execute("SELECT * FROM Shops WHERE Id = " + str(shopId))
#row = cursor.fetchone()
#print(row.MobileAppPayment)

hostname = 'semeyniydoctor6'
shopId = 850

print(hostname)
print('Terminals')
cursor.execute("SELECT * FROM Terminals WHERE ShopId = " + str(shopId))
row = cursor.fetchone()

print('ShopId, LastSessionId, HostName, SoftwareVersion, LastEventId, SyncAlgorithm, SerialNumber, Location, AppConfigId')
print(row.ShopId, row.LastSessionId, row.HostName, row.SoftwareVersion, row.LastEventId, row.SyncAlgorithm, row.SerialNumber, row.Location, row.AppConfigId)

print

print('Shops')
cursor.execute("SELECT * FROM Shops WHERE Id = " + str(shopId))
row = cursor.fetchone()

print('Id, Name, CustomersModified, BlacklistModified, Description, Language, PlanogramId, MobileAppPayment, CompanyId, Currency, BonusRate, OperatorGroupId, ProductCountersState, Address, PaymentOptions, ExternalId, VmToken, DiscountsModified, LastCartTotalsTime')
print(row.Id, row.Name, row.CustomersModified, row.BlacklistModified, row.Description, row.Language, row.PlanogramId, row.MobileAppPayment, row.CompanyId, row.Currency,row.BonusRate, row.OperatorGroupId, row.ProductCountersState, row.Address, row.PaymentOptions, row.ExternalId, row.VmToken, row.DiscountsModified, row.LastCartTotalsTime)

print()

#cursor.execute("UPDATE Shops set MobileAppPayment = 'True' WHERE Id = " + str(shopId))
#cnxn.commit()

#shops
#cursor.execute("SELECT * FROM Shops WHERE Id = " + str(shopId))
#row = cursor.fetchone()
#print(row.MobileAppPayment)

hostname = 'semeyniydoctor'
shopId = 835

print(hostname)
print('Terminals')
cursor.execute("SELECT * FROM Terminals WHERE ShopId = " + str(shopId))
row = cursor.fetchone()

print('ShopId, LastSessionId, HostName, SoftwareVersion, LastEventId, SyncAlgorithm, SerialNumber, Location, AppConfigId')
print(row.ShopId, row.LastSessionId, row.HostName, row.SoftwareVersion, row.LastEventId, row.SyncAlgorithm, row.SerialNumber, row.Location, row.AppConfigId)

print

print('Shops')
cursor.execute("SELECT * FROM Shops WHERE Id = " + str(shopId))
row = cursor.fetchone()

print('Id, Name, CustomersModified, BlacklistModified, Description, Language, PlanogramId, MobileAppPayment, CompanyId, Currency, BonusRate, OperatorGroupId, ProductCountersState, Address, PaymentOptions, ExternalId, VmToken, DiscountsModified, LastCartTotalsTime')
print(row.Id, row.Name, row.CustomersModified, row.BlacklistModified, row.Description, row.Language, row.PlanogramId, row.MobileAppPayment, row.CompanyId, row.Currency,row.BonusRate, row.OperatorGroupId, row.ProductCountersState, row.Address, row.PaymentOptions, row.ExternalId, row.VmToken, row.DiscountsModified, row.LastCartTotalsTime)

print()

#cursor.execute("UPDATE Shops set MobileAppPayment = 'True' WHERE Id = " + str(shopId))
#cnxn.commit()

#shops
#cursor.execute("SELECT * FROM Shops WHERE Id = " + str(shopId))
#row = cursor.fetchone()
#print(row.MobileAppPayment)