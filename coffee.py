class Coffee:
    def _init_(self, name):
        if not isinstance(name, str) or len(name) < 3:
            return("Name must be a string with at least 3 characters.")
        self._name = name
           
      def get_name(self):
        return self.name   

        
