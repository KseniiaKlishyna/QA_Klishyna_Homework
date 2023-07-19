import re
# 1 Чи стрічка містить лише великі і малі літери, числа на нижнє підкреслення.

test_string_1 = r'dftrefg'
match = re.fullmatch(r'\w+', test_string_1)
print('YES' if match else 'NO')

# 2 Напишіть програму, що видаляє область дужок в стрічці

test_string_2 = r'stackoverflow (.com)'
print(re.sub(r'\((.+)\)'," ", test_string_2))

# 3 Напишіть програму, що. вставляє пробіл перед великою літерою
test_string_3 = r'HelloHowAreYou?'
string_w_space = re.sub(r'(?=[A-Z])', ' ', test_string_3)
print(string_w_space)