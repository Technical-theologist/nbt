from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class GeneratePdf():
    def __init__(self, filename):
        self.canvas = canvas.Canvas(filename, pagesize=letter)
        self.width, self.height = letter
        self.y_position = self.height - 100

        # self.y_position -= 120
        image_path = "assets/logo.jpg"  # Replace with your image path
        self.canvas.drawImage(image_path, 150, self.y_position, width=300, height=100)
        self.y_position -= 50

    def defineLayout(self):
        if self.y_position < 100:
            self.y_position = self.height - 100
            self.canvas.showPage()
    
    def drawLine(self):
        self.canvas.setStrokeColor(colors.grey)  # Set line color to grey
        self.canvas.setLineWidth(1)
        self.canvas.line(50, self.y_position, self.width - 50, self.y_position)
        self.y_position -=20
    
    def insertTitleError(self, errorMessage):
        self.defineLayout()
        self.canvas.setFillColor(colors.red)
        self.canvas.setFont("Helvetica", 20)
        self.canvas.drawString(50, self.y_position, errorMessage)
        self.canvas.setFillColor(colors.black)
        self.y_position -= 23
    
    def insertErrorMessage(self, errorMessage):
        # self.defineLayout()
        self.canvas.setFont("Helvetica",12)
        self.canvas.setFillColor(colors.red)
        self.canvas.drawString(30, self.y_position, errorMessage)
        self.y_position -= 15
        self.canvas.setFillColor(colors.black)
    
    def insertLoginTest(self, username, password, assertion):
        print("In insert login test")
        self.defineLayout()
        self.canvas.setFont("Helvetica", 30)
        self.canvas.drawString(250, self.y_position, "Login")
        self.y_position -= 35
        # Username
        self.canvas.setFont("Helvetica", 12)
        self.canvas.drawString(50, self.y_position, "Email: "+username)
        self.y_position -= 15
        # Password
        self.canvas.setFont("Helvetica", 12)
        self.canvas.drawString(50, self.y_position, "Password: "+password)
        self.y_position -= 15
        if not assertion:
            self.canvas.setFillColor(colors.red)
            self.canvas.setFont("Helvetica", 12)
            self.canvas.drawString(50, self.y_position, "Invalid EmailId or password")
        elif assertion:
            self.canvas.setFillColor(colors.green)
            self.canvas.setFont("Helvetica", 12)
            self.canvas.drawString(50, self.y_position, "Login Successful")
        self.y_position -= 15

    def insert_product_name(self, productname):
        print("Product name:", productname)
        self.defineLayout()
        self.canvas.setFont("Helvetica", 20)
        self.canvas.drawString(50, self.y_position, f"Product Name: {productname}")
        self.y_position -= 30

    def insert_Tag_name(self, tagname):
        print("Tag name:", tagname)
        self.defineLayout()
        self.canvas.setFont("Helvetica", 18)
        self.canvas.setFillColor(colors.blue)
        self.canvas.drawString(50, self.y_position, f"Tag: {tagname}")
        self.y_position -= 30

    def insert_year(self,years):
        print("Year:", years)
        self.defineLayout()
        self.canvas.setFont("Helvetica", 12)
        self.canvas.setFillColor(colors.black)
        self.canvas.drawString(50, self.y_position, f"Year: {years}")
        self.y_position -= 20

    def insert_vaccine(self,vaccinestring):
        print("Vaccine:", vaccinestring)
        self.defineLayout()
        self.canvas.setFont("Helvetica", 12)
        self.canvas.setFillColor(colors.black)
        self.canvas.drawString(50, self.y_position, f"Vaccine: {vaccinestring}")
        self.y_position -= 20

    def insertTagStartNumber(self,tagnumber):
        print("Vaccine:", tagnumber)
        self.defineLayout()
        self.canvas.setFont("Helvetica", 12)
        self.canvas.setFillColor(colors.black)
        self.canvas.drawString(50, self.y_position, f"Tag start number : {tagnumber}")
        self.y_position -= 20
    def insertLine(self,line_string):
        print("Line String", line_string)
        self.defineLayout()
        self.canvas.setFont("Helvetica", 12)
        self.canvas.setFillColor(colors.black)
        self.canvas.drawString(50, self.y_position,line_string)
        self.y_position -= 20

    def save(self):
        self.canvas.save()