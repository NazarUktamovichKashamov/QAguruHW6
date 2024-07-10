import csv
from io import TextIOWrapper

from openpyxl import load_workbook
from zipfile import ZipFile
from pypdf import PdfReader
import pandas as pd

from set_path import ZIP_FILE

def test_check_pdf_in_archive():
    file_name = 'sample2.pdf'
    with ZipFile(ZIP_FILE) as zip_file:
        with zip_file.open(file_name) as file:
            reader = PdfReader(file)

            assert len(reader.pages) == 1011
            assert "PDF Form Example”" in reader.pages[1].extract_text()
