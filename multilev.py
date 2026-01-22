#multilevel inheritence
class Factorylucknow():
    def __init__(self,size,weight):
        self.size=size
        self.weight=weight
class FactoryBallia(Factorylucknow):
    def __init__(self, size, weight,material):
        super().__init__(size, weight)
        self.material=material
class FactoryRasra(FactoryBallia):
    def __init__(self, size, weight, material,type):
        super().__init__(size, weight, material)
        self.type=type
        
        obj=FactoryRasra()
        