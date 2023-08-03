# Nessus_Report_Parser
The Python script is a versatile Nessus XML scan report parser. It reads a Nessus XML scan report file and provides options to filter and display vulnerability information based on severity and specific plugin IDs.  


Install Python: Check if Python is already installed on your Kali Linux system. By default, Kali Linux comes with Python installed. Open a terminal and enter the following command to check the Python version:


python --version
If Python is not installed, you can install it using the package manager apt:


sudo apt update
sudo apt install python3
Install Required Modules: The script uses the xml.etree.ElementTree module, which is part of the Python standard library and should already be available. However, if you encounter any issues, you can ensure that the required module is installed:

sudo apt install python3-lxml
Save the Script: Save the enhanced Nessus XML scan report parsing script to a Python file (e.g., nessus_report_parser.py).

Make the Script Executable: To run the script easily from the command-line, make the Python script executable:


chmod +x Nessus_Report_Parser.py
Run the Script: Now, you can run the script and provide the path to your Nessus XML scan report as a command-line argument. For example:


./Nessus_Report_Parser.py path_to_nessus_scan_report.xml
The script will parse the report and display vulnerability information for each host.

Optional: Install Nessus: If you don't have Nessus installed and want to perform vulnerability scans to get the Nessus XML report, you can install Nessus on your Kali Linux system. Follow the official documentation from Tenable to install Nessus: https://docs.tenable.com/nessus/Content/InstallNessus.htm
