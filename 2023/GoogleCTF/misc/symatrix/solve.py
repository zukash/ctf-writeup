import re

with open("encoder.c", "r") as f:
    F = f.read()
# F = """
# aaaa
#   /* "encoder.py":67
#  * base_image.close()
#  *
#  * print("Work done!")             # <<<<<<<<<<<<<<
#  * exit(1)
#  */
#   if (__Pyx_PrintOne(0, __pyx_kp_s_Work_done) < 0) __PYX_ERR(0, 67, __pyx_L1_error)

#   /* "encoder.py":68
#  *
#  * print("Work done!")
#  * exit(1)             # <<<<<<<<<<<<<<
#  */
#   __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_exit, __pyx_tuple__16, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 68, __pyx_L1_error)
#   __Pyx_GOTREF(__pyx_t_1);
#   __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

#   /* "encoder.py":1
#  * from PIL import Image             # <<<<<<<<<<<<<<
#  * from random import randint
#  * import binascii
#  */
# """
# print(re.findall(r"\/\*.*encoder\.py.*?\*\/", F, flags=re.DOTALL))
hits = re.findall(r"encoder\.py[^\/]*\*\/", F, flags=re.DOTALL)

print(len(hits))

for i in range(len(hits)):
    line = re.findall(r'encoder\.py":(\d+)', hits[i])
    hits[i] = (int(line[0]), hits[i])

hits.sort()

for l, h in hits:
    print(h)
