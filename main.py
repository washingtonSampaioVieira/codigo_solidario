from modules.Administrator import Administrator
from modules.Doctor import Doctor
from modules.Document import Document
from modules.Patient import Patient
from modules.Report import Report
from modules.Talk import Talk
from modules.User import  User
from modules.Voluntary import Voluntary
from modules.Donations import Donations
from modules.Reception import Reception

administrator =  Administrator(1)
user = User("id_user", "name", "email", "password", "telefone", "'created_at'")

doctor = Doctor("endereco", "crm", user)
document = Document("name", "url")
donations = Donations("value", "contact", "cpf", "cnpj")
patient = Patient("name", "address", "diagnosis")
report = Report("name", "url")
voluntary = Voluntary("name", "cpf", "telphone")
talk = Talk("local", "theme", "size", voluntary)
reception = Reception("name", "address", "diagnosis")

print("FOI")
