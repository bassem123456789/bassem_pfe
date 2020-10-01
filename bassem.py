from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import psycopg2 as db
import psycopg2
from peewee import *
import datetime
from PyQt5.QtGui import QPixmap



import sys


MainUI,_ =loadUiType('project_pfe.ui')


class Main(QMainWindow , MainUI):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db_connect()
        self.Handel_buttons()
        self.UI_changes()
        self.open_login()
        self.show_all_param_category()
        self.show_all_resource()
        self.show_all_client()
        self.show_all_guide()








    def UI_changes(self):
        self.tabWidget.tabBar().setVisible(False)


    def db_connect(self):
        self.db = psycopg2.connect( database = 'pfe', user = 'postgres' , password = '123456789')
        self.cur = self.db.cursor()
        print('connection accepted')

    def Handel_buttons(self):

        self.btn_profile.clicked.connect(self.open_profile)
        self.btn_profile_3.clicked.connect(self.open_acceuil)
        self.btn_bib.clicked.connect(self.open_biblio)
        self.btn_ajouter.clicked.connect(self.open_Ajouter)
        self.btn_decision.clicked.connect(self.open_Decision)
        self.btn_settings.clicked.connect(self.open_Historique)
        self.btn_category.clicked.connect(self.Add_category)
        self.btn_profile_2.clicked.connect(self.Add_profile)
        self.add_resource.clicked.connect(self.Add_Resource)
        self.btn_client.clicked.connect(self.Add_client)
        self.recherche_btn_resource.clicked.connect(self.Modifier_resource)
        self.valider_modifier.clicked.connect(self.save_resource)
        self.pushButton_10.clicked.connect(self.save_profile)
        self.btn_supp_resource.clicked.connect(self.delete_resource)
        self.chercher_client.clicked.connect(self.Modifier_client)
        self.btn_client_2.clicked.connect(self.Save_client)
        self.btn_supp_client.clicked.connect(self.supprimer_client)
        self.add_guide.clicked.connect(self.Add_guide)
        self.pushButton_7.clicked.connect(self.open_modifier_guide)
        self.recherche_guide.clicked.connect(self.modifier_guide)
        self.save_guide_btn.clicked.connect(self.save_guide)
        self.supp_btn_guide.clicked.connect(self.supprimer_guide)
        self.recherche_g.clicked.connect(self.Recherche_guide)
        self.rech_resource.clicked.connect(self.Recherche_resource)
        self.rech_client.clicked.connect(self.Recherche_client)
        self.check_profile_btn.clicked.connect(self.check_profile)




    def open_login(self):
        self.tabWidget.setCurrentIndex(0)

    def open_acceuil(self):
        self.tabWidget.setCurrentIndex(2)


    def open_profile(self):
        self.tabWidget.setCurrentIndex(1)

    def open_biblio(self):
        self.tabWidget.setCurrentIndex(6)


    def open_Ajouter(self):
        self.tabWidget.setCurrentIndex(5)


    def open_Decision(self):
        self.tabWidget.setCurrentIndex(4)


    def open_Historique(self):
        self.tabWidget.setCurrentIndex(7)

    def open_modifier_guide(self):
        self.tabWidget_5.setCurrentIndex(2)

    def Add_profile(self):
        nom = self.lineEdit_3.text()
        prenom = self.lineEdit_4.text()
        mail = self.lineEdit_5.text()
        phone = self.lineEdit_7.text()
        city = self.lineEdit_28.text()
        adresse = self.lineEdit_30.text()
        cin =  self.lineEdit_53.text()
        motdepasse = self.lineEdit_55.text()
        motdepasse2 = self.lineEdit_58.text()

        if motdepasse == motdepasse2 :

            self.cur.execute(''' INSERT INTO profile(first_name, last_name, mail, phone, city, adresse, cin, passe, passe2)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', (nom, prenom, mail, phone, city, adresse, cin, motdepasse, motdepasse2))
            self.db.commit()
            print("profile add")
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit_5.setText('')
            self.lineEdit_7.setText('')
            self.lineEdit_28.setText('')
            self.lineEdit_30.setText('')
            self.lineEdit_53.setText('')
            self.lineEdit_55.setText('')
            self.lineEdit_58.setText('')
            QMessageBox.information(self, "success", "تم الاضافة بنجاح")

        else:
         print("inncorrecte")


    def check_profile(self):
        name = self.lineEdit_56.text()
        motdepasse = self.lineEdit_57.text()


        self.cur.execute(''' SELECT * FROM profile ''')
        data = self.cur.fetchall()
        for row in data:
            if row[1] == name and row[9] == motdepasse:
               self.groupBox_2.setEnabled(True)





    def Modifier_profile(self):
        phone_p = self.lineEdit_37.text()

        sql = (''' SELECT * FROM profile WHERE phone = %s''')
        self.cur.execute(sql, [(phone_p)])
        data = self.cur.fetchone()
        print(data)

        self.lineEdit_10.setText(data[1])
        self.lineEdit_9.setText(data[2])
        self.lineEdit_8.setText(data[3])
        self.lineEdit_31.setText(data[5])
        self.lineEdit_33.setText(data[6])

    def save_profile(self):
        name = self.lineEdit_10.text()
        prenom = self.lineEdit_9.text()
        mail = self.lineEdit_8.text()
        phone = self.lineEdit_37.text()
        city  = self.lineEdit_31.text()
        adresse  = self.lineEdit_33.text()

        self.cur.execute(''' UPDATE profile SET first_name = %s, last_name = %s, mail  = %s, phone = %s, city = %s, adresse = %s  WHERE phone = %s
                                ''', (
        name, prenom, mail, phone, city, adresse, phone))
        self.db.commit()
        print("donne")
        QMessageBox.information(self, "success", "تم تعديل بنجاح")
        self.statusBar().showMessage("تم تعديل بنجاح")



    def Add_client(self):
        name = self.lineEdit_17.text()
        phone = self.lineEdit_18.text()
        code = self.lineEdit_19.text()
        date = datetime.datetime.now()


        self.cur.execute(''' INSERT INTO client(name, phone, code, date)
                              VALUES (%s, %s, %s, %s)''', (name, phone, code, date))
        self.db.commit()
        self.show_all_client()
        print("client add")
        
        
    def Modifier_client(self):
         code_c = self.lineEdit_32.text()

         sql = (''' SELECT * FROM client WHERE code = %s''')
         self.cur.execute(sql, [(code_c)])
         data = self.cur.fetchone()
         print(data)

         self.lineEdit_35.setText(data[1])
         self.lineEdit_36.setText(str(data[2]))


    def Save_client(self):
        name = self.lineEdit_35.text()
        phone =self.lineEdit_36.text()
        code = self.lineEdit_32.text()


        self.cur.execute(''' UPDATE client SET name = %s, phone = %s, code = %s  WHERE code = %s
                                        ''', (
            name, phone, code, code))
        self.db.commit()
        print("donne")
        QMessageBox.information(self, "success", "تم تعديل بنجاح")
        self.statusBar().showMessage("تم تعديل بنجاح")
        self.show_all_client()


    def supprimer_client(self):
        code_r = self.lineEdit_32.text()

        QMessageBox.warning(self, " supprimer", "هل انت متأكد من المسح", QMessageBox.Yes | QMessageBox.No)

        if QMessageBox.Yes:
             sql = ('''
                           DELETE FROM client WHERE code = %s''')
             self.cur.execute(sql, [(code_r)])
             self.db.commit()
             self.statusBar().showMessage("تم مسح بنجاح")
             self.show_all_client()

    def Recherche_client(self):
        name = self.lineEdit_21.text()

        sql = (
            ''' SELECT name, phone,  code , date  FROM client WHERE  name = %s  ''')
        self.cur.execute(sql, [name, ])
        data = self.cur.fetchall()

        print(data)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)

        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_position)

    def Add_guide(self):
        clas_guide = self.lineEdit_34.text()
        substance = self.lineEdit_38.text()
        concentration = self.lineEdit_39.text()
        tf_guide = self.lineEdit_40.text()
        produit_guide = self.lineEdit_41.text()
        societe_guide = self.lineEdit_42.text()
        num = self.lineEdit_45.text()
        utilisation = self.textEdit_2.toPlainText()


        self.cur.execute('''INSERT INTO guide(clas_guide, substance, concentration, tf_guide, produit, societe, num, utilisation)
                                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                     ''',
                         (clas_guide, substance, concentration, tf_guide, produit_guide, societe_guide, num, utilisation))

        self.db.commit()
        print("guide add")
        self.show_all_guide()

    def modifier_guide(self):
        num_guide = self.lineEdit_52.text()

        sql = (''' SELECT * FROM guide WHERE num = %s''')
        self.cur.execute(sql, [(num_guide)])
        data = self.cur.fetchone()
        print(data)

        self.lineEdit_48.setText(data[1])
        self.lineEdit_51.setText(data[2])
        self.lineEdit_46.setText(data[3])
        self.lineEdit_47.setText(data[4])
        self.lineEdit_49.setText(data[5])
        self.lineEdit_50.setText(data[6])
        self.textEdit_3.setPlainText(data[7])

    def save_guide(self):

        clas_guide = self.lineEdit_48.text()
        substance = self.lineEdit_51.text()
        concentration = self.lineEdit_46.text()
        tf_guide = self.lineEdit_47.text()
        produit = self.lineEdit_49.text()
        societe = self.lineEdit_50.text()
        num = self.lineEdit_52.text()
        utilisation = self.textEdit_3.toPlainText()


        self.cur.execute(''' UPDATE guide SET clas_guide = %s, substance = %s, concentration = %s, tf_guide = %s, produit = %s, societe = %s, num = %s, utilisation = %s  WHERE num = %s
                                                ''', (
            clas_guide, substance, concentration, tf_guide, produit, societe, num, utilisation, num))
        self.db.commit()
        print("donne")
        QMessageBox.information(self, "success", "تم تعديل بنجاح")
        self.statusBar().showMessage("تم تعديل بنجاح")
        self.show_all_guide()


    def supprimer_guide(self):
        num = self.lineEdit_52.text()

        QMessageBox.warning(self, " supprimer", "هل انت متأكد من المسح", QMessageBox.Yes | QMessageBox.No)

        if QMessageBox.Yes:
            sql = ('''
                                  DELETE FROM guide WHERE num = %s''')
            self.cur.execute(sql, [(num)])
            self.db.commit()
            self.statusBar().showMessage("تم مسح بنجاح")


    def Recherche_guide(self):
        class_name = self.lineEdit_43.text()
        substance = self.lineEdit_44.text()

        sql = (
            ''' SELECT clas_guide, substance, concentration, tf_guide, produit, societe , utilisation, num FROM guide WHERE  clas_guide = %s  ''')
        self.cur.execute(sql, [class_name,])
        data = self.cur.fetchall()

        print(data)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)

        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)









    def Add_Resource(self):
        name = self.lineEdit_11.text()
        category = self.comboBox.currentIndex()
        culture = self.lineEdit_13.text()
        cible = self.lineEdit_14.text()
        substance = self.lineEdit_15.text()
        societe_resource = self.lineEdit_16.text()
        description = self.textEdit_5.toPlainText()
        code = self.lineEdit_22.text()
        date = datetime.datetime.now()




        self.cur.execute(''' INSERT INTO item(name, cat_id, culture, cible_resource, substance, societe_resource, description, date, code )
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                             ''',  (name, category, culture, cible, substance, societe_resource, description, date, code))

        self.db.commit()
        self.show_all_resource()
        print("resource add")


    def Add_category(self):
        category_name = self.lineEdit_12.text()
        parent_category_text = self.comboBox_2.currentText()

        #query = ''' SELECT id FROM category WHERE  category_name = %s '''
        #self.cur.execute(query,[(parent_category_text)])
        #data = self.cur.fetchone()
        #parent_category = data[0]


        self.cur.execute(''' INSERT INTO category (category_name , parent_category) 
                             VALUES (%s , %s)
        ''', (category_name,parent_category_text))
        self.db.commit()
        print("category_add")
        self.show_all_param_category()


    def Modifier_resource(self):
        code_resource = self.lineEdit_29.text()

        sql = (''' SELECT * FROM item WHERE code = %s''')
        self.cur.execute(sql,[(code_resource)])
        data = self.cur.fetchone()
        print(data)

        self.lineEdit_24.setText(data[1])
        self.comboBox_4.setCurrentIndex(int(data[2]))
        self.lineEdit_27.setText(data[3])
        self.lineEdit_26.setText(data[4])
        self.lineEdit_25.setText(data[5])
        self.lineEdit_23.setText(data[6])
        self.textEdit_6.setPlainText(data[7])



    def save_resource(self):
        name = self.lineEdit_24.text()
        category = self.comboBox_4.currentIndex()
        culture = self.lineEdit_27.text()
        cible_resource = self.lineEdit_26.text()
        substance = self.lineEdit_25.text()
        societe_resource = self.lineEdit_23.text()
        description = self.textEdit_6.toPlainText()
        code_r = self.lineEdit_29.text()



        self.cur.execute(''' UPDATE item SET name = %s, cat_id = %s, culture = %s, cible_resource = %s, substance = %s, societe_resource = %s, description = %s, code = %s WHERE code = %s
                         ''', (name, category, culture, cible_resource, substance, societe_resource, description, code_r, code_r))
        self.db.commit()
        print("donne")
        QMessageBox.information(self, "success", "تم تعديل بنجاح")
        self.statusBar().showMessage("تم تعديل بنجاح")
        self.show_all_resource()

    def delete_resource(self):
        code_r = self.lineEdit_29.text()
        QMessageBox.warning(self, " supprimer", "هل انت متأكد من المسح", QMessageBox.Yes | QMessageBox.No)

        if QMessageBox.Yes:
              sql = ('''
               DELETE FROM item WHERE code = %s''')
              self.cur.execute(sql, [(code_r)])
              self.db.commit()
              self.statusBar().showMessage("تم مسح بنجاح")
              self.show_all_resource()

    def Recherche_resource(self):
        name = self.lineEdit_20.text()


        sql = (
            ''' SELECT culture, cible_resource, substance, societe_resource, description, date , code FROM item WHERE  name = %s  ''')
        self.cur.execute(sql, [name,])
        data = self.cur.fetchall()

        print(data)
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)

        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

    def save_acceuil(self):
        name = self.lineEdit_55.text()
        date = datetime.datetime.now()
        category = self.comboBox_9.currentText()


        self.cur.execute('''INSERT INTO inter(code_id, date , type)
                                   VALUES (%s, %s, %s)
                                   ''',
                         (name,date, category))

        self.db.commit()
        print(" add")







    def show_all_param_category(self):
        self.comboBox_2.clear()
        self.cur.execute('''  SELECT category_name  FROM category ''')

        categories = self.cur.fetchall()

        for category in categories:
            self.comboBox_2.addItem(str(category[0]))
            self.comboBox.addItem(str(category[0]))
            self.comboBox_3.addItem(str(category[0]))
            self.comboBox_4.addItem(str(category[0]))

    def show_all_guide(self):
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)

        self.cur.execute(
            ''' SELECT clas_guide, substance, concentration, tf_guide, produit, societe , num, utilisation  FROM guide''')
        data = self.cur.fetchall()

        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)

    def show_all_resource(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)

        self.cur.execute(''' SELECT culture, cible_resource, substance, societe_resource, description, date, code  FROM item''')
        data = self.cur.fetchall()

        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget.setItem(row , col, QTableWidgetItem(str(item)))
                col += 1
            row_position =  self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

    def show_all_client(self):
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)

        self.cur.execute(''' SELECT name, phone, code, date FROM client''')
        data = self.cur.fetchall()

        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_position)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()