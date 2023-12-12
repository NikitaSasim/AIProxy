import os
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from dotenv import load_dotenv
import json
import openai
from .utils import get_gpt_response

load_dotenv()


class GptApiView(APIView):

    def post(self, request):

        try:
            answer = get_gpt_response(json.loads(request.body))

            return Response(answer, status=status.HTTP_200_OK)

        except Exception as e:

            if type(e) is openai.BadRequestError or type(e) is json.decoder.JSONDecodeError:

                return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            else:

                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
