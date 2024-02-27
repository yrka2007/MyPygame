import sys
import requests
from PyQt5.QtGui import QPixmap
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication


class MainWindow(QMainWindow):
    g_map: QLabel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('main_window.ui', self)

        self.map_zoom = 10
        self.map_ll = ["50.850331", "58.842917"]
        self.map_l = 'map'

        self.refresh_map()

    def refresh_map(self):
        params = {
            'll': ','.join(self.map_ll),
            'l': self.map_l,
            'z': self.map_zoom
        }
        session = requests.Session()
        retry = Retry(total=10, connect=5, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        response = session.get('http://static-maps.yandex.ru/1.x/', params=params)
        with open('tmp.png', 'wb') as tmp:
            tmp.write(response.content)
        pixmap = QPixmap()
        pixmap.load('tmp.png')
        self.g_map.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    map_window = MainWindow()
    map_window.show()
    sys.exit(app.exec())
