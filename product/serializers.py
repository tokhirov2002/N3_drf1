from rest_framework import serializers

from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


#  {
#     "id": 2,
#     "title": "Noutbook555",
#     "description": "juda yaxshi garatiya 2 uil garantiya yuq",
#     "images": "http://127.0.0.1:8000/media/produc_images/Book_1X4uBdU.png",
#     "price": 3000000,
#     "created_at": "2025-07-11T04:32:56.729074Z"
#   },
#   {
#     "id": 3,
#     "title": "sedwfrgrg",
#     "description": "gregregreg",
#     "images": "http://127.0.0.1:8000/media/produc_images/About_YOTOHde.png",
#     "price": 6526,
#     "created_at": "2025-07-11T04:33:58.458931Z"
#   }

