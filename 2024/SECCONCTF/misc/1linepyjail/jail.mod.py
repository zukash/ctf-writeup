print(
    eval(code, {}, {})
    if len(code := input("jail> ")) <= 100
    and __import__("re").fullmatch(r"([^()]|\(\))*", code)
    else ":("
)
