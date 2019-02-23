from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView

from annotator.serializers import (
	AnnotationsListSerializer,
	AnnotationsCreateSerializer,
	AnnotationsUpdateSerializer,
	AnnotationsRetrieveSerializer
)

from annotator.models import Annotations

def annotate(request):
	return render(request,"index.html",{})

class AnnotationsList(ListAPIView):
    queryset = Annotations.objects.all()
    serializer_class = AnnotationsListSerializer



class AnnotationsCreate(CreateAPIView):
    queryset = Annotations.objects.all()
    serializer_class = AnnotationsCreateSerializer




class AnnotationsUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Annotations.objects.all()
    serializer_class = AnnotationsUpdateSerializer




class AnnotationsRetrieve(RetrieveAPIView):
    queryset = Annotations.objects.all()
    serializer_class = AnnotationsRetrieveSerializer