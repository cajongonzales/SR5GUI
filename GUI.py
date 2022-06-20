from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QHBoxLayout,
    QWidget,
    QTabWidget,
)

 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SR5 Rulebook GUI")
        self.resize(600,600)
        # Main tab bar
        tabs = QTabWidget(self)
        spells_page = Spells()
        tabs.addTab(spells_page,"Spells")
        #spells_menu.addAction(button_action)
        combat_page = Combat()
        tabs.addTab(combat_page,"Combat")
        self.setCentralWidget(tabs)

class Spells (QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QHBoxLayout()
        label = QLabel("Spells go here")
        layout.addWidget(label)
        self.setLayout(layout)

class Combat(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QHBoxLayout()
        label = QLabel("Combat POW")
        layout.addWidget(label)
        self.setLayout(layout)

def main():

    app = QApplication([])

    # Create the main window
    mw = MainWindow()
    mw.show()
    
    # Start the event loop.
    app.exec()

if __name__ == '__main__':
    main()