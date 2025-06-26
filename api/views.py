from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import openai 
from django.conf import settings
import logging


logger = logging.getLogger(__name__)




def iachat(texto):
        
        openai.api_key = settings.APITOKEN  # Asegúrate de que APITOKEN esté configurado en settings.py'
        
        response = openai.responses.create(
            model="gpt-4.1-nano",
            prompt={
                "id": "id_prompt",
                "version": "1"
            },
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                "type": "input_text",
                "text": f"{texto}"
                }
            ]
            }
            
        ],
        reasoning={},
        max_output_tokens=2048)

        return response.output_text if response.output_text else "No response from IA"
    


 

# Create your views here.
class ChatbotView(APIView):
    
    def get(self, request):
        print("ChatbotView GET request received")
        return Response("ChatbotView GET response")

    def post(self, request):
        logger.info("📥 ChatbotView POST request received")
    
       
    
        
        """
           Si se quiere manejar un endpoint se puede hacer el manejo
           desde este post si se quiere hacer desde el admin que seria lo mas 
           optimo, puedes hacer una funcion para cargar el excel y convertirlo 
           a JSON
        """
        
        """
        Aqui enviar las respuesta del JSON a la IA recuerda hacer un .env con la key 
        de openIA
        """
        response= iachat('mensaje de prueba')
        
        
        return Response({"response": response})