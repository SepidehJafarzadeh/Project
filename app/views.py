from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Product, Category, Feature, ProductFeature, Comment, Image
from django.http import Http404
from .serializers import ProductSerialiser,UserSerialiser, CategorySerialiser, FeatureSerialiser, ProductFeatureSerialiser, CommentSerialiser, ImageSerialiser
from rest_framework.response import Response
from app.models import User

# Create your views here.
class ProductView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except  Product.DoesNotExist :
            raise Http404
        
    def get(self, request, pk, format=None):
        Product = self.get_object(pk)
        try:
            serializer = ProductSerialiser(Product)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        Product = self.get_object(pk)
        serializer = ProductSerialiser(Product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Product = self.get_object(pk)
        Product.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def post(self, request,pk, format=None):
        serializer = ProductSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    




class CategoryView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except  Category.DoesNotExist :
            raise Http404
        
    def get(self, request, pk, format=None):
        Category = self.get_object(pk)
        try:
            serializer = CategorySerialiser(Category)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        Category = self.get_object(pk)
        serializer = CategorySerialiser(Category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Category = self.get_object(pk)
        Category.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def post(self, request,pk, format=None):
        serializer = CategorySerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class ProductFeatureView(APIView):
    def get_object(self, pk):
        try:
            return ProductFeature.objects.get(pk=pk)
        except  ProductFeature.DoesNotExist :
            raise Http404
        
    def get(self, request, pk, format=None):
        ProductFeature = self.get_object(pk)
        try:
            serializer = ProductFeatureSerialiser(ProductFeature)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        ProductFeature = self.get_object(pk)
        serializer = ProductFeatureSerialiser(ProductFeature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        ProductFeature = self.get_object(pk)
        ProductFeature.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def post(self, request,pk, format=None):
        serializer = ProductFeatureSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class FeatureView(APIView):
    def get_object(self, pk):
        try:
            return Feature.objects.get(pk=pk)
        except  Feature.DoesNotExist :
            raise Http404
        
    def get(self, request, pk, format=None):
        Feature = self.get_object(pk)
        try:
            serializer = FeatureSerialiser(Feature)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        Feature = self.get_object(pk)
        serializer = FeatureSerialiser(Feature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Feature = self.get_object(pk)
        Feature.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def post(self, request,pk, format=None):
        serializer = FeatureSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    




class CommentView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except  Comment.DoesNotExist :
            raise Http404
        
    def get(self, request, pk, format=None):
        Comment = self.get_object(pk)
        try:
            serializer = CommentSerialiser(Comment)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        Comment = self.get_object(pk)
        serializer = CommentSerialiser(Comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Comment = self.get_object(pk)
        Comment.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def post(self, request,pk, format=None):
        serializer = CommentSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ImageView(APIView):
    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except  Image.DoesNotExist :
            raise Http404
        
    def get(self, request, pk, format=None):
        Image = self.get_object(pk)
        try:
            serializer = ImageSerialiser(Image)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        Image = self.get_object(pk)
        serializer = ImageSerialiser(Image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Image = self.get_object(pk)
        Image.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def post(self, request,pk, format=None):
        serializer = ImageSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    



class UserView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except  User.DoesNotExist :
            raise Http404
        
    def get(self, request, pk, format=None):
        User = self.get_object(pk)
        try:
            serializer = UserSerialiser(User)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        User = self.get_object(pk)
        serializer = UserSerialiser(Product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        User = self.get_object(pk)
        User.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def post(self, request,pk, format=None):
        serializer = UserSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


    




