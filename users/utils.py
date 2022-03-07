import jwt

from django.http        import JsonResponse
from .models            import User
from config.settings    import SECRET_KEY, ALGORITHM

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            if 'Authorization' not in request.headers:
                return JsonResponse({"message" : "NO AUTHORIZATION IN HEADER"}, status = 401)
            
            access_token = request.headers.get('Authorization')           
            payload      = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            user_id      = payload['user_id']
         
            if not User.objects.filter(id = user_id).exists():
                return JsonResponse({"message" : "INVALID_UESR"}, status = 401)

            request.user = User.objects.get(id = user_id)

            return func(self, request, *args, **kwargs)
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

    return wrapper