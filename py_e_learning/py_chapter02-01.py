car_company = 'Ferrari'
car_detail_1 = [{'color': 'White'},
                {'horsepower': 400},
                {'price': 8000}
                ]
car_detail_2 = [{'color': 'White'},
                {'horsepower': 400},
                {'price': 8000}
                ]

car_detail_3 = [{'color': 'White'},
                {'horsepower': 400},
                {'price': 8000}
                ]
# 리스트 구조
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 400, 'price': 5000},
    {'color': 'Red', 'horsepower': 400, 'price': 8000}
]

# del car_company_list[1]
# del car_detail_list[1]

# print(car_company_list)
# print(car_detail_list)
# print()
# print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'bmw', 'car_detail': {'color': 'black', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}}
]


# del car_dicts[2]
# car_dicts[2].pop('car_company')
# print(car_dicts)

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):  # 그냥 호출 사용자 입장의 호출, 사용자 level 에서 print 할 때
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # 리스트 안에서 호출 객체 그대로 호출, 엄격한 타입에 대한 정보를 호출하는 공식적인 표현
        return 'repr : {} - {}'.format(self._company, self._details)


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'black', 'horsepower': 400, 'price': 8000})
# print(dir(car1)) #dir은 모든 메타정보를 표현함
# print(car2)
# print(car1.__dict__) # 네임스페이스 내부에 존재하는 속성정보 딕셔너리로 출력
# print() #print시 str메소드를 우선으로 실행하지만, 없다면 repr을 실행함 둘다 없다면 클래스의 정보 표시
# print()

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
print(car_list)  # 리스트 호출

for x in car_list:
    print(x)  # 그냥 호출
