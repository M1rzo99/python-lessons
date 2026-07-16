
# 30-dars. Vorislik va Poliformizm
# Klasslardan klasslar yaratishni o'rganamiz.

#  Obyektga yo'naltirilgan dasturalshning qulayliklaridan biri bu klasslardan boshqa klasslar yaratishdir.
# Bizga kerak bo'lgan yangi klass\, avval yaratilgan klass bn o'xshashlik joylari bo'lsa, biz bu klassdan voris klass yaratishimiz mn.
# Bunda asl klass ota yoki super klass deb ataladi.
# Super klasdan yaratilgan voris klass, superClassning barcha yoki tanlangan xususiyatlari va methodlarini meros olish bn birga,o'ziga xos xususiyat va methodlarga ega bo'ladi.

# Shaxs nomli class yaratamiz, va bu class boshqa classlar un super class vazifasini bajaradi.

class Shaxs:
    """Shaxs haqida ma'lumot """
    def __init__(self,ism,familya,passport,tyil):
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """shaxs haqida ma'lumot method"""
        info = f"{self.ism} {self.familya}."
        info += f"Passport: {self.passport} va {self.tyil} - yilda tug'ilgan"
        return info
    
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi method"""
        return yil - self.tyil 
# Classni etekshirib ko'ramiz

shaxs1 = Shaxs("Mirzo","Shomuaratov","FA0342323", 1999)
print(shaxs1.get_info())
print(shaxs1.get_age(2026))

