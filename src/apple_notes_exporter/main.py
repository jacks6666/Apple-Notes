import sys

from PySide6.QtWidgets import QApplication

from apple_notes_exporter.gui.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    app.setApplicationName(
        "Apple Notes Exporter"
    )

    window = MainWindow()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()
