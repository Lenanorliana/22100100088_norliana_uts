from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic

# Kelas untuk menghubungkan GUI dari file .ui
class FORM_UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("pemesan.ui", self)  # Memuat file .ui

# Membuat aplikasi dan menampilkan jendela
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Membuat instance aplikasi
    window = FORM_UI()             # Membuat instance jendela utama
    window.show()                  # Menampilkan jendela
    sys.exit(app.exec())           # Menjalankan event loop
