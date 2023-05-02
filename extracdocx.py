from docx2python import docx2python
filepath= "Iso_manuals/ITE-SYPE-PLA-001 Instructivo Coordinacion de la produccion Rev.04.docx"
with docx2python(filepath) as output:
    output.save_images('images')
    text= output.text
with open('output.txt','w') as text_output: 
    text_output.write(str(text))


        