p = 1719620105458406433483340568317543019584575635895742560438771105058321655238562613083979651479555788009994557822024565226932906295208262756822275663694111
M = random_matrix(GF(p), 5)

period = multiplicative_order(det(M ** 3))

while True:
    for x in range(3, 100):
        m = multiplicative_order(det(M ** x))
        if period % m == 0:
            print(x)
