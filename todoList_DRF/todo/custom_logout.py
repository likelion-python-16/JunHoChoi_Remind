from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


#로그인  -> 제공해주는 형식 링크 DRF 제공 링크
#LogoutAPI -> 서버에 로그아웃 요청
#장고기본지원 -> 웹
#axios 방식 ->리액트 뷰, 언리얼엔진 , 유니티


class CustomLogoutAPI(APIView):
    permission_classes = [AllowAny]
    """
    - GET: Django 템플릿용 (redirect)
    - POST: API 호출용 (axios 등)
    """
    def get(self, request):
        logout(request)
        return redirect(reverse('todo:todo_List'))

    # def post(self, request):
    #     logout(request)
    #     return Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)