# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelView(APIView):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]  # Apply IsAuthenticated permission

    def get(self, request):
        data = YourModel.objects.all()
        serializer = YourModelSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py



from django.http import Http404
class YourDetailView(APIView):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
        all_blogs = YourModel.objects.get(pk=pk)
        serializer = YourModelSerializer(all_blogs)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put (self, request, pk):
        blog =YourModel.objects.get(pk=pk)
        serializer = YourModelSerializer (blog, data=request.data)
        if serializer.is_valid ():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = YourModelSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_object(self, pk):
        try:
            return YourModel.objects.get(pk=pk)
        except YourModel.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        blog = YourModel.objects.get(pk=pk)
        blog.delete()
        return Response (status=status.HTTP_200_OK)


#
# class PersonAPI(APIView):
#
#     def get(self,request):
#         obj = Person.objects.all()
#         serializer =peopleSerializer(obj, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         data = request.data
#         serializer = peopleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     def put(self,request):
#         data = request.data
#         serializer = peopleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     def patch(self,request):
#         data = request.data
#         obj = Person.objects.get(id=data['id'])
#         serializer = peopleSerializer(obj, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
