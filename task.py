class MacBook():
    marka = "Apple MacBook"
    def __init__(self, model, rəng, operativyaddaş, ssd=False):
        
        self.model = model
        self.rəng = rəng
        self.operativyaddaş = operativyaddaş
        self.ssd = ssd
        
    def açılış_sürəti(self):
        return f"{self.marka} {self.model} açılış sürəti: 5 saniyə"

    def operativ_yaddaş(self):
        return f"{self.marka} {self.model} operativ yaddaş(RAM): {self.operativyaddaş}"

    def performans_testi(self):
        if self.ssd:
            return f"{self.marka} {self.model} performans testinin nəticəsi: Mükəmməl"
        else:
            return f"{self.marka} {self.model} performans testinin nəticəsi: Ortadır"
        
macbook1 = MacBook("Pro", "Gümüş", "16 GB RAM", ssd=True)
print(macbook1.açılış_sürəti())
print(macbook1.operativ_yaddaş())
print(macbook1.performans_testi())

