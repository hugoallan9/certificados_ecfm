
import os
import pandas as pd
import numpy as np

class Reporte():

    def __init__(self,nombre):
        self.archivo = open( nombre + ".tex", "w" )
        self.examinados = None
        self.preambulo = ["\\documentclass[13pt]{extbook}",
        "\\usepackage{multicol}",
        "\\usepackage{lipsum}% dummy text",
        "\\usepackage{wrapfig}",
        "%Para compilar en XeLaTeX con tildes",
        "\\usepackage{polyglossia}",
        "\\setmainlanguage{spanish}",
        "\\usepackage{geometry}",
        "\\usepackage{anyfontsize,url}",
        "%%%%%%%%%%% Paquete Tcolorbox",
        "\\usepackage[skins, breakable, hooks]{tcolorbox}",
        "\\setmainfont[",
        "BoldFont={HindMadurai-SemiBold}",
        "]{Pompiere-Regular}",
         "\\geometry{",
            "legalpaper,",
            "landscape,",
            "total={320mm,175mm},",
            "left=20mm,",
            "top=20mm,",
            "}",
            "\\newtcolorbox{mybox}[2][]{colback=black!5!white,",
            "colframe=black!15!white,fonttitle=\\bfseries",
            "colbacktitle=black!55!white,enhanced}",
        "\\tcbuselibrary{fitting}",
        "\\usepackage{adjustbox}",
        "\\begin{document}"
        ]

        self.inicio_tabla = [
            "\\begin{table}[ht]",
                "\\centering",
                "\\begin{adjustbox}{width=1\\textwidth}",
                    "\\begin{tabular}{p{0.3\\textwidth}p{0.3\\textwidth}p{0.3\\textwidth}}"
        ]

    def leer_csv(self, nombre):
        self.examinados = pd.read_csv(nombre + ".csv")


    def escribir_preambulo(self):
        self.archivo.writelines(self.preambulo)
        self.archivo.writelines(self.inicio_tabla)

    def escribir_ganadores(self):