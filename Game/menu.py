import sys
import os
from records import name_record, binding
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel

num_error = 0


class MyWidget(QMainWindow):
    # Класс для отображения окна меню игры
    def __init__(self):
        # Подключаем макет и проверяем кнопку
        super().__init__()
        uic.loadUi('menu.ui',self)
        self.textBrowser = open('table_of_records.txt').read()
        self.pushButton.clicked.connect(self.play)
        self.pushButton_2.clicked.connect(self.settings)
        self.ex_s = SettingsWindow()
        self.pushButton_3.clicked.connect(self.update_table)
        self.ex_e = Error()
        self.pushButton_4.clicked.connect(self.quit)
        names = open('table_of_records.txt').read().split('\n')
        self.label_1.setText(names[0])
        self.label_2.setText(names[1])
        self.label_3.setText(names[2])
        self.label_4.setText(names[3])
        self.label_5.setText(names[4])
    
    def play(self):
        # Функция кнопки play
        name = self.lineEdit.text()
        if '...............' not in name:
            name_record(name)
            os.system("game.py 1")
            # subprocess
            # Обновляем таблицу рекордов
            names = open('table_of_records.txt').read().split('\n')
            self.label_1.setText(names[0])
            self.label_2.setText(names[1])
            self.label_3.setText(names[2])
            self.label_4.setText(names[3])
            self.label_5.setText(names[4])
        else:
            global num_error
            num_error = 1
            self.ex_e.show()
        return 0

    def settings(self):
        # Функция кнопки settings
        self.ex_s.show()
        return 0

    def update_table(self):
        # Функция для обновления таблицы рекордов
        names = open('table_of_records.txt').read().split('\n')
        self.label_1.setText(names[0])
        self.label_2.setText(names[1])
        self.label_3.setText(names[2])
        self.label_4.setText(names[3])
        self.label_5.setText(names[4])
        return 0

    def quit(self):
        self.close()


class SettingsWindow(QMainWindow):
    # Класс для отображения окна настроек игры
    def __init__(self):
        super().__init__()
        uic.loadUi('settings.ui',self)
        self.ex_rr = resetRecords()
        self.ex_rs = resetSettings()
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.reset_records)
        self.pushButton_3.clicked.connect(self.reset_settings)
        self.name_label = QLabel(self)
        self.name_label.setText('Move right button')
        self.name_label.move(40, 30)
        self.name_label = QLabel(self)
        self.name_label.setText('Move left button')
        self.name_label.move(40, 80)
        self.name_label = QLabel(self)
        self.name_label.setText('Move up button')
        self.name_label.move(40, 130)
        self.name_label = QLabel(self)
        self.name_label.setText('Move down button')
        self.name_label.move(40, 180)
        self.name_label = QLabel(self)
        self.name_label.setText('Exit button')
        self.name_label.move(40, 230)
        self.name_label = QLabel(self)
        self.name_label.setText('Screen width X height')
        self.name_label.move(40, 280)

    def save(self):
        # Функция замены размера экрана и кнопок
        file = open('data.txt').read().split(', ')
        parametrs = [self.lineEdit_r.text(), 
                     self.lineEdit_l.text(), 
                     self.lineEdit_u.text(), 
                     self.lineEdit_d.text(), 
                     self.lineEdit_exit.text(), 
                     self.spinBox_w.text(), 
                     self.spinBox_h.text()]
        for i in range(len(parametrs)):
            if parametrs[i] != '':
                file[i] = parametrs[i]
        binding(', '.join(file))
        self.close()

    def reset_records(self):
        # Функия очищения таблицы рекордов
        self.ex_rr.show()
        self.close()

    def reset_settings(self):
        # Функция сброса настроек на дефолт
        self.ex_rs.show()
        self.close()


class Error(QMainWindow):
    # Класс для отображения окна с ошибкой
    def __init__(self):
        global num_error
        super().__init__()
        # list_errors = ['Сбой программы, в последующем обновлении мы это решим', 'Вы ввели не разрешённое имя']
        list_errors = ['The program failed, we will solve it in a subsequent update',
                       'you have entered a name that is not available']
        uic.loadUi('error.ui',self)
        self.label.setText(list_errors[num_error])
        self.pushButton.clicked.connect(self.ok)

    def ok(self):
        self.close()


class resetRecords(QMainWindow):
    # Класс окна для подтверждения сброса
    def __init__(self):
        super().__init__()
        uic.loadUi('confirmation.ui',self)
        # self.label.setText('Вы уверены, что хотите удалить все рекорды?')
        self.label.setText('Are you sure you want to delete all records?')
        self.pushButton.clicked.connect(self.yes)
        self.pushButton_2.clicked.connect(self.no)

    def yes(self):
        file = open('table_of_records.txt', 'w')
        file.write(4 * '...............\n' + '...............')
        file.close()
        # Обновляем таблицу рекордов
        names = open('table_of_records.txt').read().split('\n')
        self.label_1.setText(names[0])
        self.label_2.setText(names[1])
        self.label_3.setText(names[2])
        self.label_4.setText(names[3])
        self.label_5.setText(names[4])
        self.close()

    def no(self):
        self.close()


class resetSettings(QMainWindow):
    # Класс окна для подтверждения сброса
    def __init__(self):
        super().__init__()
        uic.loadUi('confirmation.ui',self)
        # self.label.setText('Вы уверены, что хотите вернуть изначальные настройки?')
        self.label.setText('Are you sure you want to go back to the original settings?')
        self.pushButton.clicked.connect(self.yes)
        self.pushButton_2.clicked.connect(self.no)

    def yes(self):
        file = open('data.txt', 'w')
        file.write('d, a, w, s, esc, 720, 460')
        file.close()
        self.close()

    def no(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())