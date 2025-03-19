# Automatización de Facturas en PDF  

Este proyecto genera automáticamente facturas en formato PDF a partir de una plantilla HTML y datos dinámicos. Se utiliza `jinja2` para la renderización de plantillas y `pdfkit` para la conversión de HTML a PDF.  

## 📌 Características  
- ✅ Generación de facturas en PDF con datos personalizados.  
- ✅ Uso de plantillas HTML con `jinja2`.  
- ✅ Conversión de HTML a PDF con `pdfkit`.  
- ✅ Soporte para formatos de moneda y fechas en español.  

## 🛠 Tecnologías utilizadas  
- Python  
- `pdfkit`  
- `jinja2`  
- `datetime`  
- `locale`  

## 🚀 Cómo usar  
1. Asegúrate de tener instalado [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html).  
2. Ubica los archivos necesarios en la carpeta `Proyecto_01_AutomatizarPDF/`.  
3. Asegúrate de que la plantilla HTML (`plantilla.html`) y la hoja de estilos CSS (`estilo.css`) están en la carpeta.  
4. Ejecuta el script y el archivo PDF generado se guardará en la ubicación definida.  

## 📂 Estructura del Proyecto  
```
Proyecto_01_AutomatizarPDF/
│── plantilla.html          # Plantilla HTML para la factura
│── estilo.css              # Estilos CSS para la factura
│── script.py               # Script principal
│── factura.pdf             # Factura generada
```

## 📜 Licencia  
Este proyecto es de uso libre.  

---
👨‍💻 **Desarrollado por:** José María Vaca González  
📧 **Contacto:** [licjmvg98@gmail.com](mailto:licjmvg98@gmail.com)

![PDF_Automatizado](https://github.com/user-attachments/assets/f79b7f16-d9ac-44dc-98fc-7cc48270e5b9)
