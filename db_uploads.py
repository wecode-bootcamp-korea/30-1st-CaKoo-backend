import os, django, csv 	# os, django, csv를 사용하기 위함

from pathlib import Path # 경로를 객체로써 조작, 처리합니다.

BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)
# Path(__file__)은 현재 파일의 구상 경로를 인스턴스화하고 resolve() 메서드를 통해 절대경로를 반환
# 부모 경로로 2번 옮겨가면 django 프로젝트가 생성된 위치가 BASE_DIR 변수로 인스턴스화 된 것을 의미

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# 프로젝트에 등록되어있지 않은 파일에서 장고 사용
django.setup()
# 장고 셋업

from products.models import Product, ProductSize, ProductImage, InformationImage	# class 임포트
# CSV_PATH_USERS = 'product.csv'		# 파일 경로 지정

# with open(CSV_PATH_USERS) as in_file:	# csv 파일 오픈
#     data_reader = csv.reader(in_file)	# reader로 지정해 시퀀스 읽기, reader객체 반환
#     next(data_reader, None)		        # 첫줄 띄우기(필드값)
#     for row in data_reader:
#         Product.objects.create(
#             name          = row[0], 		# 필드의 0번 row값 넣기
#             description   = row[1],		    # 필드의 1번 row값 넣기
#             thumbnail     = row[2],			# 필드의 2번 row값 넣기
#             discount_rate = 0.8
#         )
# CSV_PATH_USERS = 'product_size.csv'		# 파일 경로 지정

# with open(CSV_PATH_USERS) as in_file:	# csv 파일 오픈
#     data_reader = csv.reader(in_file)	# reader로 지정해 시퀀스 읽기, reader객체 반환
#     next(data_reader, None)		        # 첫줄 띄우기(필드값)
#     for row in data_reader:
#         ProductSize.objects.create(
#             price   = row[0], 		# 필드의 0번 row값 넣기
#             product_id = row[1],		    # 필드의 1번 row값 넣기
#             size_id    = row[2],			# 필드의 2번 row값 넣기
            
#         )

# CSV_PATH_USERS = 'product_image.csv'		# 파일 경로 지정

# products = Product.objects.all()

# with open(CSV_PATH_USERS) as in_file:	# csv 파일 오픈
#     data_reader = csv.reader(in_file)	# reader로 지정해 시퀀스 읽기, reader객체 반환
#     next(data_reader, None)		        # 첫줄 띄우기(필드값)
    
#     # for product in products[1:]:
#     #     ProductImage.objects.create(
#     #             sequence = 1,
#     #             url = product.thumbnail,
#     #             product = product
#     #         )
        
#     for row in data_reader:
            
#         ProductImage.objects.create(
#             sequence   = row[0],            # 필드의 0번 row값 넣기
#             url        = row[1],		            # 필드의 1번 row값 넣기
#             product_id = row[2],			# 필드의 2번 row값 넣기   
#         )

CSV_PATH_USERS = 'information_image.csv'		# 파일 경로 지정

with open(CSV_PATH_USERS) as in_file:	# csv 파일 오픈
    data_reader = csv.reader(in_file)	# reader로 지정해 시퀀스 읽기, reader객체 반환
    next(data_reader, None)		        # 첫줄 띄우기(필드값)
    
    # for product in products[1:]:
    #     ProductImage.objects.create(
    #             sequence = 1,
    #             url = product.thumbnail,
    #             product = product
    #         )
    for row in data_reader:
            InformationImage.objects.create(
                sequence   = row[0],            # 필드의 0번 row값 넣기
                url        = row[1],		            # 필드의 1번 row값 넣기
                product_id = row[2],			# 필드의 2번 row값 넣기   
            )