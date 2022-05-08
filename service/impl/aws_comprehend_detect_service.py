import json

from service.language_detect_service import LanguageDetectService
import boto3

aws_service = 'comprehend'
aws_region_name = 'eu-central-1'

class AWSComprehendDetectService(LanguageDetectService):

    @staticmethod
    def detect(data: str) -> str:

        comprehend = boto3.client(
            aws_access_key_id='AKIAUCYMDOCRXMRNIOPV',
            aws_secret_access_key='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',
            service_name=aws_service,
            region_name=aws_region_name)

        result = json.dumps(comprehend.detect_dominant_language(Text = data))
        return result['Languages']['LanguageCode']