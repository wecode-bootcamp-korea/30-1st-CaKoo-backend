import json, bcrypt, jwt

from django.http      import JsonResponse
from django.views     import View
from users.models     import User
from users.validators import validate_email, validate_password
from config.settings  import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name         = data['name'],
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            birthdate    = data["birthdate"]

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if not validate_email(email):
                return JsonResponse({'message' : 'Invalid Email!'}, status = 400)
            
            if not validate_password(password):
                return JsonResponse({'message' : 'Invalid Password!'}, status = 400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'Email Already Exists!'}, status = 400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = hashed_password,
                phone_number = phone_number,
                birthdate    = birthdate
                
            )
            return JsonResponse({"message": "User Created!"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class SignInView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            signin_email    = data['email']
            signin_password = data['password']

            if not User.objects.filter(email = signin_email).exists():
                return JsonResponse({"message" : "INVALID_UESR"}, status = 401)

            user         = User.objects.get(email = signin_email)
            access_token = jwt.encode({'user_id' : user.id}, SECRET_KEY, ALGORITHM)
            
            if not bcrypt.checkpw(signin_password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message" : "WRONG PASSWORD"}, status = 401)

            return JsonResponse({"message" : "SUCCESS", "access_token" : access_token}, status = 200)
            
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)