
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status


from .forms import SignUpForm


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    print("Signup called")
    data = request.data
    print("Data received:", data)
    
    message = "success"

    form = SignUpForm({
        'email': data.get('email'),
        'username': data.get('username'),
        'password1': data.get('password1'),
        'password2': data.get('password2')
    })

    if form.is_valid():
        form.save()
    else:
        message = "error"
        print("Form errors:", form.errors)  # Log form errors
        return JsonResponse({'status': message, 'errors': form.errors}, status=400)

    return JsonResponse({'status': message})

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
    })


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if email exists
        if not User.objects.filter(email=email).exists():
            return Response({'detail': 'Account with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Authenticate user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            return Response({'token': 'your-token-here'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Incorrect password.'}, status=status.HTTP_401_UNAUTHORIZED)


