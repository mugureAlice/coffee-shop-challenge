class Customer:
    def _init_(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self.name = name
            else:
                return("Must be a str with 1 to 15 characters")    

     def get_name(self):
        self.name

  
