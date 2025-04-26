#To acquire the dump file, run the command on command prompt: go-winpmem_amd64_1.0-rc1.exe acquire filename.raw.
#As soon as you enter the command, immediately press CTRL+C to cancel the command to ensure not a big file is generated that takes time to analyze
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog, QTextEdit, QLabel,
    QVBoxLayout, QWidget, QHBoxLayout, QTabWidget, QDialog, QFrame
)
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt
import subprocess
import json


class ReportViewer(QDialog):
    def __init__(self, report_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("📄 Memory Analysis Report")
        self.setGeometry(200, 150, 900, 500)
        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setFont(QFont("Consolas", 10))
        self.text_edit.setStyleSheet("background-color: #2b2b2b; color: #f1f1f1; border: none;")
        layout.addWidget(self.text_edit)

        formatted_report = json.dumps(report_data, indent=4)
        self.text_edit.setText(formatted_report)

        self.setLayout(layout)
        self.setStyleSheet("background-color: #3c3f41; color: white;")


class MemoryForensicsTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Memory Forensics Tool")
        self.setGeometry(100, 100, 1000, 650)
        self.setWindowIcon(QIcon("forensics_icon.png"))

        self.setFont(QFont("Segoe UI", 10))
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QLabel, QTextEdit {
                color: #f1f1f1;
            }
            QPushButton {
                background-color: #3c3f41;
                color: white;
                padding: 6px;
                border: 1px solid #5c5f61;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #4c5052;
            }
            QTabWidget::pane {
                border-top: 2px solid #444;
            }
            QTabBar::tab {
                background: #3c3f41;
                color: #aaa;
                padding: 10px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background: #2b2b2b;
                color: #fff;
            }
        """)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.main_tab = QWidget()
        self.tabs.addTab(self.main_tab, "🔍 Analysis")

        layout = QVBoxLayout()

        title = QLabel("🧠 Memory Forensics Tool")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        layout.addWidget(self._separator())

        self.label = QLabel("Select a Memory Dump File to Analyze")
        self.label.setFont(QFont("Segoe UI", 11))
        layout.addWidget(self.label)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setFont(QFont("Consolas", 11))
        self.text_area.setStyleSheet("background-color: #2b2b2b; color: #f1f1f1; border: 1px solid #444;")
        layout.addWidget(self.text_area)

        btn_layout = QHBoxLayout()

        self.btn_select = QPushButton("📂 Select Memory Dump")
        self.btn_select.clicked.connect(self.load_memory_dump)
        btn_layout.addWidget(self.btn_select)

        self.btn_analyze = QPushButton("🔍 Analyze Memory Dump")
        self.btn_analyze.clicked.connect(self.analyze_memory)
        btn_layout.addWidget(self.btn_analyze)

        self.btn_report = QPushButton("📝 Generate Report")
        self.btn_report.clicked.connect(self.generate_report)
        btn_layout.addWidget(self.btn_report)

        layout.addLayout(btn_layout)
        self.main_tab.setLayout(layout)

    def _separator(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color: #555;")
        return line

    def load_memory_dump(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Memory Dump File", "",
            "All Files (*);;Memory Dumps (*.dmp *.raw *.vmem *.bin *.img)",
            options=options
        )
        if file_name:
            self.text_area.append(f"\n📁 Selected File: {file_name}\n")
            self.memory_dump_path = file_name

    def analyze_memory(self):
        if hasattr(self, 'memory_dump_path'):
            self.text_area.append("\n🔎 Running Volatility Analysis...\n")
            volatility_path = "C:\\Users\\Aditya Chitransh\\volatility3\\vol.py"

            commands = {
                "Processes": f"python \"{volatility_path}\" -f \"{self.memory_dump_path}\" windows.pslist",
                "Malware Check": f"python \"{volatility_path}\" -f \"{self.memory_dump_path}\" windows.malfind"
            }
            self.analysis_results = {}

            for key, command in commands.items():
                try:
                    output = subprocess.getoutput(command)
                    self.analysis_results[key] = output
                    self.text_area.append(f"\n--- {key} Analysis ---\n{output}\n")
                except Exception as e:
                    self.text_area.append(f"\n⚠️ Error in {key}: {str(e)}\n")
        else:
            self.text_area.append("\n⚠️ No memory dump selected!\n")

    def generate_report(self):
        if hasattr(self, 'analysis_results'):
            report_path = "memory_analysis_report.json"
            with open(report_path, "w") as report_file:
                json.dump(self.analysis_results, report_file, indent=4)
            self.text_area.append(f"\n✅ Report generated: {report_path}\n")

            self.report_viewer = ReportViewer(self.analysis_results, self)
            self.report_viewer.exec_()
        else:
            self.text_area.append("\n⚠️ No analysis data available! Run analysis first.\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MemoryForensicsTool()
    window.show()
    sys.exit(app.exec_())
