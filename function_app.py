import azure.functions as func
from azure.functions.decorators.http import HttpMethod
import logging
import os
import json
from dotenv import load_dotenv


load_dotenv()
cognitiveSearchQueryKey : str = os.getenv('cognitiveSearchQueryKey')

app = func.FunctionApp()
@app.route(route="HttpExample", auth_level=func.AuthLevel.ADMIN, methods=[HttpMethod.GET])
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    responseHeaders : dict[str, str] = {"Access-Control-Allow-Origin": "*"}
    
    return func.HttpResponse(json.dumps({"key": f"{cognitiveSearchQueryKey}"}, ensure_ascii=False),
                             mimetype="application/json",
                             charset="utf-8",
                             headers=responseHeaders)
