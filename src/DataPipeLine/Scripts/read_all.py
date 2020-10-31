import os
import importlib
import camelot
from src.DataPipeLine.Scripts.read_pdf import getPDF

Directory = 'F:/Deeplearning/Datathon-1.0'
pdf_dir = Directory + '/data/daily_pdf'

All_files = os.listdir(pdf_dir)
print(All_files)

for pdf_name in All_files:
    getPDF(pdf_dir + '/' + pdf_name)

