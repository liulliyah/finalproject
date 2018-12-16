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
        'SELECT TOP 10 count(Mahasiswa) as jmlakses, Mahasiswa, Jurusan FROM dbo.matkul_nmmhs_aksestrakir  group by Jurusan,Mahasiswa order by jmlakses desc')

    cursor.execute(sqlselect)
    '''results = cursor.fetchall()
    print(results)'''
    row = cursor.fetchone()

    jmlakses = []
    Mahasiswa = []

    while row:
        jmlakses.append(row[0])
        Mahasiswa.append(row[1])
        row = cursor.fetchone()
    plt.barh(jmlakses,Mahasiswa)
    plt.show()
readtextc()