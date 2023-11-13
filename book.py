import math
# # kapak_fiyati = 24.95
# # kargo_ücreti = 3 
# # ek_kopya = 0.75

# # sonuc = kapak_fiyati * 40 / 100 + kargo_ücreti  + (ek_kopya * 60)
# # print(sonuc)


# # def tekrar(samet):
# #     print(samet)
# #     print(samet)

# # def draw_grid(rows, columns):
# #     row_separator = "+ " + "- " * (columns // 2) + "+ " + "- " * (columns // 2) + "+"
# #     cell = "| " + "  " * (columns // 2) + "| " + "  " * (columns // 2) + "|"

# #     for _ in range(rows // 2):
# #         print(row_separator)
# #         for _ in range(columns // 2):
# #             print(cell)
# #     print(row_separator)


# # rows = 4
# # columns = 8


# # draw_grid(rows, columns)
# # import turtle
# # bob = turtle.Turtle()
 
# # def ornek(x,y):
# #     if x > y :
# #         print(1)
# #     elif x == y:
# #         print(0)
# #     elif x < y: 
# #         print(2)

# # ornek(5,3)
# import math
# def mesafe(x1,x2,y1,y2):
#     dx = x2 - x1
#     dy = y2 - y1 
#     dsquare = dx**2 + dy**2
#     result = math.sqrt(dsquare)
#     print(result)
#     # print('dx is ', dx)
#     # print('dy is ', dy)
#     return result
# mesafe(1,2,4,6)

# def hipotenus(a,b,c):
#     a = int(input("A kenarinin uzunlugunu giriniz: "))
#     b = int(input("B kenarinin uzunlugunu giriniz: "))
#     c = math.sqrt(a**2 + b**2)
#     print("Hipotenüs: ",int(c))
#     return c
# hipotenus(3,4,5)
def factorial(n):
    if n == 0:
        return 1 
    else:
        faktoriyel = 1 
        result =+ faktoriyel * n
        n =- 1
        print(result)
factorial(5) 
        