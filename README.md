# 🧠 Memory Forensics for Malware Analysis

This project provides a Memory Forensics Tool built using Python and PyQt5 for analyzing memory dumps to detect malware. The tool uses Volatility3 for memory dump analysis and provides an intuitive GUI for users to interact with the data, generate reports, and analyze system memory for potentially malicious activity.
---

## 🚀 Project Overview

- Memory Dump Selection: Load memory dumps in various formats (.dmp, .raw, .vmem, .bin, .img).
- Memory Analysis: Use Volatility3 to run various plugins such as windows.pslist for listing processes and windows.malfind for malware detection.
- Report Generation: Automatically generate detailed reports in JSON format, which can be visualized in the tool.
- GUI Interface: Easy-to-use graphical interface built with PyQt5, enabling seamless navigation and analysis.

---

## 🛠️ Tech Stack

- **Python 3**
- **PyQt5** (for GUI)
- **Volatility3** - A powerful tool for memory analysis.
- **JSON** – For storing and displaying analysis results.

---

## 📋 Requirements

1. Clone the repository:
   ```bash
   git clone https://github.com/heatblaze/Memory-Forensics-for-Malware-Analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Memory-Forensics-for-Malware-Analysis
   ```
3. Create and activate a virutal environment (Optional but recommended):
   ```bash
   python3 -m venv venv
   ```
   - source venv/bin/activate  # On macOS/Linux
   - venv\Scripts\activate     # On Windows
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Install Volatility3:
   ```bash
   pip install volatility3
   ```

---

## Usage

1. Run the tool: python main.py

2. The application will open with a GUI that allows you to:
- Select a memory dump file (.dmp, .raw, .vmem, .bin, .img).
- Analyze the memory dump by running commands such as windows.pslist to list processes and windows.malfind to detect malware.
- View the results of the analysis within the text area.
- Generate a JSON report that includes the analysis results.

3.Steps in the GUI:
- Click Select Memory Dump to load your memory dump file.
- Click Analyze Memory Dump to start the analysis using Volatility3.
- Click Generate Report to create a report in JSON format, which will be displayed in the tool's interface.

---



