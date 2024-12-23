from PyQt6.QtWidgets import (QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from image_iterator import ImagePathIterator


class MainWindow(QMainWindow):
    """
        Главное окно приложения Dataset Viewer.
        Позволяет загружать файл аннотаций, просматривать изображения по порядку.
    """
    def __init__(self) -> None:
        """
            Конструктор класса MainWindow.
        """
        super().__init__()
        self.setWindowTitle("Dataset Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel("Выберите файл аннотации")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.select_csv_button = QPushButton("Выбрать файл аннотации")
        self.select_csv_button.clicked.connect(self.select_csv)

        self.next_image_button = QPushButton("Следующее изображение")
        self.next_image_button.clicked.connect(self.show_next_image)
        self.next_image_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.select_csv_button)
        layout.addWidget(self.next_image_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.iterator = None

    def select_csv(self) -> None:
        """
            Открывает диалоговое окно для выбора файла аннотации (CSV).
        """
        file, _ = QFileDialog.getOpenFileName(self)
        if file:
            try:
                self.iterator = ImagePathIterator(file)
                self.next_image_button.setEnabled(True)
                self.show_next_image()
            except Exception as e:
                self.image_label.setText(f"Ошибка: {str(e)}")

    def show_next_image(self) -> None:
        """
            Отображает следующее изображение из итератора.
            Показывает сообщение, если изображения закончились или произошла ошибка.
        """
        if self.iterator:
            try:
                image_path = next(self.iterator)
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    self.image_label.setText("Не удалось загрузить изображение.")
                else:
                    self.image_label.setPixmap(
                        pixmap.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio))
            except StopIteration:
                self.image_label.setText("Конец датасета.")
                self.next_image_button.setEnabled(False)
            except Exception as e:
                self.image_label.setText(f"Ошибка: {e}")
