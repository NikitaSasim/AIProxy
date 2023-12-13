from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import openai
import fastjsonschema
from .utils import get_gpt_response, get_giga_response, validate_message


class GptApiView(APIView):

    def post(self, request):

        try:
            message = json.loads(request.body)
        except Exception as e:
            return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            validate_message(message, 'gpt')
        except fastjsonschema.JsonSchemaException as e:
            return Response(f"Data failed validation: {e}", status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            answer = get_gpt_response(message)
            return Response(answer, status=status.HTTP_200_OK)
        except Exception as e:
            if type(e) is openai.BadRequestError or type(e) is json.decoder.JSONDecodeError:
                return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GigaApiView(APIView):

    def post(self, request):

        try:
            message = json.loads(request.body)
        except Exception as e:
            return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            validate_message(message, 'giga')
        except fastjsonschema.JsonSchemaException as e:
            return Response(f"Data failed validation: {e}", status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            answer = get_giga_response(message)
            return Response(answer, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
