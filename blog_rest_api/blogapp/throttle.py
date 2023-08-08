from rest_framework.throttling import UserRateThrottle


class CategoryListCreateViewThrottle(UserRateThrottle):
    scope = "blog-list"