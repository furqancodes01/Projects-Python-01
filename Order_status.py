from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5
    
class Order:
    def __init__(self,order_id,customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.status = OrderStatus.SHIPPED
        
    def update_status(self,new_status):
        if isinstance(new_status,OrderStatus):
            self.status = new_status
            print(f"Order {self.order_id} updated to {self.status}")
                
        
        
    
    def display(self):
        print (f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Status: {self.status.name}")
        
        
order1 = Order(1001,"Adam")
order2 = Order(1002,"Joy")
order1.display()    
order1.update_status(OrderStatus.PROCESSING)
order2.display()

        