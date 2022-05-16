from fpdf import FPDF

class pdf(FPDF):
    pass
    def logo(self,name,x, y, x, w, h ):
        self.image(name,x, y, x, w, h )

    def texts(self, name):
        with open(name, 'rb') as xy:
            txt=xy.read().decode('latin-1')
        self.set_xy(10.0,80.0)
        self.set_text_color(76-0,32.0,250.0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0,10,txt)

    def titles(self, title):
        self.set_xy(0.0,0.0)
        self.set_font('Arial','B',16)
        self.set_text_color(250,50,50)
        self.cell(w=210.0, h=40.0, align='C', txt=title,border=0)

    pdf = FPDF()
    pdf.add_page()
    pdf.logo('logo.png', 0, 0, 60, 15)
    pdf.texts('Hola_Mundo.pdf')
    pdf.texts('Hola Mundo!!')
    pdf.set_author('Mariana Casella')
    pdf.output('test.pdf', 'F')