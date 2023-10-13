class Car():
    # 클래스의 설명은 반드시 사용하라! Car.__doc__를 통해서 설명에 접근 가능하다

    """
    Car class
    Author : Kim
    Date:2019.11.08
    """
    # 클래스 변수, 네임 스페이스에 없지만 값은 존재, 모든 인스턴스가 공유됨(static과 비슷?)
    # 클래스 변수는 보통 _로 시작하지 않음
    car_count = 0
    def __init__(self, company, details):
        self.car_count=10 #만약 car1에서 접근시키면 우선 접근한다
        self._company = company
        self._details = details
        Car.car_count+=1
    def __str__(self):  # 그냥 호출 사용자 입장의 호출, 사용자 level 에서 print 할 때
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # 리스트 안에서 호출 객체 그대로 호출, 엄격한 타입에 대한 정보를 호출하는 공식적인 표현
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company,self._details.get('price')))

    def __del__(self): # 실행 종료시 반드시 __del__이 실행됨(메모리 할당 해제)
        print("del 호출")
        Car.car_count-=1
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'black', 'horsepower': 400, 'price': 8000})
car3 = Car('BMW', {'color': 'black', 'horsepower': 600, 'price': 1000})

print(id(car1))
print(id(car2))
print(id(car3))

# car1 is car2 vs car1 == car2 is문법은 car1과 car2의 주소가 같은지 판단하고, car1==car2는 값이 같은지 판단한다.
# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))
# 클래스에 정의된 메소드(함수) 출력한다
print(car1.__dict__)
print(car2.__dict__)

car1.detail_info()

print(car1.__class__, car2.__class__)
print(id(car1.__class__),id(car2.__class__),id(car3.__class__))

# 에러
# Car.detail_info()
# 비교
Car.detail_info(car2)
car2.detail_info()

print(Car.car_count)
print(car1.car_count)
print(dir(car1)) #클래스 변수도 나온다
print(car1.__dict__) #클래스 변수는 안나온다

del car2
# 삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 자동으로 검색한다.
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
print(Car.__doc__)