from django.db import connection

class Product:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from product")
            datas = cursor.fetchall()
        return datas

    def create(self,product):
        with connection.cursor() as cursor:
            sql = """INSERT INTO product(CategoryID,ModelNumber,ModelName,UnitCost,ProductImage,Description)
                    VALUES(%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql,product)
    # def update(self,product):
    #     with connection.cursor() as cursor:
    #         sql = 