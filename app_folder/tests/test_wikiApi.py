from unittest import result
import requests

from ..PapyRobot.WikipediaApi import ApiWikiMedia

apiWiki = ApiWikiMedia("Lyon")


def test_WikiApi(monkeypatch):
    results = { 'batchcomplete': '',
  'query': { 'pages': { '802627': { 'extract': 'Lyon (prononcé /ljɔ̃/ ou /liɔ̃/ ) est une commune française située dans le quart '
                                               'sud-est de la France, au '
                                               'confluent du Rhône et de la '
                                               'Saône. Siège du conseil de la '
                                               'métropole de Lyon, à laquelle '
                                               'son statut particulier confère '
                                               'à la fois les attributions '
                                               "d'une métropole et d'un "
                                               'département, elle est aussi le '
                                               "chef-lieu de l'arrondissement "
                                               'de Lyon, celui de la '
                                               'circonscription départementale '
                                               'du Rhône et celui de la région '
                                               'Auvergne-Rhône-Alpes. Ses '
                                               'habitants sont appelés les '
                                               'Lyonnais.\n'
                                               'La commune a une situation de '
                                               'carrefour géographique du '
                                               'pays, au nord du couloir '
                                               'rhodanien qui court de Lyon à '
                                               'Marseille. Située entre le '
                                               "Massif central à l'ouest et le "
                                               "massif alpin à l'est, la ville "
                                               'de Lyon occupe une position '
                                               'stratégique dans la '
                                               'circulation nord-sud en '
                                               'Europe. Ancienne capitale des '
                                               "Gaules du temps de l'Empire "
                                               "romain, elle est le siège d'un "
                                               'archevêché dont le titulaire '
                                               'porte le titre de primat des '
                                               'Gaules. Lyon devint une ville '
                                               'très commerçante et une place '
                                               'financière de premier ordre à '
                                               'la Renaissance. Sa prospérité '
                                               'économique est portée aussi à '
                                               'cette époque par la soierie et '
                                               "l'imprimerie puis par "
                                               "l'apparition des industries "
                                               'notamment textiles, chimiques '
                                               'et, plus récemment, par '
                                               "l'industrie de l'image.\n"
                                               'Lyon, historiquement ville '
                                               'industrielle, a accueilli au '
                                               'sud de la ville de nombreuses '
                                               'activités pétrochimiques le '
                                               'long du Rhône, dans ce que '
                                               "l'on nomme le couloir de la "
                                               'chimie. Après le départ et la '
                                               'fermeture des industries '
                                               "textiles, elle s'est "
                                               'progressivement recentrée sur '
                                               "les secteurs d'activité de "
                                               'techniques de pointe, telles '
                                               'que la pharmacie et les '
                                               "biotechnologies. C'est "
                                               'également la deuxième ville '
                                               'étudiante de France, avec '
                                               'quatre universités et '
                                               'plusieurs grandes écoles. '
                                               'Enfin, la ville a conservé un '
                                               'patrimoine architectural '
                                               "important allant de l'époque "
                                               'romaine au XXe siècle en '
                                               'passant par la Renaissance et, '
                                               'à ce titre, les quartiers du '
                                               'Vieux Lyon, de la colline de '
                                               "Fourvière, de la Presqu'île et "
                                               'des pentes de la Croix-Rousse '
                                               'sont inscrits sur la liste du '
                                               'patrimoine mondial de '
                                               "l'UNESCO.\n"
                                               'En 2022, Lyon constitue, par '
                                               'sa population, la troisième '
                                               'commune de France avec 522 969 '
                                               'habitants, la ville-centre de '
                                               'la deuxième unité urbaine avec '
                                               '1 735 494 habitants et de la '
                                               "deuxième aire d'attraction de "
                                               'France avec 2 280 845 '
                                               'habitants. Elle est la '
                                               'préfecture du département du '
                                               'Rhône, de la région '
                                               'Auvergne-Rhône-Alpes, de la '
                                               'zone de défense et de sécurité '
                                               'Sud-Est et le siège de la '
                                               'métropole de Lyon, qui '
                                               'rassemble 59 communes et 1 411 '
                                               '571 habitants en 2019. La '
                                               'ville exerce une attractivité '
                                               "d'importance nationale et "
                                               'européenne. Son importance '
                                               'dans les domaines culturels, '
                                               'bancaires, financiers, '
                                               'commerciaux, technologiques, '
                                               'pharmaceutiques, ou encore les '
                                               'arts et les divertissements '
                                               'font de celle-ci une ville '
                                               'mondiale de rang « Beta- » '
                                               'selon le classement GaWC en '
                                               '2020, comparable à Osaka, '
                                               'Saint-Pétersbourg ou '
                                               'Stuttgart. La ville abrite  '
                                               'également le siège du Centre '
                                               'international de recherche sur '
                                               'le cancer depuis 1965 et celui '
                                               "d'Interpol depuis 1989.\n"
                                               '\n',
                                    'ns': 0,
                                    'pageid': 802627,
                                    'title': 'Lyon'}}}}

    pageid = str(results["query"]["pages"])
    pageid = pageid.split("{")[1][1:-3]
    datas = str(results["query"]["pages"][pageid]["extract"])
    final_info = str(datas.split(".")[0:2])[2:-2]

    def mockWikipediaApi():
        return results

    monkeypatch.setattr(requests, 'get', mockWikipediaApi)

    assert apiWiki.history == final_info
    assert apiWiki.keyWord == 'Lyon'
