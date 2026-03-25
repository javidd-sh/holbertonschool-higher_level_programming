#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and save it to data.json.

    Args:
        csv_filename (str): The filename of the CSV file to convert.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
