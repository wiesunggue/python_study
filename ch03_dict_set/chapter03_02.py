# 지능형 딕셔너리

DIAL_CODES = [
    (86,'China'),
    (91,'India'),
    (1,'United States'),
    (62,'Indonesia'),
    (55,'Brazil'),
    (92,'Parkistan'),
    (880,'Banladesh'),
    (234,'Nigeria'),
    (7,'Russia'),
    (81,'Japan'),
]

country_code ={country: code for code, country in DIAL_CODES}
print(country_code)

print({code : country.upper() for country, code in country_code.items() if code <66})
