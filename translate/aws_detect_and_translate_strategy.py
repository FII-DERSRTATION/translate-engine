from service.impl.aws_comprehend_detect_service import AWSComprehendDetectService
from service.impl.aws_ntm_translate_service import AWSNTMTranslateService
from translate.translate_startegy import TranslateStrategy


class AWSDetectAndTranslateStrategy(TranslateStrategy):

    @staticmethod
    def translate(target: str, lang: str) -> str:
        frm_lang_code = AWSComprehendDetectService.detect(target)
        translated_text = AWSNTMTranslateService.translate(target, frm_lang_code, lang)

        return translated_text
