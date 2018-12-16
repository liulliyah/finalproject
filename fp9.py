import pyodbc
import matplotlib.pyplot as plt
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8BVD8QS;'
                      'Database=datashareits;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()
def readtextc():
    cursor = cnxn.cursor()
    sqlselect = (
        'SELECT TOP 10 Matakuliah,Percakapan FROM dbo.chat GROUP BY Matakuliah, Percakapan  order by Percakapan desc')

    cursor.execute(sqlselect)
    '''results = cursor.fetchall()
    print(results)'''
    row = cursor.fetchone()

    Matakuliah = []
    Percakapan = []

    while row:
        Percakapan.append(row[0])
        Matakuliah.append(row[1])
        row = cursor.fetchone()
    plt.barh(Percakapan,Matakuliah)
    plt.show()
readtextc()