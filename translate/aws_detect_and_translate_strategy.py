from service.impl.aws_comprehend_detect_service import AWSComprehendDetectService
from service.impl.aws_ntm_translate_service import AWSNTMTranslateService
from translate.translate_startegy import TranslateStrategy


class AWSDetectAndTranslateStrategy(TranslateStrategy):

    def __init__(self):
        pass

    def translate(self, target: str, lang: str) -> str:
        frm_lang_code = AWSComprehendDetectService.detect(target)
        if frm_lang_code != 'de' and frm_lang_code != 'fr':
            frm_lang_code = 'de'
        translated_text = AWSNTMTranslateService.translate(target, frm_lang_code, lang)

        return translated_text
