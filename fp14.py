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
        'SELECT TOP 10 count(Mahasiswa) as jmlmhs, Matakuliah, Jurusan FROM dbo.matkul_nmmhs_aksestrakir  group by Jurusan, Matakuliah order by jmlmhs desc')

    cursor.execute(sqlselect)
    '''results = cursor.fetchall()
    print(results)'''
    row = cursor.fetchone()

    jmlmhs = []
    Matakuliah = []

    while row:
        jmlmhs.append(row[0])
        Matakuliah.append(row[1])
        row = cursor.fetchone()
    plt.barh(Matakuliah,jmlmhs)
    plt.show()
readtextc()