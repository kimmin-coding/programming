import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        
        
        self.ui = uic.loadUi(__file__.replace(".py",".ui"), self)
        
        self.ui.show()

    def select_m(self):
        db=__file__.replace("select_label.py","movie.db")        

        conn=sqlite3.connect(db)
        cur=conn.cursor()

        strQuery="select * from movie_watch "
        search_title=self.search_tb.text()
        if len(search_title)>0:
            strQuery+="where title like'%"+search_title+"%'"


        cur.execute(strQuery)
                
        records=cur.fetchall()
        a=""
        for v in records:
            a+=str(v)+"\n"
        self.view_label.setText(a)
        cur.close()
        conn.close()
    def search(self):
        pass
    #     conn=sqlite3.connect("movie.db")
    #     cur=conn.cursor()

    #     strQuery="select title from movie_watch"
    #     print(strQuery)
    #     cur.execute(strQuery)

                
    #     records=cur.fetchall()
        
            

        
        

        

if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())