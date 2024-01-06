# sariq dev copy
# x=10
# print(type(x))
# matn='salom'
# print(type(matn))
# print(matn.upper())
# print(x.upper)

# def salom():
#     print('assalom alekom')

# print(type(salom))

# class Talaba:
#     def __init__(self,ism,familya,tyil):
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil

#     def get_nema(self):
#         return self.ism
    
#     def get_age(self,yil):
#         return yil - self. tyil

#     def get_lastname(self):
#         return self.familya

#     def tanishtir(self):
#         return f"ismim {self.ism} {self.familya}. tug'ligan yilim {self.tyil}"

# talaba1=Talaba("oybek",'komiljonov',2010)        
# talaba2=Talaba("azizbek",'islomiv',2009)        
# talaba3=Talaba("jamshid",'davlatboyev',2009)               

# sariq dev copy 2

# class Talaba:
#     """"TALABA nomil klass yaratamiz"""
#     def __init__(self,ism,familya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#         self.bosqich=1

#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         self.bosqich += 1

# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

# talaba1.update_bosqich() 
# print(talaba1.get_info())

# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

