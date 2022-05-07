# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import re

from connector import connect_to_kis_db, fetch_jsons


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import boto3

    comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')


    con = connect_to_kis_db()
    entries = fetch_jsons(con)
    con.close()

    for entry in entries:
        data = json.loads(re.sub(r"[\n\t\s]*", "", entry[0].decode("utf-8")))
        print(30 * "=")
        print(data.keys())
        # print(data['Bericht']['Status']['Inhalt'])
        print(30 * "=")


        # print('Calling DetectDominantLanguage')
        # print(json.dumps(comprehend.detect_dominant_language(Text=data['Inhalt']), sort_keys=True, indent=4))
        # print("End of DetectDominantLanguage\n")


    # comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')
    # print('Calling DetectDominantLanguage')
    # print(json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True, indent=4))
    # print("End of DetectDominantLanguage\n")
    #
    #
    # translate = boto3.client(service_name='translate', region_name='eu-central-1', use_ssl=True)
    #
    # result = translate.translate_text(Text="Hello, World",
    #                                   SourceLanguageCode="en", TargetLanguageCode="de")
    #
    # print('TranslatedText: ' + result.get('TranslatedText'))
    # print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
    # print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
