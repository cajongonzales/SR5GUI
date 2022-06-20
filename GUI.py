
def main():
    from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
    from PyQt6.QtGui import QPalette, QColor

    app = QApplication([])

    # Create a Qt widget, which will be our window.
    mw = QMainWindow()
    mw.show()

    # Start the event loop.
    app.exec()

    # Your application won't reach here until you exit and the event
    # loop has stopped.


if __name__ == '__main__':
    main()