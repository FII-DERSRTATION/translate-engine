from service.impl.aws_comprehend_detect_service import AWSComprehendDetectService
from service.impl.aws_ntm_translate_service import AWSNTMTranslateService

if __name__ == "__main__":
    frm = AWSComprehendDetectService.detect("Status nach Fraktur am Knie vor vielen Jahren")
    print(AWSNTMTranslateService.translate("Status nach Fraktur am Knie vor vielen Jahren", frm, 'en'))