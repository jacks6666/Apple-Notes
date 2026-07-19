from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "Apple Notes Exporter v2"
        )

        self.resize(
            800,
            500
        )


        layout = QVBoxLayout()


        title = QLabel(

            "Apple Notes Exporter v2.0\n"
            "Ready"

        )


        button = QPushButton(

            "开始导出"

        )


        layout.addWidget(title)

        layout.addWidget(button)


        container = QWidget()

        container.setLayout(
            layout
        )

        self.setCentralWidget(
            container
        )
