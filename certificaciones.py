
import os
import pandas as pd
import numpy as np

class Reporte():

    def __init__(self,nombre, fecha_examen, autoridad):
        self.archivo = open( nombre + ".tex", "w" )
        self.examinados = None
        self.fecha_examen = fecha_examen
        self.autoridad = autoridad
        self.preambulo = ["\\documentclass[13pt]{extbook}\n",
        "\\usepackage{multicol}\n",
        "\\usepackage{lipsum}% dummy text\n",
        "\\usepackage{wrapfig}\n",
        "%Para compilar en XeLaTeX con tildes\n",
        "\\usepackage{polyglossia}\n",
        "\\setmainlanguage{spanish}\n",
        "\\usepackage{geometry}\n",
        "\\usepackage{anyfontsize,url}\n",
        "%%%%%%%%%%% Paquete Tcolorbox\n",
        "\\usepackage[skins, breakable, hooks]{tcolorbox}\n",
        "\\setmainfont[\n",
        "BoldFont={HindMadurai-SemiBold}\n",
        "]{Pompiere-Regular}\n",
         "\\geometry{\n",
            "legalpaper,\n",
            "landscape,\n",
            "total={320mm,175mm},\n",
            "left=20mm,\n",
            "top=20mm,\n",
            "}\n",
            "\\newtcolorbox{mybox}[2][]{colback=black!5!white,\n",
            "colframe=black!15!white,fonttitle=\\bfseries\n",
            "colbacktitle=black!55!white,enhanced}\n",
        "\\tcbuselibrary{fitting}\n",
        "\\usepackage{adjustbox}\n",
        "\\begin{document}\n"
        ]

        self.inicio_tabla = [
            "\\begin{table}[ht]\n",
                "\\centering\n",
                "\\begin{adjustbox}{width=1\\textwidth}\n",
                    "\\begin{tabular}{p{0.3\\textwidth}p{0.3\\textwidth}p{0.3\\textwidth}}\n"
        ]

    def leer_csv(self, nombre):
        self.examinados = pd.read_csv(nombre + ".csv", sep = ",")


    def escribir_preambulo(self):
        self.archivo.writelines(self.preambulo)
        self.archivo.writelines(self.inicio_tabla)

    def reconocer_carrera(self,carrera):
        if carrera == "2":
            return "Licenciatura en Matemática Aplicada"
        if carrera == "1":
            return "Licenciatura en Física Aplicada"

    def escribir_ganadores(self):
        aprobados = self.examinados[self.examinados["Resultado"] == "Aprobado"]
        for x in range(aprobados.shape[0]):
            if x!= 0 and x % 3 == 0:
                self.archivo.write("\\newpage")
                self.archivo.write("\\begin{table}[ht] \n" +
	            "\\centering \n"+
	            "\\begin{adjustbox}{width=1\\textwidth}\n"+
				"\\begin{tabular}{p{0.3\\textwidth}p{0.3\\textwidth}p{0.3\\textwidth}}\n")
            self.archivo.write( "%*********************" + str(x) + "**************** \n"+
            "\\begin{tcolorbox}\n" +
	        "\\begin{tikzpicture}[remember picture,overlay,yshift=-5mm, xshift=42mm]\n" +
	        "\\node at (0,0) {\\includegraphics[width=1.1\\textwidth,height=15mm]{header1.jpg}};\n"+
	        "\\end{tikzpicture}\n"+
	        "\\vskip 12mm\n"+
		    "\\begin{center}\n"+
			"\\Large UNIVERSIDAD DE SAN CARLOS DE GUATEMALA   \\\\ \\vskip 0.5mm\n"+
		    "\\Large ESCUELA DE CIENCIAS FÍSICAS Y MATEMÁTICAS  \\\\  \\vskip 3mm\n" +
    		"\\Large \\textbf{CONSTANCIA SATISFACTORIA \\\\ PRUEBA ESPECÍFICA DE MATEMÁTICA } \\\\ \\vskip 1mm\n"+
            "NOV " +  str(aprobados.iloc[x]["NOV"]) + "\\\\ \n"+
    		"CUI " +  '{:.0f}'.format(aprobados.iloc[x]["CUI"]) +  "\\\\ \n"+
            "\\vskip 1mm \n" +
		    "\\end{center}\n"+
	        "\\textbf{Nombre completo:} \\\\ \n" +
            str(aprobados.iloc[x]["Nombre"]) + "  \\\\ \n"+
	        "\\textbf{Carrera:} \\\\" +
	        str( self.reconocer_carrera( str(aprobados.iloc[x]["Carrera"]) ) )  + "\\\\ \n" +
            "\\textbf{Fecha de aprobación:} \\\\"+
            self.fecha_examen +  "\\vskip 10mm \n" +
             "\\begin{center} \n" +
 	        "\\rule{5cm}{0.5pt} \\\\ \n" +
 	         str(self.autoridad) + "\\\\ \n" +
 	        "Secretario Académico \n"
            "\\end{center} \n" +
            "\\textbf{INFORMACIÓN IMPORTANTE:} \\\\" +
            "La consulta de las fechas de inscripción y los pasos a seguir para inscribirse se deben realizar en el sitio web\n" +
            "\\begin{center}\n" +
        	"\\url{www.registro.usac.edu.gt}\n" +
            "\\end{center}\n" +
            "Si por cualquier motivo no puede ingresar al sitio web diríjase al  Departamento\n" +
            "de Registro y Estadística de lunes a viernes de 8:00  a 13:00 horas o al antiguo edificio de CALUSAC oficina 6. \\\\[2mm]\n" +
            "\\begin{tikzpicture}[remember picture,overlay,yshift=-1mm, xshift=8mm]\n"+
            "\\node at (0,0) {\\includegraphics[width=0.35cm,height=0.35cm]{fb.jpg}/ecfmUSAC}; \n"
            "\\end{tikzpicture}\n"+
            "\\begin{tikzpicture}[remember picture,overlay,yshift=-1mm, xshift=8mm]\n" +
            "\\node at (2,0) {\\includegraphics[width=0.35cm,height=0.35cm]{tw.jpg}/UsacEcfm};\n"
            "\\end{tikzpicture}\n" +
            "\\begin{tikzpicture}[remember picture,overlay,yshift=-2mm, xshift=8mm]\n"+
            "\\node at (5.5,0) {\\small\\url{http://ecfm.usac.edu.gt/}};\n"+
            "\\end{tikzpicture}\\\\[1mm]\n" +
            "\\end{tcolorbox}\n"
            )
            if x % 3 != 2 and x != aprobados.shape[0]-1:
                self.archivo.write("&\n")
            else:
                if x == aprobados.shape[0]-1:
                    self.archivo.write( ( 3 - ( (x+1) % 3 ) ) * "&" + "\n" )

                self.archivo.write("\\end{tabular} \n"+
	            "\\end{adjustbox}\n"+
                "\\end{table}\n")

    def terminar_documento(self):
        self.archivo.write("\\end{document}")
        self.archivo.close()


reporte = Reporte("primera_oportunidad2018","31 de agosto de 2018", "Mtr. Edgar Anibal Cifuentes Anléu ")
reporte.leer_csv("primera-oportunidad")
reporte.escribir_preambulo()
reporte.escribir_ganadores()
reporte.terminar_documento()





