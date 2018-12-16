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
        'SELECT TOP 10 count(Matakuliah) as jmlmatkul, Mahasiswa, Jurusan FROM dbo.matkul_mhs  group by Jurusan, Mahasiswa order by jmlmatkul desc')

    cursor.execute(sqlselect)
    '''results = cursor.fetchall()
    print(results)'''
    row = cursor.fetchone()

    jmlmatkul = []
    Mahasiswa = []

    while row:
        jmlmatkul.append(row[0])
        Mahasiwa.append(row[1])
        row = cursor.fetchone()
    plt.barh(Mahasiswa,jmlmatkul)
    plt.show()
readtextc()