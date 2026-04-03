import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class ComingSoonApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BIM QA Automation Tool")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        title = QLabel("BIM QA Automation Tool")
        title.setStyleSheet("color: #00C896; font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)

        label = QLabel("Coming Soon")
        label.setStyleSheet("color: white; font-size: 36px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Automating Drawing QA with Excel + PDF")
        subtitle.setStyleSheet("color: gray; font-size: 12px;")
        subtitle.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(label)
        layout.addWidget(subtitle)

        self.setLayout(layout)
        self.setStyleSheet("background-color: #121212;")

if __name__ == "__main__":
    from PyQt5.QtCore import Qt

    app = QApplication(sys.argv)
    window = ComingSoonApp()
    window.show()
    sys.exit(app.exec_())