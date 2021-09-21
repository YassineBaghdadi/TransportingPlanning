from index import *
import random
cnx = con()
cur = cnx.cursor()
alph = [i for i in "A B C D E F G H I J K L M N O P R S T".split(" ")]
#
# def gen():
#     j = f"{''.join(random.choices(alph, k=3))}{random.randint(111, 999)}"
#     return j if j not in done else gen()
cur.execute(f"select id from agents ")
# done = []
# for id in [i[0] for i in cur.fetchall()]:
#     m = gen()
#     print(m)
#     cur.execute(f'update agents set matrr = "{m}" where id = {id}')
#     cnx.commit()


pics = ["https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg", "https://images.pexels.com/photos/2078265/pexels-photo-2078265.jpeg",
            "https://images.pexels.com/photos/6962024/pexels-photo-6962024.jpeg",
            "https://images.pexels.com/photos/7148620/pexels-photo-7148620.jpeg",
            "https://images.pexels.com/photos/6214874/pexels-photo-6214874.jpeg",
            "https://images.pexels.com/photos/7013617/pexels-photo-7013617.jpeg",
            "https://images.pexels.com/photos/4924538/pexels-photo-4924538.jpeg",
            "https://images.pexels.com/photos/6962008/pexels-photo-6962008.jpeg",
            "https://images.pexels.com/photos/5032023/pexels-photo-5032023.jpeg",
            "https://images.pexels.com/photos/7654096/pexels-photo-7654096.jpeg",
            "https://images.pexels.com/photos/6195663/pexels-photo-6195663.jpeg",]

for i in [i[0] for i in cur.fetchall()]:
    cur.execute(f'''update agents set pic = "{random.choice(pics)}" where id = {i}''')
    cnx.commit()

cnx.close()