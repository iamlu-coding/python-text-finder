import os, sys
import re
from pathlib import PurePath
from openpyxl import load_workbook
import openpyxl
from binaryornot.check import is_binary
from PyPDF2 import PdfReader

class TextFinder:
    def __init__(self, root_dir, text_value):
        self._text_value = text_value
        self._dir_path = root_dir
        self._is_found = 'No'
        self._results = []

    def _execute(self):
        for file in os.listdir(self._dir_path):
            dir_file_path = PurePath(self._dir_path, file)
            if os.path.isfile(str(dir_file_path)):
                # Check if file is Excel 
                if re.findall('\\b.xls\\b', str(file)) or re.findall('\\b.xlsx\\b', str(file)):
                    self._search_excel_file(dir_file_path, file)
                # Check if file is binary or not
                elif is_binary(str(dir_file_path)) == False:
                    self._search_text_file(dir_file_path, file)

                # Check if file is PDF
                elif re.findall('\\b.pdf\\b', str(file)):
                    self._search_pdf_file(dir_file_path, file)

                # ToDo search for binary file like DOCX.

    def _search_pdf_file(self, dir_file_path, filename):
        page_number = 0
        pdf_obj = PdfReader(str(dir_file_path))
        for page in pdf_obj.pages:
            page_number += 1
            page_text = page.extract_text().split('\n')
            for idx, line in enumerate(page_text):
                if re.search(self._text_value, line, flags=re.IGNORECASE):
                    result_str = 'File Name: ' + filename + ' | ' \
                        + 'Page #: ' + str(page_number) + ' | ' \
                        + 'Found at Row #: ' + str(idx + 1) + ' | ' \
                        + 'Row Value: ' + line
                    self._results.append(result_str)
                    self._is_found = 'Yes'

    def _search_excel_file(self, dir_file_path, filename):
        wb = load_workbook(dir_file_path)
        for ws in wb.worksheets:
            for idx, row in enumerate(ws.rows):
                for cell in row:
                    if isinstance(cell, openpyxl.cell.cell.MergedCell):
                        continue
                    if re.search(self._text_value, str(cell.value), flags=re.IGNORECASE) is not None:
                        result_str = 'File Name: ' + filename + ' | ' \
                            + 'Worksheet Name: ' + ws.title + ' | ' \
                            + 'Found at Row # ' + str(idx + 1) + ' | ' \
                            + 'Cell Value: ' + str(cell.value)
                        self._results.append(result_str)
                        self._is_found = 'Yes'

    def _search_text_file(self, dir_file_path, filename):
        with open(dir_file_path, 'r') as text_file:
            lines = text_file.readlines()

        for idx, line in enumerate(lines):
            if re.search(self._text_value, line, flags=re.IGNORECASE) is not None:
                result_str = 'File Name: ' + filename + ' | ' \
                    + 'Found at Line # ' + str(idx + 1) + ' | ' \
                    + 'Row Value: ' + line
                self._results.append(result_str)
                self._is_found = 'Yes'

    def get_results_list(self):
        return self._results

    def is_value_found(self):
        return self._is_found

