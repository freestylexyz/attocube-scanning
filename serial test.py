from pylablib.devices import Attocube
# import time
# atc1 = Attocube.ANC300("COM5")  # USB or RS232 connection
# x = atc1.get_mode()
# print([i for i in x.values()])
# atc1.enable_axis(1, 'off')
# y=atc1.is_enabled()
# atc1.measure_capacitance()
# print('measured')
# print(atc1.get_frequency(4))
# a=[0,1,2,3,4,5]
# print(a[4:])
# print(type(y))
# print(atc1.get_capacitance(1))

# print(atc1.is_enabled())
# x = atc1.get_output(1)
# y = 1 if x==0 else 0
# atc1.set_offset(1, y)
# time.sleep(0.01)
# print(y==atc1.get_output(1))
# atc1.close()
# from qcodes.instrument_drivers.stanford_research.SR860 import SR860
# sr860 = SR860('SR860', 'USB0::0xB506::0x2000::003476::INSTR')
# sr860.frequency(300)
# print(sr860.X())
# print(int(1.6))
# for i in range(5):
#     for j in range(5):
#         if j == 3:
#             break
#         print(i, j)
#     if j == 3:
#         break

# def swich(x):
#     match x:
#         case 0:
#             return "zero"
#         case 1:
#             return "one"
#         case 2:
#             return "two"
#         case default:
#             return "something"
# import numpy as np
# x = np.ones((5,5))
# x[2,3]=2
# x[3:,:] = 3
# x[2:,4:] = 3
# print(x)
x, y, z = [0,1,2]
print(x)

