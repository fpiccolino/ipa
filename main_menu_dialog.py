# main_menu_dialog.py

from qgis.PyQt.QtWidgets import QDialog
from .main_menu_dialog_base import Ui_Dialog  # o Ui_MainWindow, a seconda di come è impostato

class MainMenuDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainMenuDialog, self).__init__(parent)
        self.setupUi(self)

        
