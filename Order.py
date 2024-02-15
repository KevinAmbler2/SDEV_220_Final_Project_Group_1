class Order():
    def __init__(self,  order_id, order_type, order_date):
        self.order_id = order_id
        self.order_type = order_type
        self.order_date = order_date

    def finalize(self, products):
        # calculate price and taxes and what not
        product = products[self.order_type]
        
        return product.price() # just return price for now until tax rate and all that is figured
