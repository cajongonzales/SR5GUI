from PyQt6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QWidget,
    QTabWidget,
)
class Spells (QWidget):
    def __init__(self) -> None:
        """Represents the spells page.
        """
        super().__init__()
        layout = QHBoxLayout()
        label = QLabel("Spells go here")
        layout.addWidget(label)
        self.setLayout(layout)