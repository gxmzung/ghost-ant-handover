import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer

from simulation.uam import UAM

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ghost Ant Handover Dashboard")
        self.resize(500, 300)

        self.uam = UAM(position=(2, 2, 2), velocity=(1, 1, 0))
        self.t = 0
        self.handover = 0

        self.title = QLabel("Ghost Ant Handover Dashboard")
        self.position = QLabel()
        self.cell = QLabel()
        self.reward = QLabel()
        self.status = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.position)
        layout.addWidget(self.cell)
        layout.addWidget(self.reward)
        layout.addWidget(self.status)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_dashboard)
        self.timer.start(600)

    def update_dashboard(self):
        pos = self.uam.move()
        self.t += 1

        selected_cell = f"BS-{min(9, max(1, self.t // 4 + 1))}"
        reward = 1.2 + self.t * 0.03

        self.position.setText(f"UAM Position: {pos}")
        self.cell.setText(f"Selected Cell: {selected_cell}")
        self.reward.setText(f"Reward Score: {reward:.3f}")
        self.status.setText("Status: Predictive Ghost Ant running")

app = QApplication(sys.argv)
window = Dashboard()
window.show()
sys.exit(app.exec_())
