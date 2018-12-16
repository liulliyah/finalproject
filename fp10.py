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
        'SELECT TOP 10 count(Matakuliah) as jmlmatkul, Dosen,Jurusan  FROM dbo.matkul_nmdosen_aksestrakir  group by Jurusan, Dosen order by jmlmatkul desc')

    cursor.execute(sqlselect)
    '''results = cursor.fetchall()
    print(results)'''
    row = cursor.fetchone()

    jmlmatkul = []
    Dosen= []

    while row:
        Dosen.append(row[0])
        jmlmatkul.append(row[1])
        row = cursor.fetchone()
    plt.barh(Dosen,jmlmatkul)
    plt.show()
readtextc()