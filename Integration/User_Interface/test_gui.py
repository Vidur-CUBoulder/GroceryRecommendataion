import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)

label = QLabel()
pixmap = QPixmap("./emoji.png")
label.setPixmap(pixmap)
label.show()

sys.exit(app.exec_())
