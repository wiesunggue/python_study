# 6.1 사례: 전략 패턴의 리팩토링
# 전략 패턴은 파이썬에서 함수를 일급 객체로 사용하면 더욱 간단해질 수 있는 디자인 패턴의 대표적인 사례이다.

# 콘텍스트
# 일부 계산을 서로 다른 알고리즘을 구현하는 교환 가능한 컴포넌트에 위임함으로써 서비스를 제공한다.
# 전자상거래 예제에서 콘텍스트는 Order로서, 여러 알고리즘 중 하나에 따라 프로모션 할인을 적용하도록 설정된다.

# 전략
# 여러 알고리즘을 구현하는 컴포넌트에 공통된 인터페이스, 전자상거래 예제에서는 이 역할을 Promotion이라는 추상 클래스가 담당한다.

# 구체적인 전략
# 전략의 구상 서브클래스 중 하나. 여기서는 FidelityPromo, BulkItemPromo, LargeOrderPromo등 총 3개의 구체적인 전략이 구현되어 있다.

# 일련의 알고리즘을 정의하고 각가을 하나의 클래스 안에 넣어서 교체하기 쉽게 만든다.
# 전략을 이용하면 사용하는 클라이언트에 따라 알고리즘을 독립적으로 변경할 수 있다.

# 전자상거래 규칙
# 1. 충성도 포인트가 1000점 이상인 고객은 전체 주문에 대해 5% 할인을 적용한다
# 2. 하나의 주문에서 20개 이상의 동일한 상품을 구입하면 해당 상품에 대해 7% 할인을 적용한다.
# 3. 서로 다른 상품을 10종류 이상 주문함녀 전체 주문에 대해 7% 할인을 적용한다.
# 하나의 주문에는 하나의 규칙만 적용한다.


# 고전적인 전략
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer','name fidelity')

class LineItem:
    
    def __init__(self,product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
        
    def total(self):
        return self.price * self.quantity
    
class Order:
    
    def __init__(self,customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(),self.due())
    
class Promotion(ABC): # 추상 베이스 클래스
    
    @abstractmethod
    def discount(self,order):
        """할인액을 구체적인 숫자로 반환한다."""

class FidelityPromo(Promotion): #  첫 번째 구체적인 전략
    """충성도 점수가 1000점 이상인 고객에게 전체 5% 할인 적용"""
    
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0
    
class BulkItemPromo(Promotion): # 두 번째 구체적이 전략
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""
    
    def discount(self,order):
        discount=0
        for item in order.cart:
            if item.quantity >=20:
                discount += item.total() * .1
        return discount
    
class LargeOrderPromo(Promotion): # 세 번째 구체적인 전략
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""
    
    def discount(self, order):
        discount_items = {item.product for item in order.cart}
        if len(discount_items) >= 10:
            return order.total() * .07
        return 0

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple',10, 1.5),
        LineItem('watermellon',5,5.0)]


print(Order(joe,cart, FidelityPromo()))
print(Order(ann,cart,FidelityPromo()))
banana_cart = [LineItem('banana',30,0.5),
               LineItem('apple',10,1.5)]

print(Order(joe, banana_cart, BulkItemPromo()))

long_order = [LineItem(str(item_code),1,1.0)
              for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))

