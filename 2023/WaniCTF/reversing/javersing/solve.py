"""
http://www.javadecompilers.com/result?currentfile=javersing.java
"""

s = "Fcn_yDlvaGpj_Logi}eias{iaeAm_s"

inv7 = pow(7, -1, 30)

for i in range(30):
    print(s[i * inv7 % 30], end='')
