import Helper

class Variable:
    def __init__(self, name):
        self.name = name
        self.value = None

    def __str__(self):
        if self.value == None:
            Helper.error()
        return f"{self.value}"
    
    def set_value(self, value):
        try:
            int_value = int(value)
            self.value = int_value
        except ValueError:
            Helper.error()
        
    def get_value(self):
        if self.value == None:
            Helper.error()
        return self.value
    
