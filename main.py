# class Singleton:
#     _instance = None
#     def __init__(self):
#         if Singleton._instance is not None:
#             raise Exception("Uz je")
#         else:
#             self.meno = "Patrik"
#             Singleton._instance = self
#
#     @staticmethod
#     def getInstance():
#         if Singleton._instance is None:
#             Singleton()
#         return Singleton._instance
#
# s1 = Singleton.getInstance()
# print(s1.meno)
# s2 = Singleton.getInstance()
# s1.meno = "Milan"
# print(s2.meno)
# s3 = Singleton()


# class Document:
#     def create(self):
#         raise NotImplementedError("Metoda create() musi byt prepisana ")
#
# class PDFDocument(Document):
#     def create(self):
#         return "Vytvara PDF dokument"
#
# class WordDocument(Document):
#     def create(self):
#         return "Vytvara Word dokument"
#
# class TXT(Document):
#     def create(self):
#         return "Vytvara TXT dokument"
#
#
# class Factory:
#     def create_document(self,type):
#         if type == "pdf":
#             return PDFDocument()
#         elif type == "word":
#             return WordDocument()
#         elif type == "TXT":
#             return TXT()
#         else:
#             raise ValueError("neznamy typ suboru")
#
# factory = Factory()
# pdf=factory.create_document("pdf")
# print(pdf.create())
#
# word=factory.create_document("word")
# print(word.create())
#
# txt=factory.create_document("TXT")
# print(txt.create())

# class Form:
#     def __init__(self):
#         self.fields = []
#
#     def add_field(self, field):
#         self.fields.append(field)
#
#     def __str__(self):
#         return "\n".join(self.fields)
#
# class FormBuilder:
#     def __init__(self):
#         self.form = Form()
#     def add_name_field(self):
#         self.form.add_field("Name: [__________]")
#         return self
#     def add_adress_field(self):
#         self.form.add_field("Adress: [__________]")
#         return self
#
#     def add_email_field(self):
#         self.form.add_field("email: [__________]")
#         return self
#
#     def add_country_field(self):
#         self.form.add_field("Country: [__________]")
#         return self
#
#     def build(self):
#         return self.form
#
# builder = FormBuilder()
# form = builder.add_name_field().add_adress_field().add_email_field().add_country_field().build()
#
# print(form)