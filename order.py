class Order:
    def __init__(self,customer_name,items,discount,total_price):
     self.customer_name=customer_name
     self.items=items
     self.__discount=discount
     self.__total_price=total_price



    def __final_price(self):
         return self.__total_price - self.__discount

    def _admin_view(self):
        return{
            "customer":self.customer_name,
            "items":self.items,
            "discount":self.__discount,
            "total_price":self.__total_price,


        }
    def customer_view(self):
        return{
            "customer":self.customer_name,
            "items":self.items,
            "discount":self.__discount,
            "final_bill": self.__total_price

        }
class admin:
    def show_order(self,order):
        return order._admin_view()
class customer:
    def show_order(self,order):
        return order.customer_view()
order = Order("Mugundhan","pizza",20,80)
customer = customer()
admin = admin()
print(admin.show_order(order))
print(customer.show_order(order))

