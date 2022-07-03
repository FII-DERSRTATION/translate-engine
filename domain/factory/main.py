import json


if __name__ == "__main__":
    a = json.loads('{ 	"Diagnosen": { 		"Titel": "Diagnosen", 		"Diagnosen": { 			"List": [ 				{ 					"Titel": "1. Unklare Unterbauchschmerzen", 					"Inhalt": "- DD: Gastroenteritis, Appendizitis, Adnexitis", 					"Hauptdiagnose": "1", 					"Nebendiagnose": "0", 					"Behandlungsrelevant": "1" 				}, 				{ 					"Titel": "2. Polyarthritis", 					"Inhalt": "- Unter Immunsuppression", 					"Hauptdiagnose": "1", 					"Nebendiagnose": "0", 					"Behandlungsrelevant": "1" 				} 			] 		} 	} }')
    for e in a['Diagnosen']['Diagnosen']['List']:
        print(e['Titel'])

        if "Inhalt" in e.keys():
            print("===>" + e['Inhalt'])