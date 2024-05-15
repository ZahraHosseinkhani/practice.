class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_polynomial(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            current = current.next
        print()

    def add_polynomials(self, poly1, poly2):
        result = LinkedList()
        current1 = poly1.head
        current2 = poly2.head
        while current1 and current2:
            if current1.exponent == current2.exponent:
                result.add_node(current1.coefficient + current2.coefficient, current1.exponent)
                current1 = current1.next
                current2 = current2.next
            elif current1.exponent > current2.exponent:
                result.add_node(current1.coefficient, current1.exponent)
                current1 = current1.next
            else:
                result.add_node(current2.coefficient, current2.exponent)
                current2 = current2.next

        while current1:
            result.add_node(current1.coefficient, current1.exponent)
            current1 = current1.next
        while current2:
            result.add_node(current2.coefficient, current2.exponent)
            current2 = current2.next

        return result

    def multiply_polynomials(self, poly1, poly2):
        result = LinkedList()
        current1 = poly1.head
        while current1:
            current2 = poly2.head
            while current2:
                coeff = current1.coefficient * current2.coefficient
                exp = current1.exponent + current2.exponent
                result.add_node(coeff, exp)
                current2 = current2.next
            current1 = current1.next

        return result

# گرفتن چندجمله‌ای اول از کاربر
poly1 = LinkedList()
num_terms1 = int(input("تعداد اصطلاحات چندجمله‌ای اول را وارد کنید: "))
for _ in range(num_terms1):
    coefficient = float(input("ضریب را وارد کنید: "))
    exponent = int(input("توان را وارد کنید: "))
    poly1.add_node(coefficient, exponent)

# گرفتن چندجمله‌ای دوم از کاربر
poly2 = LinkedList()
num_terms2 = int(input("تعداد اصطلاحات چندجمله‌ای دوم را وارد کنید: "))
for _ in range(num_terms2):
    coefficient = float(input("ضریب را وارد کنید: "))
    exponent = int(input("توان را وارد کنید: "))
    poly2.add_node(coefficient, exponent)

# چاپ چندجمله‌ای اول و دوم
print("چندجمله‌ای اول:")
poly1.print_polynomial()
print("چندجمله‌ای دوم:")
poly2.print_polynomial()

# جمع چندجمله‌ای ها
sum_poly = LinkedList()
sum_poly = sum_poly.add_polynomials(poly1, poly2)
print("مجموع چندجمله‌ای:")
sum_poly.print_polynomial()

# ضرب چندجمله‌ای ها
mul_poly = LinkedList()
mul_poly = mul_poly.multiply_polynomials(poly1, poly2)
print("حاصلضرب چندجمله‌ای:")
mul_poly.print_polynomial()