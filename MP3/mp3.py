# MP3 GUI
# Diseño de Sistemas en Chip(TE2003)
# ITESM Puebla
# Equipo 2 - Santiago Hernandez Arrellano
#            Antonio Silva Martinez
#            Jhonatan Yael Martinez Vargas

# Importacion de libreria para la creacion de la GUI y la interaccion con los archivos .mp3
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame

# Se crea un array con los nombres de los archivos a repodrucir y mostrar
playList = ["ACDC - Highway To Hell.mp3",
            "Bee Gees - Staying Alive.mp3",
            "Coldplay - Yellow.mp3",
            "David Guetta - Titanium.mp3",
            "Jaden - Rainbow Bap.mp3",
            "OneRepublic - Secrets.mp3",
            "Panic! at the Disco - High Hopes.mp3",
            "Perfect - Simple Plan.mp3",
            "The Script - Man on a Wire.mp3",
            "Demons - Imagine Dragons.mp3"]

# Inicializa el modulo para reproducir  musica
pygame.mixer.init()
mp3 = pygame.mixer.music

# Se guarda en una variable globla el estado de reproduccion(Bool)
status = mp3.get_busy()

# Se crean y se detallan cada uno de los elementos visuales que tendra la GUI en la ventana principal
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        
        # Se definen las dimensiones de la ventana principal(pixeles)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 337)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Se designa el espacio para visualizar las canciones
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(380, 40, 381, 251))
        self.listWidget.setObjectName("listWidget")
        
        # Se asigana una accion tras detectar un click en la "listWidget"
        self.listWidget.itemClicked.connect(self.loadSong)
    
        # Se agregan muestran las canciones de la playList en una lista dentro del GUI
        for i in playList:
            
            pos = 0
            self.listWidget.insertItem(pos,i)
            pos += 1
        
        #inicia desde la cancion 1
        self.listWidget.setCurrentRow(0)

        # Se crean y configuran los 4 botones(play/pause, stop, preview, next)
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(20, 130, 71, 41))
        self.playButton.setObjectName("playpButton")
        self.playButton.clicked.connect(self.playPause)

        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(110, 130, 75, 41))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.stopSong)

        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(200, 130, 75, 41))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.nextSong)

        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(290, 130, 75, 41))
        self.prevButton.setObjectName("prevButton")
        self.prevButton.clicked.connect(self.prevSong)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 31))
        
        # Se le da un mejor formato al Font principal
        font = QtGui.QFont()

        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")

        # Se crear y configura la barra donde se visualizara la cancion en reproduccion
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 351, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.loadSong(self.listWidget.currentItem())
        
        # Se hacen algunos ajustes a la ventan principal
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 15, 81, 21))

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menubar.setObjectName("menubar")

        self.menuMP3_Player = QtWidgets.QMenu(self.menubar)
        self.menuMP3_Player.setObjectName("menuMP3_Player")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMP3_Player.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    # Se establecen los nombres visibles en la GUI para cada widget creado
    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playButton.setText(_translate("MainWindow", "Play/Pause"))
        self.stopButton.setText(_translate("MainWindow", "Alto"))
        self.nextButton.setText(_translate("MainWindow", "Siguiente"))
        self.prevButton.setText(_translate("MainWindow", "Anterior"))
        self.label.setText(_translate("MainWindow", "Now Playing:"))
        self.label_2.setText(_translate("MainWindow", "Playlist"))
        self.menuMP3_Player.setTitle(_translate("MainWindow", "MP3 Player"))
        
# Acciones de los botones

    # Se encarga de reproducir el elemto seleccionado en la lista
    def loadSong(self, item):
       
        global mp3
        global status
        
        # Se selecciona la cancion a reproduccir tras a ver dado click a un elemento de la lista
        mp3.load(item.text())
        
        # Se despliega la informacion de la cancion seleccionada
        self.lineEdit.setText(item.text())
        
        # Se reproduce la cancion
        mp3.play()
        
        # Toogle al la variable global "status"
        status = not status

    # Se encarga de pausar / reanudar la cancion seleccionada
    def playPause(self):
        
        global mp3
        global status
        
        # Dependiendo el valor de la variable global "status" pausa o reanuda la cancion
        if status:
            
            mp3.pause()
            
        else:
            
            mp3.unpause()
        
        #Toogle a la variable global "status"
        status = not status
    
    # Se detiene por completo la cancion
    def stopSong(self):
        mp3.stop()
    
    # Se selecciona la siguiente cancion de la lista
    def nextSong(self):
        
        # Limitamos el rango de movimiento hacia adelante
        if (self.listWidget.currentRow() < 9):
            
            self.listWidget.setCurrentRow(self.listWidget.currentRow()+1)
            self.loadSong(self.listWidget.currentItem())

    # Se selecciona la cancion previa de la lista
    def prevSong(self):
        
        # Limitamos el rango de movimiento hacia atras
        if (self.listWidget.currentRow() > 0):
            
            self.listWidget.setCurrentRow(self.listWidget.currentRow()-1)
            self.loadSong(self.listWidget.currentItem())

# main()

if __name__ == "__main__":

    import sys
    
    # Se instancia la ventana principal y sus configuraciones
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    # Se abre la GUI
    MainWindow.show()
    
    # Se sale de la GUI
    sys.exit(app.exec_())
