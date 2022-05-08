import boto3

from service.language_translate_service import LanguageTranslateService

aws_service = 'translate'
aws_region_name = 'eu-central-1'


class AWSNTMTranslateService(LanguageTranslateService):

    @staticmethod
    def translate(data: str, frm: str, to: str) -> str:
        translate = boto3.client(
            aws_access_key_id='AKIAUCYMDOCRXMRNIOPV',
            aws_secret_access_key='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',
            service_name=aws_service,
            region_name=aws_region_name)

        return translate.translate_text(Text=data, SourceLanguageCode=frm, TargetLanguageCode=to)['TranslatedText']
