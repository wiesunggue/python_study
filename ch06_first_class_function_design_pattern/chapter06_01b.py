# 함수지향 전략
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity


class Order:  # 콘텍스트
    
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple',10, 1.5),
        LineItem('watermellon',5,5.0)]


print(Order(joe,cart, fidelity_promo))
print(Order(ann,cart,fidelity_promo))
banana_cart = [LineItem('banana',30,0.5),
               LineItem('apple',10,1.5)]

print(Order(joe, banana_cart, bulk_item_promo))

long_order = [LineItem(str(item_code),1,1.0)
              for item_code in range(10)]
print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))


promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    """최대로 할인받은 금액을 반환한다.
    """
    return max(promo(order) for promo in promos)

# promos를 만드는 방법은 없을까?
# 내장 함수 globals()
# 현재 전역 심벌 테이블을 나타내는 딕셔너리 객체를 반환한다. 이 딕셔너리는 언제나 현재 모듈에 대한 내용을 담고 있다.
# (함수나 메서드 안에서 호출할 때, 함수를 호출한 모듈이 아니라 함수가 정의된 모듈을 나타낸다.)

# 이름의 마지막에 _promo가 들어간 것들의 list를 구성하여 준다
promos = [globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promo']
print(promos)

#
import inspect
from chapter06_01a import Promotion
promos = [func for name, func in inspect.getmembers(Promotion, inspect.isfunction)]
print(promos)

# inspect.getmembers() 함수는 조건식으로 걸러낸 객체의 속성들을 반환한다.
# insepct.isfunction은 함수인 것만 참을 반환한다.
