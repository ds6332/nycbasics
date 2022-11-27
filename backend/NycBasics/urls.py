from django.urls import path, re_path
from .views import userviews, listviews, detailviews, ratingviews


urlpatterns = [
    re_path(
        r"^api/water/(?P<pk2>[\d\.\d]+)/(?P<pk1>[\d\.\d]+)/$",
        listviews.water_List.as_view(),
        name="waterlist",
    ),
    re_path(
        r"^api/wifi/(?P<pk2>[\d\.\d]+)/(?P<pk1>[\d\.\d]+)/$",
        listviews.wifi_List.as_view(),
        name="wifilist",
    ),
    re_path(
        r"^api/bench/(?P<pk2>[\d\.\d]+)/(?P<pk1>[\d\.\d]+)/$",
        listviews.bench_List.as_view(),
        name="benchlist",
    ),
    re_path(
        r"^api/toilet/(?P<pk2>[\d\.\d]+)/(?P<pk1>[\d\.\d]+)/$",
        listviews.toilet_List.as_view(),
        name="toiletlist",
    ),
    re_path(
        r"^api/parking/(?P<pk2>[\d\.\d]+)/(?P<pk1>[\d\.\d]+)/$",
        listviews.parking_List.as_view(),
        name="parkinglist",
    ),
    path(
        "api/water/<int:pk>/",
        detailviews.water_amenity_detail.as_view(),
        name="waterdetail",
    ),
    path(
        "api/wifi/<int:pk>/",
        detailviews.wifi_amenity_detail.as_view(),
        name="wifidetail",
    ),
    path(
        "api/bench/<int:pk>/",
        detailviews.bench_amenity_detail.as_view(),
        name="benchdetail",
    ),
    path(
        "api/toilet/<int:pk>/",
        detailviews.toilet_amenity_detail.as_view(),
        name="toiletdetail",
    ),
    path(
        "api/parking/<int:pk>/",
        detailviews.parking_amenity_detail.as_view(),
        name="parkingdetail",
    ),
    path("api/addUser/", userviews.Record.as_view(), name="register"),
    path("api/users/", userviews.Record.as_view(), name="viewusers"),
    path(
        "api/addUser_SendEmail/",
        userviews.Record_SendEmail.as_view(),
        name="register_SendEmail",
    ),
    path(
        "api/login/",
        userviews.Login.as_view(),
        name="login",
    ),
    path("api/logout/", userviews.Logout.as_view(), name="logout"),
    path(
        "api/rating_review/<str:pk1>/<int:pk2>/",
        ratingviews.rating_List.as_view(),
        name="ratingdetail",
    ),
    path(
        "api/allreviews/",
        ratingviews.all_ratings.as_view(),
        name="allreviews",
    ),
    path(
        "api/review/<int:pk>/",
        ratingviews.all_ratings.as_view(),
        name="ratingdetailall",
    ),
    path(
        "api/create_rating/",
        ratingviews.create_Rating.as_view(),
        name="createrating",
    ),
    path(
        "api/verification/<str:pk1>/<int:pk2>/",
        userviews.Email_Verification.as_view(),
        name="emailverification",
    ),
    path(
        "api/reset_password/<str:pk1>/<int:pk2>/",
        userviews.Reset_Password.as_view(),
        name="reset_password",
    ),
    path(
        "api/reset_password_SendEmail/",
        userviews.Reset_Password_SendEmail.as_view(),
        name="reset_password_SendEmail",
    ),
    path(
        "api/reset_password_verification/<str:pk1>/<int:pk2>/<str:pk3>",
        userviews.Reset_Password_Verification.as_view(),
        name="reset_password_verification",
    ),
]
