from rest_framework import serializers
from apps.subjects.models import Subject
from django.template.defaultfilters import slugify



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['name'])
        if Subject.objects.filter(slug=validated_data['slug']).exists():
            raise serializers.ValidationError('This slug already exists')
        return super().create(validated_data)


{
    "name": "Backend",
    "desc":"Vashe zo'r kurs",
    "price":"1500000"
}