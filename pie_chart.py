from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QToolBar, QLabel
from PyQt6.QtGui import QPainter, QFont, QAction, QIcon
from PyQt6.QtCharts import QChart, QChartView, QPieSeries

class Window(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id  # Store user_id for later use
        self.setWindowTitle('Categories Percentage Report')
        self.setGeometry(0, 0, 900, 600)
        self.setWindowIcon(QIcon('images/window_icon_images/piechart_icon.png'))
        self.setStyleSheet("""
            QMainWindow { background-color: #e3e9f2; font-family: Arial; font-size: 14px; }
            QLabel { font-size: 18px; }
            QToolBar QToolButton { background-color: #4CAF50; color: white; font-weight: bold; padding: 5px 10px; border-radius: 5px; font-size: 14px; }
            QToolBar QToolButton:hover { background-color: #45a049; }
            QToolBar QToolButton:pressed { background-color: #388e3c; }
        """)
        self.create_ui()

    def create_ui(self):
        self.toolbar = QToolBar("Toolbar")
        self.addToolBar(self.toolbar)
        refresh_action = QAction("Refresh Data", self)
        refresh_action.triggered.connect(self.refresh_data)
        self.toolbar.addAction(refresh_action)

        self.label = QLabel("Click 'Refresh Data' to update the chart with the latest data.", self)
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.chart_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.refresh_data()

    def refresh_data(self):
        from app import ExpenseApp
        # Pass user_id to categories_data method
        expense_app = ExpenseApp(self.user_id)  # Create an instance of ExpenseApp with user_id
        category_percentages = expense_app.categories_data()  # Call categories_data with no additional argument

        series = QPieSeries()
        for category, percentage in category_percentages.items():
            slice = series.append(category, percentage)
            slice.setLabel(f'{category}: {percentage:.1f}%')
            slice.setLabelFont(QFont("Arial", 10, QFont.Weight.Bold))
            slice.setLabelColor(Qt.GlobalColor.black)

        series.setLabelsVisible(True)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.setTitle('Expense Distribution by Category')
        chart.setTitleFont(QFont("Calibri", 20))

        chart.legend().setFont(QFont("Arial", 10))
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignTop)
        self.chart_view.setChart(chart)




