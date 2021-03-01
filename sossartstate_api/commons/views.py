
"""Serializers for the File"""
from .commons_func import CommonsFunctions
from .bibliometric_func import AnalizerBibliometric
from .semantic_module import AnalizerSemantic
from file.models import File
from file.serializers import FileSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

from customuser.models import CustomUser
from customuser.serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token


class ProcessBibtexView(APIView):
    """This View, return the grouped meta-data before it's extract and agrupate."""
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        """keept the data file"""
        try:
            # implements the operative classes.
            cf = CommonsFunctions()
            ab = AnalizerBibliometric()

            # get the object reference and set the path the file.
            list_bibtext = request.data.get("idFiles")
            list_dictionarys = []
            for identifier in list_bibtext:
                obj = File.objects.get(id=identifier)
                list_dictionarys.append(
                    cf.convertBibtextToListDictionary(obj.file.path))
                ab.extractRelevantData(list_dictionarys)

            # keept and agroup the relevant information.
            ab.getRelevantData()
            return JsonResponse({"status": status.HTTP_200_OK,
                                 "data":  ab.getRelevantData()})
        except:
            return JsonResponse({"status": status.HTTP_400_BAD_REQUEST})


class sendSearchRefactorized(APIView):
    """This View, return the grouped meta-data before it's extract and agrupate."""
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        """keept the data file"""
        try:
            return JsonResponse({"status": status.HTTP_200_OK})
        except:
            return JsonResponse({"status": status.HTTP_400_BAD_REQUEST})


"""para responder los usuarios en el login"""


class Log_in_Custom(APIView):
    """Class Login to manage the log acces in the plattform"""

    def post(self, request):
        """recive a document_id and password and return the basic info and the token access"""
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        """si el se reciben bien los parametros busca el usuario"""
        if email and password:
            user_querysets = CustomUser.objects.get(email__iexact=email)
            """Si lo encuentra y esta activo elimna los campos sencibiles y crea el token"""
            if (user_querysets.is_active):
                user = user_querysets
                """valida que la contraseña propocionada sea correcta"""
                print(check_password(password, user.password))
                if(check_password(password, user.password)):
                    """Si la contraseña es correcta trae el usuario"""
                    user_token = CustomUser.objects.get(
                        email__iexact=email)
                    """creamos el token de acceso ..."""
                    token, created = Token.objects.get_or_create(
                        user=user_token)
                    """revisa el perfil del usuario"""
                    objserializer = UserSerializer(user_token).data
                    """Identifica el plan del tenant"""
                    return Response({"message": "Login exitoso",
                                     "data":  {
                                         "token": token.key,
                                         "user_data": objserializer
                                     }})
                else:
                    message = "Contraseña incorrecta"
                    return Response({"message": message, 'data': {}},
                                    status=status.HTTP_204_NO_CONTENT)
            else:
                message = "El id proporcionado no existe o el usuario no está activo"
                return Response({"message": message, 'data': {}},
                                status=status.HTTP_204_NO_CONTENT)
        else:
            message = "No ha proporciando datos validos"
            return Response({"message": message, 'data': {}},
                            status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class Log_out(APIView):
    """Class Logout to manage the log acces in the plattform"""

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
