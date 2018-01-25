from django.db import connection

# class foods:
#     def all(self):
#         with connection.cursor() as cursor:
#             cursor.execute("select * from foods")
#             datas = cursor.fetchall()
#         return datas

#     def create(self,foods):
#         with connection.cursor() as cursor:
#             sql = """INSERT INTO foods(CategoryID,ModelNumber,ModelName,UnitCost,foodsImage,Description)
#                     VALUES(%s,%s,%s,%s,%s,%s)"""
#             cursor.execute(sql,foods)
#     # def update(self,foods):
#     #     with connection.cursor() as cursor:
#     #         sql = 
class Foods:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from foods")
            datas = cursor.fetchall()
        return datas
    
    def single(self,id):
        with connection.cursor() as cursor:
            cursor.execute("select * from foods where id=%s",(id,))
            data = cursor.fetchone()
        return data

    def create(self,foods):
        with connection.cursor() as cursor:
            sql = """INSERT INTO foods(Foodname,FoodType,IcedDate,ExpireDate,FoodImg,Description)
                     VALUES(%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql,foods)

    def update(self,foods):
        with connection.cursor() as cursor:
            sql = """UPDATE foods set Foodname=%s,FoodType=%s,IcedDate=%s,ExpireDate=%s,FoodImg=%s,Description=%s
                     where id=%s"""
            cursor.execute(sql,foods)

    def delete(self, id):
        with connection.cursor() as cursor:
            sql = "delete from foods where id=%s"
            cursor.execute(sql,(id,))

    def sort(self , foodid):
        with connection.cursor() as cursor:
            sql = """INSERT INTO foods(FoodId)
                     VALUES(%s)"""
            cursor.execute(sql,foods)