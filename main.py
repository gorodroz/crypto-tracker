import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from logic import get_binance_price, get_binance_kline_data


class CryptoTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bitcoin Tracker")
        self.setGeometry(100, 100, 800, 600)

        # Головний віджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Лейаут
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Ціна BTC
        self.price_label = QLabel("Ціна BTC: Завантаження...", self)
        self.price_label.setStyleSheet("font-size: 24px;")
        self.layout.addWidget(self.price_label)

        # Полотно графіку
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Таймер для автооновлення
        self.timer = QTimer()
        self.timer.setInterval(5000)  # кожні 5 секунд
        self.timer.timeout.connect(self.update_data)
        self.timer.start()

        # Перше оновлення
        self.update_data()

    def update_data(self):
        # Оновлення ціни
        price = get_binance_price("BTCUSDT")
        if price:
            self.price_label.setText(f"Ціна BTC: {price} USDT")
        else:
            self.price_label.setText("Ціна BTC: Не вдалося завантажити")

        # Оновлення графіку
        kline_data = get_binance_kline_data("BTCUSDT", interval="1m", limit=30)
        if kline_data:
            timestamps, prices = kline_data
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(timestamps, prices, color='orange', marker='o')
            ax.set_title("BTC/USDT - останні 30 хв")
            ax.set_xlabel("Час")
            ax.set_ylabel("Ціна (USDT)")
            ax.tick_params(axis='x', rotation=45)
            self.canvas.draw()
        else:
            print("Помилка при завантаженні даних для графіку")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoTracker()
    window.show()
    sys.exit(app.exec_())
