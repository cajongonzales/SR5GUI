from PyQt6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QWidget,
    QTabWidget,
)

class Combat(QWidget):
    def __init__(self) -> None:
        """Represents the combat page.
        """
        super().__init__()
        layout = QHBoxLayout()
        label = QLabel("Combat POW")
        layout.addWidget(label)
        self.setLayout(layout)