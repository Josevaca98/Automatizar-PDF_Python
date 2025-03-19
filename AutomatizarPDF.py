# -*- coding: utf-8 -*-
#Importamos librerías
import pdfkit
import jinja2
from datetime import datetime
import locale

# Configurar idioma a español
locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')

#Variables con nuestros datos
client_name = "José María Vaca González"
item1 = "PlayStation 5"
item2 = "TV"
item3 = "Bocinas"

subtotal1 = 499
subtotal2 = 399
subtotal3 = 129
total = subtotal1 + subtotal2 + subtotal3

today_date = datetime.today().strftime("%A, %d de %B de %Y")

month = datetime.today().strftime("%B")


# diccionario aquí cambiamos las variables de la plantilla del html con nuestra variables
context = {'client_name': client_name, 'today_date': today_date, 'total': f'${total:.2f}', 'month': month,
            'item1': item1, 'subtotal1': f'${subtotal1:.2f}',
            'item2': item2, 'subtotal2': f'${subtotal2:.2f}',
            'item3':item3, 'subtotal3': f'${subtotal3:.2f}'
            }

# Usando la librería jinja2 le decimos que busque en la carpeta de proyectos
template_loader = jinja2.FileSystemLoader('./Proyecto_01_AutomatizarPDF')
template_env = jinja2.Environment(loader=template_loader)

# Asignamos en una variable la plantilla html
html_template = 'plantilla.html'
# Y renderizamos la plantilla
template = template_env.get_template(html_template)
output_text = template.render(context)

# Con la herramienta de wkhtmltopdf creamos el pdf
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
output_pdf_name = r"C:\Users\HBK_j\Desktop\Curso Python\Proyecto_01_AutomatizarPDF\factura.pdf"

pdfkit.from_string(output_text, output_pdf_name, configuration=config, css='./Proyecto_01_AutomatizarPDF/estilo.css')