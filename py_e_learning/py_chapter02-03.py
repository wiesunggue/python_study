class Car():
    # 클래스의 설명은 반드시 사용하라! Car.__doc__를 통해서 설명에 접근 가능하다

    """
    Car class
    Author : Kim
    Date:2021.01.10
    """
    # 클래스 변수, 네임 스페이스에 없지만 값은 존재, 모든 인스턴스가 공유됨(static과 비슷?)
    # 클래스 변수는 보통 _로 시작하지 않음
    price_per_raise = 1.0

    def __init__(self, company, details):
        # self.car_count=10
        self._company = company
        self._details = details # _붙혀서 선언하면 protected 변수로 선언됨( 실제 protected가 아니라 경고 표시만 뜸)

    def __str__(self):  # 그냥 호출 사용자 입장의 호출, 사용자 level 에서 print 할 때
        return '&str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # 리스트 안에서 호출 객체 그대로 호출, 엄격한 타입에 대한 정보를 호출하는 공식적인 표현
        return '*repr : {} - {}'.format(self._company, self._details)

    # instance Method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company, self._details.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    def get_price_calc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company,
                                                                    self._details.get('price') * Car.price_per_raise)

    @classmethod # 클래스 변수를 받음(price_per_raise), (self는 클래스에 선언된 하나의 변수)
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 Or More")
            return
        cls.price_per_raise = per
        print('Succeed! price increased')

    # Static method 아무 것도 받지 않는 메소드 cls, self 둘다
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not BMW'


# self 의미
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'black', 'horsepower': 400, 'price': 5000})

car1.detail_info()
car2.detail_info()

# 가격 정보 직접 접근
print(car1._details.get('price'))
print(car2._details['price'])

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상 (클래스 메소드 미사용) 직접접근하면 안좋다
Car.price_per_raise = 1.4

# 가격 정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())
# 클래스 매소드 사용
Car.raise_price(1.6)

print(car1.get_price_calc())
print(car2.get_price_calc())

print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car1))  # 이렇게 호출하는 것도 가능
print(car1.__str__)
print(car1)