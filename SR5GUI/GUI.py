from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
)

from SR5GUI.Spells import Spells
from SR5GUI.Combat import Combat
 
class MainWindow(QMainWindow):
    def __init__(self):
        """The main window.
        """
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



def main():

    app = QApplication([])

    # Create the main window
    mw = MainWindow()
    mw.show()
    
    # Start the event loop.
    app.exec()

if __name__ == '__main__':
    main()