from turtle import color

from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QPixmap, QBrush, QColor, QPen


# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class DatumChart(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        #series erstellt
        self.series = QLineSeries()
        self.series.setName("Series")

        #Farbe für die Line ändern
        pen = QPen(QColor(144, 238, 144))
        pen.setWidth(5)
        self.series.setPen(pen)

        #andere methode für farbe hinzufügen
        #self.series.setColor(QColor("blue"))


        #chart erstellt und series hinzufgefügt
        self.chart = QChart()
        self.chart.setTitle("Karte")
        self.chart.addSeries(self.series)

        #achsen erstellt und range eingestellt
        axis_y = QValueAxis()
        axis_y.setRange(0, 10)


        #datum x achse erstellen




        axis_x = QDateTimeAxis()
        axis_x.setTickCount(10)  # Anzahl der Datenpunkte (Tage)
        axis_x.setFormat("dd.MM")  # Format des Datums
        axis_x.setTitleText("Datum")

        start_date = QDateTime.currentDateTime()
        end_date = QDateTime.currentDateTime().addDays(9)
        axis_x.setRange(start_date, end_date)


        #achsen dem chart hinzugefügt
        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        #nachdem achsen hinzufügen einfügen
        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        #werte für die series hinzufügenfrom turtle import color

from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QPixmap, QBrush, QColor, QPen


# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class DatumChart(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        #series erstellt
        self.series = QLineSeries()
        self.series2 = QLineSeries()
        self.series.setName("Series")
        self.series2.setName("Series2")

        #Farbe für die Line ändern
        #pen = QPen(QColor(144, 238, 144))
        #pen.setWidth(5)
        #self.series.setPen(pen)

        #andere methode für farbe hinzufügen
        self.series.setColor(QColor("blue"))
        self.series2.setColor(QColor("yellow"))


        #chart erstellt und series hinzufgefügt
        self.chart = QChart()
        self.chart.setTitle("Karte")
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.series2)

        #achsen erstellt und range eingestellt
        axis_y = QValueAxis()
        axis_y.setRange(0, 10)



        #datum x-achse erstellen
        axis_x = QDateTimeAxis()
        axis_x.setTickCount(10)  # Anzahl der Datenpunkte (Tage)
        axis_x.setFormat("dd.MM")  # Format des Datums
        axis_x.setTitleText("Datum")

        start_date = QDateTime.currentDateTime()
        end_date = QDateTime.currentDateTime().addDays(-9)
        axis_x.setRange(end_date, start_date)

        #achsen andere farbe
        axis_x.setLabelsColor(QColor("blue"))

        #grid farbe ändern
        pen_grid = QPen(QColor("red"))
        axis_x.setGridLinePen(pen_grid)
        axis_y.setGridLineColor(QColor("blue"))


        #achsen dem chart hinzugefügt
        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        #nachdem achsen hinzufügen einfügen
        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        self.series2.attachAxis(axis_x)
        self.series2.attachAxis(axis_y)

        #werte für die series hinzufügen
        self.series.append(QDateTime.currentDateTime().addDays(-9).toMSecsSinceEpoch(), 1)
        self.series.append(QDateTime.currentDateTime().addDays(-8).toMSecsSinceEpoch(), 2)
        self.series.append(QDateTime.currentDateTime().addDays(-7).toMSecsSinceEpoch(), 3)
        self.series.append(QDateTime.currentDateTime().addDays(-6).toMSecsSinceEpoch(), 4)

        self.series2.append(QDateTime.currentDateTime().addDays(-9).toMSecsSinceEpoch(), 4)
        self.series2.append(QDateTime.currentDateTime().addDays(-8).toMSecsSinceEpoch(), 5)
        self.series2.append(QDateTime.currentDateTime().addDays(-7).toMSecsSinceEpoch(), 6)
        self.series2.append(QDateTime.currentDateTime().addDays(-6).toMSecsSinceEpoch(), 7)


        #hintergrund farbe ändern
        gruener_hintergrund = QBrush(QColor(0, 255, 0))  # RGB für Grün
        self.chart.setBackgroundBrush(gruener_hintergrund)

        #chart anzeigen
        self.setChart(self.chart)a
