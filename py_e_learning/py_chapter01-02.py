import pendulum
from datetime import datetime

pst = pendulum.timezone('America/Los_Angeles')
ist = pendulum.timezone('Asia/Seoul')
print(1)
print(type(pst))

print('Current Date Time in PST = ', datetime.now(pst))
print('Current Date Time in IST = ', datetime.now(ist))

