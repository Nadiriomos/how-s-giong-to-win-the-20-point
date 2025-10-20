import PySide6.QtCore as QtCore
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QFrame, QPushButton, QStackedWidget
)
from PySide6.QtWidgets import QShortcut
from PySide6.QtGui import QIcon
import sys
import os


# Import utility functions
from utlis import get_screen_geometry, make_sidebar_button

# Import Pages
from Pages.TestPage import TestPage
from Pages.StudentsGroupsPag import StudentsGroupsPag
from Pages.QuestionsDatabasePage import QuestionsDatabasePage
from Pages.SettingsPage import SettingsPage
from Pages.ContactPage import ContactPage

# === Main Window Setup ===
class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        self.showMaximized()

        # set geometry
        geometry = get_screen_geometry(app)
        self.setGeometry(geometry)

        # shortcut
        QShortcut(QKeySequence("Esc"), self, activated=self.close)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Sidebar + Content
        sidebar = self._build_sidebar()
        self.content_stack = self._build_content()

        # Layout assembly
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.content_stack, stretch=1)

    # === Sidebar ===
    def _build_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("QFrame { background: #2c3e50; }")

        layout = QVBoxLayout(sidebar)

        # --- Top buttons ---
        top_buttons = [
            ("new test", "src/icons/test.png", 0),
            ("students and groups", "src/icons/school.png", 1),
            ("questions database", "src/icons/questions.png", 2)
        ]
        for text, icon, index in top_buttons:
            btn = make_sidebar_button(text, icon)
            btn.clicked.connect(lambda _, i=index: self.content_stack.setCurrentIndex(i))
            layout.addWidget(btn)

        layout.addStretch()  # pushes next widgets down

        # --- Bottom buttons ---
        bottom_buttons = [
            ("Settings", "src/icons/settings.png", 3),
            ("Contact", "src/icons/contact.png", 4),
        ]
        for text, icon, index in bottom_buttons:
            btn = make_sidebar_button(text, icon)
            btn.clicked.connect(lambda _, i=index: self.content_stack.setCurrentIndex(i))
            layout.addWidget(btn)

        return sidebar

    # === Content Area ===
    def _build_content(self):
        stack = QStackedWidget()
        stack.addWidget(TestPage())  # index 0
        stack.addWidget(StudentsGroupsPag())  # index 1
        stack.addWidget(QuestionsDatabasePage())   # index 2
        stack.addWidget(SettingsPage())   # index 3
        stack.addWidget(ContactPage())    # index 4
        return stack


if __name__ == "__main__":
    app = QApplication([])
    home_page = HomePage()
    home_page.show()
    app.exec()

