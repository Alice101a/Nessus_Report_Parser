import xml.etree.ElementTree as ET
import argparse

def parse_nessus_scan_report(xml_file, severity_threshold=None, plugins=None):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for report_host in root.findall("./Report/ReportHost"):
        hostname = report_host.get("name")
        for report_item in report_host.findall("./ReportItem"):
            plugin_id = report_item.get("pluginID")
            severity = report_item.get("severity")
            name = report_item.get("pluginName")
            description = report_item.find("description").text

            # Apply severity threshold if provided
            if severity_threshold and int(severity) < severity_threshold:
                continue

            # Filter by specified plugin IDs if provided
            if plugins and plugin_id not in plugins:
                continue

            print(f"Host: {hostname}, Plugin ID: {plugin_id}, Severity: {severity}, Name: {name}")
            print(f"Description: {description}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nessus XML Scan Report Parser")
    parser.add_argument("xml_file", help="Path to the Nessus XML scan report")
    parser.add_argument("-t", "--threshold", type=int, help="Filter vulnerabilities by severity threshold")
    parser.add_argument("-p", "--plugins", nargs="+", type=int, help="Filter vulnerabilities by specified plugin IDs")

    args = parser.parse_args()

    parse_nessus_scan_report(args.xml_file, args.threshold, args.plugins)
