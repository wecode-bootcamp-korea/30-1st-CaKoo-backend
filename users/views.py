import json, bcrypt

from django.http  import JsonResponse
from django.views import View

from users.models     import User
from users.validators import validate_email, validate_password


class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name         = data["name"],
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            birthdate    = data["birthdate"]

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if not validate_email(email):
                return JsonResponse({'Message' : 'Invalid Email!'}, status = 400)
            
            if not validate_password(password):
                return JsonResponse({'Message' : 'Invalid Password!'}, status = 400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'Message' : 'Email Already Exists!'}, status = 400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = hashed_password,
                phone_number = phone_number,
                birthdate    = birthdate
                
            )
            return JsonResponse({"MESSAGE": "User Created!"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
