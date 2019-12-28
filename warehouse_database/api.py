from rest_framework import routers
from warehouse_db import api_views as myapp_views
from users import views as my_views

router = routers.DefaultRouter()
router.register(r'users', my_views.UserListView)
router.register(r'product', myapp_views.ProductViewset)
router.register(r'stock', myapp_views.Stock_On_HandViewset)