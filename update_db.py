# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Country, Club, base, User

engine = create_engine('sqlite:///clubs.db')
base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

user1 = User(name='Hazem Ahmed', email='hazeem.egy@gmail.com',)
session.add(user1)
session.commit()

'#England'
country1 = Country(name='England', img_url='https://images3.alphacoders.com/743/74305.jpg')
session.add(country1)
session.commit()

club1 = Club(name='Liverpool', description="Liverpool Football Club is a\
 professional football club in Liverpool, England, that competes in the\
 Premier League, the top tier of English football. The club has won six\
 European Cups, more than any other English club, three UEFA Cups and four\
 UEFA Super Cups, also English records, eighteen League titles, seven FA Cups\
 a record eight League Cups and fifteen FA Community Shields.",
 img_url = 'https://pluspng.com/img-png/logo-liverpool-fc-png-liverpool-fc-logo-500.png',
              country=country1, user_id=1)
session.add(club1)
session.commit()

club2 = Club(name='Manchester City', description="Manchester City Football\
 Club is\
 an English football club based in Manchester, that competes in the Premier\
 League, the top flight of English football. The club have won six domestic\
 league titles. Under the management of Pep Guardiola they won the Premier\
 League in 2018 becoming the only Premier League team to attain 100 points in\
 a single season. In 2019, they won four trophies, completing an unprecedented\
 sweep of all domestic trophies in England and becoming the first English \
 men's team to win the domestic treble.",
 img_url = 'https://upload.wikimedia.org/wikipedia/ar/thumb/e/eb/Manchester_City_FC_badge.svg/1200px-Manchester_City_FC_badge.svg.png',
             country=country1, user_id=1)
session.add(club2)
session.commit()

club3 = Club(name='Chelsea', description="Chelsea Football Club are an English\
 professional football club based in Fulham, London. Founded in 1905, they\
 compete in the Premier League, the top division of English football. Chelsea\
 are among England's most successful clubs; they have been league champions\
 six\
 times and won over thirty competitive honours, including six European\
 trophies.\
 Their home ground is Stamford Bridge.",
             country=country1, user_id=1)
session.add(club3)
session.commit()

club4 = Club(name='Manchester United', description="Manchester United\
 Football Club is a\
 professional football club based in Old Trafford, Greater Manchester,\
 England, that\
 competes in the Premier League, the top flight of English football.\
 Nicknamed 'the\
 Red Devils'.Manchester United have won more trophies than any other\
 club in English\
 football, with a record 20 League titles, 12 FA Cups, five League Cups\
 and a record\
 21 FA Community Shields. United have also won three UEFA Champions\
 Leagues, one UEFA\
 Europa League, one UEFA Cup Winners' Cup, one UEFA Super Cup, one\
 Intercontinental Cup\
 and one FIFA Club World Cup",
 img_url = 'https://upload.wikimedia.org/wikipedia/ar/thumb/7/7a/Manchester_United_FC_crest.svg/1200px-Manchester_United_FC_crest.svg.png',
             country=country1, user_id=1)
session.add(club4)
session.commit()

club5 = Club(name='Arsenal', description="Arsenal Football Club is a\
 professional football\
 club based in Islington, London, England, that plays in the Premier\
 League, the top\
 flight of English football. The club has won 13 League titles, a record\
 13 FA Cups,\
 2 League Cups, 15 FA Community Shields, 1 League Centenary Trophy, 1 UEFA\
 Cup Winners'\
 Cup and 1 Inter-Cities Fairs Cup",
img_url = 'https://www.pngitem.com/pimgs/m/47-473677_transparent-arsenal-png-arsenal-fc-logo-png-png.png',
             country=country1, user_id=1)
session.add(club5)
session.commit()

'#Spain'
country2 = Country(name='Spain', img_url='https://wallpaperaccess.com/full/1099381.jpg')
session.add(country2)
session.commit()

club1 = Club(name='Real Madrid', description="Real Madrid, is a Spanish\
 professional football\
 club based in Madrid.the club has won 64 trophies; a record 33 La Liga\
 titles, 19 Copa\
 del Rey, 10 Supercopa de Espana, a Copa Eva Duarte, and a Copa de la Liga.\
 In European\
 and worldwide competitions, the club has won a record 26 trophies; a record\
 13 European\
 Cup/UEFA Champions League titles, two UEFA Cups and four UEFA Super Cups.\
 In international\
 football, they have achieved a record seven club world championships.",
 img_url = 'https://lh3.googleusercontent.com/proxy/kmKgQhj_d8iMzQr_W21Mft9tGTHPM9pox0zi3002Ea1OHgrpCPoQoxc1VHRWm-Ni6e9u1EdVYqZxOeO-VXnJjIH29x49Wv1TedSdxZjSeDFV1ochpA',
              country=country2, user_id=1)
session.add(club1)
session.commit()

club2 = Club(name='Barcelona', description="Founded in 1899 by a group\
 of Swiss, Spanish,\
 English, and Catalan footballers led by Joan Gamper. Barcelona has won\
 a record\
 74 trophies; 26 La Liga, 30 Copa del Rey, 13 Supercopa de Espana, 3\
 Copa Eva Duarte,\
 and 2 Copa de la Liga trophies, as well as being the record holder\
 for the latter\
 four competitions. In international club football, the club has won\
 20 European\
 and worldwide titles; 5 UEFA Champions League titles, a record 4 UEFA\
 Cup Winners'\
 Cup, a joint record 5 UEFA Super Cup, a record 3 Inter-Cities Fairs\
 Cup, and 3\
 FIFA Club World Cup.",
 img_url = 'https://upload.wikimedia.org/wikipedia/ar/thumb/0/03/Barcelona-logo.svg/1010px-Barcelona-logo.svg.png',
             country=country2, user_id=1)
session.add(club2)
session.commit()

club3 = Club(name='Atletico Madrid', description="A Spanish professional\
 football club based\
 in Madrid.In terms of league titles won, most recently in 2014,\
 Atletico Madrid are\
 the third most successful club in Spanish football behind Real\
 Madrid and Barcelona.\
 Atletico have won La Liga on 10 occasions, including a league and\
 cup double in 1996.\
 the Copa del Rey on 10 occasions, two Supercopas de Espana and one\
 Copa Eva Duarte,\
 in Europe, they won the European Cup Winners' Cup in 1962, were\
 runners-up in 1963\
 and 1986, were Champions League runners-up in 1974, 2014 and 2016,\
 won the Europa\
 League in 2010, 2012 and 2018, and won the UEFA Super Cup in 2010,\
 2012 and 2018\
 as well as the 1974 Intercontinental Cup.",
 img_url = 'https://worldsportlogos.com/wp-content/uploads/2018/01/atletico-madrid-logo.png',
              country=country2, user_id=1)
session.add(club3)
session.commit()

'#Germany'
country3 = Country(name='Germany', img_url='https://i.pinimg.com/originals/97/b1/6a/97b16a20eac054c88f23212f3287d6c5.jpg')
session.add(country3)
session.commit

club1 = Club(name='Bayern Munich', description="FC Bayern, is a German\
 sports club based in\
 Munich, Bavaria, and is the most successful club in German football\
 history, having\
 won a record 29 national titles and 19 national cups.Since the formation\
 of the Bundesliga,\
 Bayern has been the dominant club in German football, winning 29\
 titles, including seven\
 consecutively since 2013. They have traditional local rivalries\
 with 1860 Munich and 1.\
 FC Nurnberg, as well as with Borussia Dortmund since the mid 1990s",
 img_url = 'https://www.logofootball.net/wp-content/uploads/FC-Bayern-Munich-HD-Logo.png',
              country=country3, user_id=1)
session.add(club1)
session.commit()

club2 = Club(name='Borussia Dortmund', description="Dortmund, is a German\
 sports club based in Dortmund,\
 North Rhine-Westphalia. BVB the second largest sports club by membership\
 in Germany. Borussia\
 Dortmund have won eight German championships, four DFB-Pokals, six\
 DFL-Supercups, one UEFA\
 Champions League, one UEFA Cup Winners' Cup, and one Intercontinental Cup.\
 Their Cup Winners'\
 Cup win in 1966 made them the first German club to win a European title.",
 img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/1024px-Borussia_Dortmund_logo.svg.png',
              country=country3, user_id=1)
session.add(club2)
session.commit()

club3 = Club(name='FC Schalke 04', description="FC Schalke 04 is a\
 professional German football and\
 multi-sports club originally from the Schalke district of Gelsenkirchen,\
 North\
 Rhine-Westphalia.Founded in 1904, Schalke has won seven German\
 championships, five\
 DFB-Pokals, one DFL-Supercup and one UEFA Cup. Schalke also succeeded\
 as the first\
 German club to win a cup double in 1937.",
             country=country3, user_id=1)
session.add(club3)
session.commit()

'#Italy'
country4 = Country(name='Italy', img_url='https://wallpaperaccess.com/full/46396.jpg')
session.add(country4)
session.commit()

club1 = Club(name='Juventus', description="Juve  is an Italian professional\
 football\
 club based in Turin, Piedmont. Founded in 1897 by a group of Torinese\
 students.\
 Nicknamed Vecchia Signora ('the Old Lady'), the club has won 35 official\
 league\
 titles, 13 Coppa Italia titles and eight Supercoppa Italiana titles, being\
 the\
 record holder for all these competitions; two Intercontinental Cups, two\
 European Cups / UEFA Champions Leagues, one European Cup Winners' Cup, a\
 joint national record of three UEFA Cups, two UEFA Super Cups and a joint\
 national record of one UEFA Intertoto Cup.",
 img_url = 'https://worldsportlogos.com/wp-content/uploads/2018/01/Juventus-logo.png',
             country=country4, user_id=1)
session.add(club1)
session.commit()

club2 = Club(name='A.S. Roma', description="A.S. Roma is an Italian\
 professional football\
 club based in Rome. Founded by a merger in 1927. Roma have won Serie A\
 three times, in 1942, 1983 and 2001, as well as winning nine\
 Coppa Italia titles and two Supercoppa Italiana titles. In European\
 competitions, Roma won the Inter Cities Fairs Cup in 1961 and were\
 runners up in the 1984 European Cup and the 1991 UEFA Cup.",
              country=country4, user_id=1)
session.add(club2)
session.commit()

club3 = Club(name='A.C. Milan', description="Milan, is a professional\
 football club\
 in Milan, Italy, founded in 1899. Milan has won a joint record three\
 Intercontinental Cups and one FIFA Club World Cup, seven European\
 Cup/Champions League titles (Italian record), the UEFA Super Cup a joint\
 record five times and the Cup Winners' Cup twice. With 18 league titles,\
 Milan is also the joint-second most successful club in Serie A, along with\
 local rivals Internazionale and behind Juventus (35 league titles). They\
 have also won the Coppa Italia five times, and the Supercoppa Italiana\
 seven.",
 img_url = 'https://www.logofootball.net/wp-content/uploads/AC-Milan-HD-Logo.png',
   country=country4, user_id=1)
session.add(club3)
session.commit()

'#France'
country5 = Country(name='France', img_url='https://wallpaperaccess.com/full/397830.jpg')
session.add(country5)
session.commit()

club1 = Club(name='Paris Saint-Germain', description="PSG, is a French\
 professional\
 football club based in Paris. Founded in 1970.PSG have won a total of 40\
 titles, 39 of them considered major trophies, making it the most successful\
 French club in history by this measure. Paris SG is also the only club to\
 have never been relegated from Ligue 1, the club with most consecutive\
 seasons in the top-flight (they have played 45 seasons in Ligue 1 since\
 1974), one of only two French clubs to have won a major European title,\
 the most popular football club in France, and one of the most widely\
 supported teams in the world.",
 img_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Paris_Saint-Germain_F.C..svg/1200px-Paris_Saint-Germain_F.C..svg.png',
             country=country5, user_id=1)
session.add(club1)
session.commit()

club2 = Club(name='Olympique Lyonnais', description=" The club was formed\
 as Lyon\
 Olympique Universitaire in 1899,The club won its first Ligue 1 championship\
 in 2002, starting a national record setting streak of seven successive\
 titles. Lyon has also won eight Trophee des Champions, five Coupe de\
 France titles and three Ligue 2 titles.",
             country=country5, user_id=1)
session.add(club2)
session.commit()

club3 = Club(name='Olympique de Marseille', description=" Marseille, is a\
 French\
 football club in Marseille in France. Founded in 1899, the club play in\
 Ligue 1 and have spent most of their history in the top tier of French\
 football. The club has won ten official league titles (nine times in\
 Ligue 1), ten Coupes de France and three Coupes de la Ligue.",
              country=country5, user_id=1)
session.add(club3)
session.commit()

'#Netherlands'
country6 = Country(name='Netherlands', img_url='https://hdwallsource.com/img/2016/5/netherlands-flag-desktop-wallpaper-50694-52386-hd-wallpapers.jpg')
session.add(country6)
session.commit()

club1 = Club(name='AFC Ajax', description="Ajax, is a Dutch professional\
 football club based in Amsterdam, that plays in the Eredivisie.\
 Ajax has been the most successful club in the Netherlands, with 34\
 Eredivisie titles and 19 KNVB Cups.",
 img_url = 'https://www.logofootball.net/wp-content/uploads/AFC-Ajax-Logo.png',
             country=country6, user_id=1)
session.add(club1)
session.commit()

club2 = Club(name='PSV Eindhoven', description="PSV Eindhoven is a sports\
 club from Eindhoven, Netherlands, that plays in the Eredivisie,\
 The team has won the Eredivisie 24 times, the KNVB Cup nine times\
 and the Johan Cruyff Shield ten times. ",
             country=country6, user_id=1)
session.add(club2)
session.commit()

club3 = Club(name='Feyenoord', description="Feyenoord is a Dutch professional\
 football club in Rotterdam, that plays in the Eredivisie, Feyenoord\
 is one of the most successful clubs in Dutch football, winning 15\
 Eredivisie titles, 13 KNVB Cups, and 4 Johan Cruyff Shields.\
 Internationally, it has won one European Cup, two UEFA Cups,\
 and one Intercontinental Cup.",
             country=country6, user_id=1)
session.add(club3)
session.commit()

'#Brazil'
country7 = Country(name='Brazil', img_url='https://wallpaperaccess.com/full/118713.jpg')
session.add(country7)
session.commit()

club1 = Club(name='Clube de Regatas do Flamengo', description="Flamengo, is a\
 Brazilian sports club based in Rio de Janeiro and established in 1895.\
 They captured several Campeonato Carioca (Rio de Janeiro state league)\
 titles prior to the establishment of the first Brazilian national\
 football league in 1959. Since then, they have remained successful\
 in Brazilian football, having won 6 Campeonato Brasileiro Serie A,\
 3 Copa do Brasil, and a record 35 Campeonato Carioca ",
              country=country7, user_id=1)
session.add(club1)
session.commit()

club2 = Club(name='Santos FC', description="The club was founded in 1912\
 by the initiative of three sports enthusiasts from Santos. They\
 have won a total of 24 titles during that decade including five\
 consecutive Brasileiroes, a feat that remains unequaled today.\
 Os Santasticos won four competitions in 1962, thus completing a\
 quadruple, comprising the Paulistao, the Brasileirao, the Copa\
 Libertadores and the European/South American Cup.",
 img_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Santos_FC_logo.svg/1045px-Santos_FC_logo.svg.png',
              country=country7, user_id=1)
session.add(club2)
session.commit()

club3 = Club(name='Sociedade Esportiva Palmeiras', description="Palmeiras\
 is a Brazilian professional football club based in the city of Sao\
 Paulo and founded in 1914. Palmeiras have won 14 national\
 competitions, making it the most successful club inside Brazil.\
 The club's most important titles are the 1951 Copa Rio international\
 tournament, 1999 Copa Libertadores, 5 Brazilian National League\
 titles ",  country=country7, user_id=1)
session.add(club3)
session.commit()

'#Egypt'
country8 = Country(name='Egypt', img_url='https://wallpaperaccess.com/full/139859.jpg')
session.add(country8)
session.commit()

club1 = Club(name='Zamalek SC', description="Zamalek is an Egyptian sports\
 club based in Giza, Egypt and founded on 5 January 1911.Zamalek are\
 one of two clubs that have played in every season of the Egyptian\
 Premier League, and one of seven clubs that have never been\
 relegated to the Egyptian Second Division. On the continental side,\
 Zamalek has won five CAF Champions League titles,as follows one CAF\
 Confederation Cup title, three CAF Super Cup titles and one African\
 Cup Winners' Cup title; making themselves as one of the most\
 successful clubs in Africa.",
 img_url = 'https://upload.wikimedia.org/wikipedia/ar/0/04/ZamalekSC.png',
             country=country8, user_id=1)
session.add(club1)
session.commit()

club2 = Club(name='Al Ahly SC', description="Al Ahly, is an Egyptian\
 sports club based in Cairo. Al Ahly has a record of 41 national\
 league titles, 36 national cups titles, and 11 national super cup\
 titles making Al Ahly the most decorated club in Egypt. In addition,\
 Al Ahly has never been relegated to the Egyptian Second Division.",
              country=country8, user_id=1)
session.add(club2)
session.commit()

club3 = Club(name='Ismaily SC', description="Ismaily is an Egyptian\
 professional\
 football club, established on 13 April 1924. Ismaily won the Egyptian\
 Premier League three times in 1967, 1991 and 2002, as well as the Egyptian\
 Cup in 1997 and 2000. In 1969 the club won the CAF Champions League. That\
 event, the first for an Egyptian team, was so monumental at the time that\
 in many ways it remains a legendary victory in the minds of a whole\
 generation.",
 img_url = 'https://i.pinimg.com/originals/e7/aa/18/e7aa18b0cedb3d83824998145e29d78e.png',
   country=country8, user_id=1)
session.add(club3)
session.commit()

print "added clubs!"
