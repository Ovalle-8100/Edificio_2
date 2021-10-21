import xml.etree.cElementTree as et

root = et.Element("TIC")

se = et.SubElement(root, "Desarrollo_de_Software")
et.SubElement(se, "Matricula").text = "18040023"
et.SubElement(se, "Nombre").text = "Gregorio Azael Ovalle Macias"

et.SubElement(se, "Matricula").text = "18040024"
et.SubElement(se, "Nombre").text = "Cristina Guadalupe Quiroz Macias"

et.SubElement(se, "Matricula").text = "18040025"
et.SubElement(se, "Nombre").text = "Miriam Yuvicela Reyes Macias"

et.SubElement(se, "Matricula").text = "18040026"
et.SubElement(se, "Nombre").text = "Jorge Eduardo Ovalle Macias"

et.SubElement(se, "Matricula").text = "18040027"
et.SubElement(se, "Nombre").text = "Axel Betancourt Ovalle"

se = et.SubElement(root, "Redes_Inteligentes_y_Ciberseguridad")
et.SubElement(se, "Matricula").text = "18040078"
et.SubElement(se, "Nombre").text = "Xochitl Anahi Ovalle Macias"

et.SubElement(se, "Matricula").text = "18040079"
et.SubElement(se, "Nombre").text = "Susana Elizabeth Ovalle Macias"

et.SubElement(se, "Matricula").text = "18040080"
et.SubElement(se, "Nombre").text = "Armando Jared Betancourt Ovalle"

et.SubElement(se, "Matricula").text = "18040081"
et.SubElement(se, "Nombre").text = "Reyna Giselle Martinez Ovalle"

et.SubElement(se, "Matricula").text = "18040082"
et.SubElement(se, "Nombre").text = "Abdiel Omar Betancourt Ovalle"

se = et.SubElement(root, "Multimedia")
et.SubElement(se, "Matricula").text = "18040056"
et.SubElement(se, "Nombre").text = "Lorenzo de Jesus Martinez Rodriguez"

et.SubElement(se, "Matricula").text = "18040057"
et.SubElement(se, "Nombre").text = "Miguel Rodriguez Granados"

et.SubElement(se, "Matricula").text = "18040057"
et.SubElement(se, "Nombre").text = "Ernestina Macias Lucio"

et.SubElement(se, "Matricula").text = "18040058"
et.SubElement(se, "Nombre").text = "Sotero Ovalle Alamillo"

et.SubElement(se, "Matricula").text = "18040059"
et.SubElement(se, "Nombre").text = "Andrea Guadalupe Rojas Lopez"

tree = et.ElementTree(root)
tree.write("TIC.xml", xml_declaration=True)
