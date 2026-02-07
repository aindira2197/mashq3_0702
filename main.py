class Talaba:
    def __init__(self, ism, kurs, baholar):
        self.ism = ism
        self.kurs = kurs
        self.baholar = baholar

    def malumot(self):
        return f"{self.ism}, {self.kurs} - kurs, baholar - {self.baholar}"

    def orta_baho(self):
        return sum(self.baholar) / len(self.baholar)
