from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, parser_classes
# from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ValidationError
from .serializers import FileSerializer
from .models import File
import logging

# Set up logging
logger = logging.getLogger(__name__)

class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class to handle large datasets
    - page_size: Number of items per page
    - page_size_query_param: Allows client to override page size via query parameter
    - max_page_size: Maximum limit to prevent performance issues
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Ensures only authenticated users can access
def file_list(request):
    """
    List all files with pagination support
    
    GET parameters:
    - page: Page number
    - page_size: Number of items per page
    """
    try:
        # Get all files ordered by most recent first
        files = File.objects.all().order_by('-created_at')
        
        # Initialize paginator
        paginator = StandardResultsSetPagination()
        paginated_files = paginator.paginate_queryset(files, request)
        
        # Serialize the paginated queryset
        serializer = FileSerializer(paginated_files, many=True)
        
        # Return paginated response
        return paginator.get_paginated_response(serializer.data)
    
    except Exception as e:
        logger.error(f"Error in file_list view: {str(e)}")
        return JsonResponse(
            {'error': 'Failed to retrieve files'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
# @authentication_classes([])
@permission_classes([])
@parser_classes([MultiPartParser, FormParser])  # Required for handling file uploads
def file_upload(request):
    """
    Handle file upload with validation and error handling
    
    POST parameters:
    - file: The file to be uploaded
    """
    try:
        # Validate if file is present in request
        if 'file' not in request.FILES:
            return JsonResponse(
                {'error': 'No file provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES['file']
        
        # Validate file size (example: 5MB limit)
        if file.size > 5 * 1024 * 1024:
            return JsonResponse(
                {'error': 'File size exceeds 5MB limit'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validate file type (example: only allow certain extensions)
        allowed_extensions = ['.pdf', '.doc', '.docx', '.txt']
        # in python this is a list comprehension, it's a more concise way to write a for loop
        if not any(file.name.lower().endswith(ext) for ext in allowed_extensions):
            return JsonResponse(
                {'error': 'File type not allowed'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create file object with additional metadata
        file_obj = File.objects.create(
            file=file,
            filename=file.name,
            file_size=file.size,
            # uploaded_by=request.user  # Assuming User foreign key exists in model
        )

        # Serialize the created file object
        serializer = FileSerializer(file_obj)
        
        return JsonResponse(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    except ValidationError as e:
        logger.error(f"Validation error in file_upload: {str(e)}")
        return JsonResponse(
            {'error': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    except Exception as e:
        logger.error(f"Error in file_upload view: {str(e)}")
        return JsonResponse(
            {'error': 'Failed to upload file'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )