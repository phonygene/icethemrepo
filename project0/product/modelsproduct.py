from django.db import connection

# class Product:
#     def all(self):
#         with connection.cursor() as cursor:
#             cursor.execute("select * from product")
#             datas = cursor.fetchall()
#         return datas

#     def create(self,product):
#         with connection.cursor() as cursor:
#             sql = """INSERT INTO product(CategoryID,ModelNumber,ModelName,UnitCost,ProductImage,Description)
#                     VALUES(%s,%s,%s,%s,%s,%s)"""
#             cursor.execute(sql,product)
#     # def update(self,product):
#     #     with connection.cursor() as cursor:
#     #         sql = 
class Product:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from product")
            datas = cursor.fetchall()
        return datas
    
    def single(self,id):
        with connection.cursor() as cursor:
            cursor.execute("select * from product where productid=%s",(id,))
            data = cursor.fetchone()
        return data

    def create(self,product):
        with connection.cursor() as cursor:
            sql = """INSERT INTO product(CategoryID,ModelNumber,ModelName,UnitCost,ProductImage,Description)
                     VALUES(%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql,product)

    def update(self,product):
        with connection.cursor() as cursor:
            sql = """UPDATE product set CategoryID=%s,ModelNumber=%s,ModelName=%s,UnitCost=%s,ProductImage=%s,Description=%s
                     where productid=%s"""
            cursor.execute(sql,product)

    def delete(self, id):
        with connection.cursor() as cursor:
            sql = "delete from product where productid=%s"
            cursor.execute(sql,(id,))