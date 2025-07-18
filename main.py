import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,
    QSizePolicy, QComboBox, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from logic import get_binance_price, get_binance_kline_data
from matplotlib.dates import DateFormatter
from storage import save_price_to_csv


class CryptoTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Tracker")
        self.setGeometry(100, 100, 900, 650)
        self.setFixedSize(900, 650)

        self.symbol = "BTCUSDT"
        self.interval = "1m"

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.selector_layout = QHBoxLayout()

        self.symbol_selector = QComboBox()
        self.symbol_selector.addItems(["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT"])
        self.symbol_selector.currentTextChanged.connect(self.on_selection_change)

        self.interval_selector = QComboBox()
        self.interval_selector.addItems(["1m", "5m", "15m", "1h", "4h", "1d"])
        self.interval_selector.currentTextChanged.connect(self.on_selection_change)

        self.selector_layout.addWidget(QLabel("Монета:"))
        self.selector_layout.addWidget(self.symbol_selector)
        self.selector_layout.addWidget(QLabel("Інтервал:"))
        self.selector_layout.addWidget(self.interval_selector)
        self.layout.addLayout(self.selector_layout)

        self.price_label = QLabel("Ціна: Завантаження...", self)
        self.price_label.setStyleSheet("font-size: 24px; margin: 10px 0;")
        self.layout.addWidget(self.price_label)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.canvas)

        self.timer = QTimer()
        self.timer.setInterval(5000)  # 5 секунд
        self.timer.timeout.connect(self.update_data)
        self.timer.start()

        self.update_data()

    def on_selection_change(self):
        self.symbol = self.symbol_selector.currentText()
        self.interval = self.interval_selector.currentText()
        self.update_data()

    def update_data(self):
        price = get_binance_price(self.symbol)
        if price:
            self.price_label.setText(f"Ціна {self.symbol}: {price:.2f} USDT")
        else:
            self.price_label.setText(f"Ціна {self.symbol}: помилка")
            QMessageBox.warning(self, "Помилка", "Не вдалося отримати ціну з Binance")

        kline_data = get_binance_kline_data(self.symbol, self.interval, 30)
        if kline_data and kline_data[0]:
            timestamps, prices = kline_data

            latest_ts = timestamps[-1]
            latest_price = prices[-1]
            save_price_to_csv(latest_ts, latest_price, self.symbol, self.interval)

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(timestamps, prices, color='orange', marker='o')
            ax.set_title(f"{self.symbol} ({self.interval}) — останні {len(prices)} свічок")
            ax.set_xlabel("Час")
            ax.set_ylabel("Ціна (USDT)")
            ax.tick_params(axis='x', rotation=45)


            time_format = DateFormatter("%H:%M")
            ax.xaxis.set_major_formatter(time_format)

            self.figure.tight_layout()
            self.canvas.draw()
        else:
            print("Графік: помилка при завантаженні даних")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoTracker()
    window.show()
    sys.exit(app.exec_())