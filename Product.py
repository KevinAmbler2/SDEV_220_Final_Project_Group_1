class Product():
    def __main__(self, product_type, product_xml):
        self.product_type = product_type
        self.product_name = product_xml.find("Name").text
        self.product_price = float(product_xml.find("Price").text)
    
    def price(self):
        return self.product_price
    
    def name(self):
        return self.product_name
    
    def type(self):
        return self.product_type