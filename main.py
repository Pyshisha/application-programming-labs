from PyQt6.QtWidgets import QApplication

from main_window import MainWindow


if __name__ == "__main__":
    """
            Главная функция программы. Обрабатывает аргументы командной строки и выводит результаты.
    """
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
