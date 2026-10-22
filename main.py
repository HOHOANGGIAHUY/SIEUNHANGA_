import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

  def __init__(self):
    super().__init__()
    # Load trực tiếp file .ui mà không cần thông qua PyUIC nữa
    uic.loadUi("GiaiPhuongTrinhBac1.ui", self)

    # Kết nối sự kiện nút bấm
    self.btnGiai.clicked.connect(self.xu_ly_giai)
    self.btnThoat.clicked.connect(self.close)

  def xu_ly_giai(self):
    try:
      a_text = self.txtA.text().strip()
      b_text = self.txtB.text().strip()

      if not a_text or not b_text:
        self.txtKetQua.setText("Vui lòng nhập đủ a và b!")
        return

      a = float(a_text)
      b = float(b_text)

      # Giải phương trình bậc 1: ax + b = 0
      if a == 0:
        if b == 0:
          self.txtKetQua.setText("Phương trình vô số nghiệm")
        else:
          self.txtKetQua.setText("Phương trình vô nghiệm")
      else:
        x = -b / a
        self.txtKetQua.setText(f"x = {x}")
    except ValueError:
      self.txtKetQua.setText("Vui lòng nhập định dạng số hợp lệ!")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())