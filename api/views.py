import os
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from dotenv import load_dotenv

load_dotenv()


class GptApiView(APIView):

    def post(self, request):

        if request.headers['Auth'] == self.api_key:

            dataset = get_dataset()

            try:
                for data in dataset:
                    send_all(data)
            except:
                print(dataset)


            return Response('', status=status.HTTP_201_CREATED)

        else:
            return Response('', status=status.HTTP_401_UNAUTHORIZED)