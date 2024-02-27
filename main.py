import sqlite3
import sys
from sys import stderr
from traceback import format_exc

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QLabel, QTableWidgetItem, QGridLayout
from pic_funcs import Funcs


# Это класс основного окна приложения
class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #  Загружаю интерфейс приложения
        uic.loadUi('F://QT_PROJECT/INTERFACE.ui', self)

        self.setGeometry(1080, 350, 1000, 500)
        self.choose_pic_button.clicked.connect(self.choose_pic)
        self.accept.clicked.connect(self.accept_differences)
        self.save.clicked.connect(self.savepic)

        self.find.clicked.connect(self.find_setup)
        self.create_setup.clicked.connect(
            lambda: self.create(self.Brightness.value(), self.Contrast.value(), self.Saturation.value(),
                                self.Warmth.value(), self.Red.value(), self.Green.value(), self.Blue.value()))
        self.con = sqlite3.connect('F://QT_PROJECT/final_database.db')
        self.update_table()
        self.use.clicked.connect(self.use_setup)

    #  Обновляет таблицу с базой данных
    def update_table(self):
        try:
            cur = self.con.cursor()
            result = cur.execute(
                f"""SELECT * FROM setups""").fetchall()
            self.table.setRowCount(len(result))
            self.table.setColumnCount(len(result[0]))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.table.setItem(i, j, QTableWidgetItem(str(val)))
            self.con.commit()
        except:
            print(format_exc(10), file=stderr)

    #  Находит в базе данных настройку с названием, которое вы ввели в строку
    def find_setup(self):
        try:
            cur = self.con.cursor()
            result = cur.execute(
                f"""SELECT * FROM setups
                            WHERE setup_name LIKE '%{self.find_name.text().lower()}%'
                                                """).fetchall()
            self.table.setRowCount(len(result))
            self.table.setColumnCount(len(result[0]))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.table.setItem(i, j, QTableWidgetItem(str(val)))
            self.con.commit()
        except:
            print(format_exc(10), file=stderr)

    #  Создает новую настройку с именем, которое вы ввели в строку
    def create(self, brightness, contrast, saturation, warmth, red, green, blue):
        try:
            name = self.new_name.text().lower()
            cur = self.con.cursor()
            check = cur.execute(
                f"""SELECT setup_name FROM setups""").fetchall()
            check = list(map(lambda x: x[0], check))
            if name not in check:
                result = cur.execute(
                    f"""INSERT INTO setups
                                VALUES('{name}', {brightness}, 
                                        {contrast}, {saturation}, {warmth}, {red}, {green}, {blue})
                                                    """).fetchall()
            else:
                result = cur.execute(
                    f"""UPDATE setups
                                SET brightness = {brightness}, contrast = {contrast}, saturation = {saturation},
                                    warmth = {warmth}, red = {red}, green = {green}, blue = {blue}
                                    WHERE setup_name = '{name}'
                                                    """).fetchall()
            self.update_table()
            self.con.commit()
        except:
            print(format_exc(10), file=stderr)

    #  Использует на картинке настройку, имя которой вы ввели в строку
    def use_setup(self):
        try:
            cur = self.con.cursor()
            result = cur.execute(
                f"""SELECT * FROM setups
                                        WHERE setup_name LIKE '%{self.name_use.text().lower()}%'
                                                            """).fetchone()

            self.Brightness.setValue(result[1])
            self.Contrast.setValue(result[2])
            self.Saturation.setValue(result[3])
            self.Warmth.setValue(result[4])
            self.Red.setValue(result[5])
            self.Green.setValue(result[6])
            self.Blue.setValue(result[7])

            self.picture.function('brightness', self.Brightness.value() - (self.delts['Brightness']))
            self.picture.filename = self.picture.resultname
            self.picture.result = Funcs(self.picture.filename, self.picture.resultname)
            self.delts['Brightness'] = self.Brightness.value() - 100

            self.picture.function('contrast', self.Contrast.value() - (self.delts['Contrast']))
            self.picture.filename = self.picture.resultname
            self.picture.result = Funcs(self.picture.filename, self.picture.resultname)
            self.delts['Contrast'] = self.Contrast.value() - 100

            self.picture.function('saturation', self.Saturation.value() - (self.delts['Saturation']))
            self.picture.filename = self.picture.resultname
            self.picture.result = Funcs(self.picture.filename, self.picture.resultname)
            self.delts['Saturation'] = self.Saturation.value() - 100

            self.picture.function('warmth', self.Warmth.value() - (self.delts['Warmth']))
            self.picture.filename = self.picture.resultname
            self.picture.result = Funcs(self.picture.filename, self.picture.resultname)
            self.delts['Warmth'] = self.Warmth.value() - 100

            self.picture.function('red', self.Red.value() - (self.delts['Red']))
            self.picture.filename = self.picture.resultname
            self.picture.result = Funcs(self.picture.filename, self.picture.resultname)
            self.delts['Red'] = self.Red.value() - 100

            self.picture.function('green', self.Green.value() - (self.delts['Green']))
            self.picture.filename = self.picture.resultname
            self.picture.result = Funcs(self.picture.filename, self.picture.resultname)
            self.delts['Green'] = self.Green.value() - 100

            self.picture.function('blue', self.Blue.value() - (self.delts['Blue']))
            self.picture.filename = self.picture.resultname
            self.picture.result = Funcs(self.picture.filename, self.picture.resultname)
            self.delts['Brightness'] = self.Brightness.value() - 100
        except:
            print(format_exc(10), file=stderr)

    #  Выбор картинки и инициализация ползунков, необходимых для работы с ней
    def choose_pic(self):
        try:
            self.delts = {'Brightness': 0, 'Contrast': 0, 'Saturation': 0, 'Warmth': 0,
                          'Red': 0, 'Green': 0, 'Blue': 0}

            self.Brightness.setRange(0, 200)
            self.Brightness.setSliderPosition(100)
            self.Brightness.sliderReleased.connect(lambda: self.difference('brightness'))
            self.Brightness.sliderReleased.connect(lambda: self.acception())

            self.Contrast.setRange(0, 200)
            self.Contrast.setSliderPosition(100)
            self.Contrast.sliderReleased.connect(lambda: self.difference('contrast'))
            self.Contrast.sliderReleased.connect(lambda: self.acception())

            self.Saturation.setRange(0, 200)
            self.Saturation.setSliderPosition(100)
            self.Saturation.sliderReleased.connect(lambda: self.difference('saturation'))
            self.Saturation.sliderReleased.connect(lambda: self.acception())

            self.Warmth.setRange(0, 200)
            self.Warmth.setSliderPosition(100)
            self.Warmth.sliderReleased.connect(lambda: self.difference('warmth'))
            self.Warmth.sliderReleased.connect(lambda: self.acception())

            self.Red.setRange(0, 200)
            self.Red.setSliderPosition(100)
            self.Red.sliderReleased.connect(lambda: self.difference('red'))
            self.Red.sliderReleased.connect(lambda: self.acception())

            self.Green.setRange(0, 200)
            self.Green.setSliderPosition(100)
            self.Green.sliderReleased.connect(lambda: self.difference('green'))
            self.Green.sliderReleased.connect(lambda: self.acception())

            self.Blue.setRange(0, 200)
            self.Blue.setSliderPosition(100)
            self.Blue.sliderReleased.connect(lambda: self.difference('blue'))
            self.Blue.sliderReleased.connect(lambda: self.acception())

            fname = QFileDialog.getOpenFileName(
                self, 'Выбрать картинку', '',
                'Картинка (*.jpg);;Все файлы (*)')[0]
            self.picture = Picture(fname)
            self.picture.show()
        except:
            print(format_exc(10), file=stderr)

    #  Сохранения изменений при отпускании ползунка
    def acception(self):
        try:
            self.picture.filename = self.picture.resultname
            self.picture.result = Funcs(self.picture.filename, self.picture.resultname)
            self.delts[self.sender().objectName()] = self.sender().value() - 100
        except:
            print(format_exc(10), file=stderr)

    #  Принятие всех изменений и возвращение ползунков в исходное положение
    def accept_differences(self):
        try:
            self.picture = Picture(self.picture.resultname, self.picture.resultname)
            self.picture.show()

            self.Brightness.setSliderPosition(100)
            self.Contrast.setSliderPosition(100)
            self.Saturation.setSliderPosition(100)
            self.Warmth.setSliderPosition(100)
            self.Red.setSliderPosition(100)
            self.Green.setSliderPosition(100)
            self.Blue.setSliderPosition(100)
        except:
            print(format_exc(10), file=stderr)

    #  Выполнение функции изменения картинки
    def difference(self, func):
        try:
            self.picture.function(func, self.sender().value() - (self.delts[self.sender().objectName()]))
        except:
            print(format_exc(10), file=stderr)

    #  Сохранить файл как
    def savepic(self):
        try:
            sname = QFileDialog.getSaveFileName(
                self, 'Выбрать картинку', '',
                'Картинка (*.jpg);;Все файлы (*)')[0]
            self.picture.result.result.save(sname)
        except:
            print(format_exc(10), file=stderr)

#  Окно с двумя картинками: результатом и оригиналом
class Picture(QWidget):
    def __init__(self, fname, sname='result.jpg'):
        super().__init__()
        self.filename = fname
        self.resultname = sname
        self.result = Funcs(self.filename, self.resultname)
        self.initUI()

    #  Инициализаци класса
    def initUI(self):
        self.setGeometry(10, 40, 700, 1000)
        self.setWindowTitle('Картинка')
        self.gridLayout = QGridLayout(self)

        self.pixmap = QPixmap(self.resultname)
        self.image = QLabel(self)
        self.image.setPixmap(self.pixmap)
        self.gridLayout.addWidget(self.image)

        self.origpixmap = QPixmap(self.filename)
        self.origimage = QLabel(self)
        self.origimage.setPixmap(self.origpixmap)
        self.gridLayout.addWidget(self.origimage, 0, 1)

    #  Обновление картинок
    def upd(self):
        self.pixmap = QPixmap(self.resultname)
        self.image.setPixmap(self.pixmap)

    #  Изменения картинки по заданному параметру в заданном количестве
    def function(self, func, delta):
        if func == 'brightness':
            self.result.brightness(delta)

        elif func == 'contrast':
            self.result.contrast(delta)

        elif func == 'saturation':
            self.result.saturation(delta)

        elif func == 'warmth':
            self.result.warmth(delta)

        elif func == 'red':
            self.result.color(0, delta)

        elif func == 'green':
            self.result.color(1, delta)

        elif func == 'blue':
            self.result.color(2, delta)

        self.upd()


#  Запуск приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
