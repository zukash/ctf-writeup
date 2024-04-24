#include <iostream>

void win() {
  std::system("/bin/sh");
}

// xxxxxxxxxxxxxxxzzzzzzzzyyyyy

// _name
// xxxxxxx xxxxxxxx zzzzzzzz yyyyy00
// sss

void input_person(int& age, std::string& name) {
  int _age;
  char _name[0x100];
  std::cout << "What is your first name? ";
  std::cin >> _name;
  std::cout << "How old are you? ";
  std::cin >> _age;
  name = _name;
  age = _age;
}

"""
0x000: &name
0x008: &age
---
0x010: _age
0x018: _name
---
0x :canary
---
0x130: saved_rbp
return_addr
---
main_local_varia ble
"""


"""
basic_string_(_name, name)


A
-----
pointer
---
size
---
xxxxxxx
"""

"""
A: _name
-----
pointer -> local_buf
---
size
---
local_buf = win_addr
"""

"""
B: name
-----
0x130: pointer -> _stack_check_fail
---
size 大きい 0x404050
---
capcity or local_buf
"""

int main() {
  int age;
  std::string name;
  input_person(age, name);
  std::cout << "Information:" << std::endl
            << "Age: " << age << std::endl
            << "Name: " << name << std::endl;
  return 0;
}

__attribute__((constructor))
void setup(void) {
  std::setbuf(stdin, NULL);
  std::setbuf(stdout, NULL);
}
