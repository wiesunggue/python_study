# 7.3 데커레이터로 개선한 전략 패턴

#6.1에서 전략 패턴의 리팩토링에서 구현한 전자상거래 프로모션의 할인 코드를 개선하는데 데코레이터를 사용

promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """10종류 이상의 상품을 구매하면 전체 7% 할인 적용"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    """최대로 할인받을 금액을 반환한다.
    """
    return max(promo(order) for promo in promos)


# 6.1 코드에 비해서 나은 점
# 프로모션 전략 함수명이 특별한 형태로 되어 있을 필요 없다
# @promotion 데커레이터는 데커레이트된 함수의 목적을 명확히 알려주며, 임시로 어떤 프로모션을 배제할 수 있다. 단지 데커레이터만 주석 처리하면 된다
# 프로모션 할인 전략을 구현한 함수는 @promotion 데커레이터가 적용되는 한 어느 모듈에서든 정의할 수 있다.
