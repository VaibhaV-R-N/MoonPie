from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as bs
import json
import subprocess

xpiLink = "/tmp/tmp-u4y.xpi"
# options = Options()
# options.add_argument("--headless")
driver = webdriver.Firefox()
driver.install_addon(xpiLink,temporary=True)

global f,scroll
scroll = 500
f = True
pokeSet = set()

def scrape():
    soup = bs(driver.page_source,"lxml")
    divs = soup.find_all("div",class_="PokemonAltRow")
    for div in divs:
        span = div.find("span").find("span",class_="PokemonSprite is-normalized-width").find_next_sibling("span")
        pokeSet.add(span.text)
        print(pokeSet,"\n")

while "Zygarde-Complete" not in pokeSet:
    driver.get("https://www.smogon.com/dex/sm/pokemon/")
    if f == True:
        scrape()
        f = False
        continue

    driver.execute_script(f"window.scrollTo(0,{scroll})")
    scrape()
    scroll+=100
   
# pokeList = ['Arceus', 'Shellos', 'Ampharos-Mega', 'Ditto', 'Carracosta', 'Persian', 'Terrakion', 'Wynaut', 'Kingdra', 'Wurmple', 'Gothita', 'Silvally-Bug', 'Manectric-Mega', 'Hoppip', 'Probopass', 'Archen', 'Suicune', 'Furfrou', 'Silvally-Fire', 'Vivillon-Pokeball', 'Litwick', 'Rampardos', 'Kabuto', 'Sandslash', 'Deoxys', 'Spearow', 'Yanmega', 'Dragalge', 'Pidgeotto', 'Croconaw', 'Salazzle-Totem', 'Paras', 'Samurott', 'Amoonguss', 'Silvally-Water', 'Swampert-Mega', 'Darumaka', 'Deerling', 'Gible', 'Litleo', 'Chespin', 'Celesteela', 'Nuzleaf', 'Raticate-Alola-Totem', 'Sealeo', 'Vikavolt-Totem', 'Bonsly', 'Onix', 'Reuniclus', 'Rotom-Mow', 'Machamp', 'Hoopa', 'Raichu', 'Vanillite', 'Braviary', 'Togedemaru', 'Starmie', 'Aerodactyl', 'Scizor', 'Wormadam-Sandy', 'Clawitzer', 'Shelmet', 'Ledyba', 'Sylveon', 'Gloom', 'Plusle', 'Crabrawler', 'Ribombee-Totem', 'Yungoos', 'Mareanie', 'Chikorita', 'Grotle', 'Persian-Alola', 'Sandile', 'Naganadel', 'Conkeldurr', 'Gothorita', 'Hawlucha', 'Silvally-Ghost', 'Dhelmise', 'Amaura', 'Sawk', 'Basculin', 'Genesect-Shock', 'Chingling', 'Grovyle', 'Dusclops', 'Cyndaquil', 'Shieldon', 'Lapras', 'Lopunny-Mega', 'Kyurem-White', 'Ninetales', 'Larvitar', 'Dewott', 'Minccino', 'Cradily', 'Yamask', 'Tyranitar-Mega', 'Guzzlord', 'Poliwrath', 'Rhydon', 'Camerupt', 'Vivillon', 'Pumpkaboo-Small', 'Sawsbuck', 'Squirtle', 'Kirlia', 'Crawdaunt', 'Genesect-Chill', 'Audino-Mega', 'Nidoking', 'Garbodor', 'Turtonator', 'Tornadus-Therian', 'Bisharp', 'Drifblim', 'Qwilfish', 'Blaziken', 'Dwebble', 'Tyrogue', 'Krabby', 'Mightyena', 'Jirachi', 'Quilava', 'Metang', 'Foongus', 'Toxicroak', 'Voltorb', 'Goomy', 'Pidgeot', 'Raticate', 'Snover', 'Chandelure', 'Golduck', 'Cosmoem', 'Whismur', 'Aron', 'Shinx', 'Silvally-Dragon', 'Happiny', 'Kingler', 'Stakataka', 'Lycanroc-Midnight', 'Rotom-Heat', 'Pansage', 'Scolipede', 'Silvally-Ice', 'Carbink', 'Stoutland', 'Servine', 'Bastiodon', 'Metagross', 'Infernape', 'Cloyster', 'Houndoom-Mega', 'Rotom-Fan', 'Murkrow', 'Combee', 'Oricorio-Sensu', 'Tympole', 'Vespiquen', 'Bibarel', 'Tapu Fini', 'Gumshoos-Totem', 'Buneary', 'Koffing', 'Steelix-Mega', 'Pikachu-Hoenn', 'Nidorina', 'Araquanid', 'Armaldo', 'Glameow', 'Ho-Oh', 'Arceus-Bug', 'Oricorio-Pom-Pom', 'Seviper', 'Swoobat', 'Wimpod', 'Seel', 'Shuppet', 'Arceus-Ground', 'Clefable', 'Honedge', 'Kecleon', 'Uxie', 'Stufful', 'Dodrio', 'Drilbur', 'Machoke', 'Skorupi', 'Lileep', 'Toxapex', 'Regigigas', 'Hariyama', 'Sewaddle', 'Smeargle', 'Nidoqueen', 'Scyther', 'Dusknoir', 'Goodra', 'Aegislash-Blade', 'Salazzle', 'Buizel', 'Marshadow', 'Caterpie', 'Poliwhirl', 'Blastoise-Mega', 'Liepard', 'Roggenrola', 'Tangela', 'Cubone', 'Vigoroth', 'Poipole', 'Piloswine', 'Tauros', 'Exeggutor-Alola', 'Rufflet', 'Shroomish', 'Sharpedo', 'Ekans', 'Bidoof', 'Growlithe', 'Lampent', 'Zorua', 'Pansear', 'Charizard-Mega-X', 'Froakie', 'Flareon', 'Leavanny', 'Drowzee', 'Vulpix', 'Simisear', 'Aurumoth', 'Riolu', 'Hakamo-o', 'Arceus-Psychic', 'Lurantis-Totem', 'Mime Jr.', 'Drapion', 'Anorith', 'Vanilluxe', 'Quagsire', 'Whirlipede', 'Pikachu-Original', 'Basculin-Blue-Striped', 'Slurpuff', 'Makuhita', 'Togepi', 'Pidgey', 'Altaria-Mega', 'Scraggy', 'Hippopotas', 'Steenee', 'Togekiss', 'Venipede', 'Arcanine', 'Eelektrik', 'Slakoth', 'Lunala', 'Glaceon', 'Silvally-Electric', 'Taillow', 'Pelipper', 'Decidueye', 'Heatmor', 'Tornadus', 'Latios-Mega', 'Marill', 'Excadrill', 'Inkay', 'Zekrom', 'Escavalier', 'Mawile-Mega', 'Octillery', 'Beautifly', 'Lillipup', 'Spinarak', 'Minior-Meteor', 'Eevee-Starter', 'Gulpin', 'Shiftry', 'Togedemaru-Totem', 'Barbaracle', 'Carnivine', 'Kricketune', 'Golisopod', 'Lopunny', 'Kyurem', 'Cubchoo', 'Breloom', 'Nidorino', 'Swellow', 'Typhlosion', "Farfetch'd", 'Mr. Mime', 'Binacle', 'Meloetta-Pirouette', 'Melmetal', 'Throh', 'Ralts', 'Gengar', 'Aggron-Mega', 'Noivern', 'Swampert', 'Arceus-Fighting', 'Mimikyu-Totem', 'Fletchinder', 'Arceus-Grass', 'Gligar', 'Lycanroc-Dusk', 'Whimsicott', 'Genesect-Burn', 'Arceus-Water', 'Haxorus', 'Huntail', 'Karrablast', 'Solosis', 'Metapod', 'Dragonite', 'Klefki', 'Noctowl', 'Musharna', 'Kyogre-Primal', 'Remoraid', 'Snorlax', 'Stunfisk', 'Porygon2', 'Loudred', 'Aerodactyl-Mega', 'Reshiram', 'Aromatisse', 'Empoleon', 'Elgyem', 'Nosepass', 'Eevee', 'Charmeleon', 'Deoxys-Speed', 'Klang', 'Panpour', 'Arceus-Ghost', 'Wailmer', 'Garchomp', 'Venonat', 'Marowak-Alola', 'Skiploom', 'Regice', 'Girafarig', 'Zebstrika', 'Greninja-Ash', 'Cryogonal', 'Toucannon', 'Absol', 'Rayquaza', 'Lotad', 'Slaking', 'Mewtwo-Mega-X', 'Blitzle', 'Darmanitan-Zen', 'Prinplup', 'Granbull', 'Marowak', 'Crustle', 'Shedinja', 'Kartana', 'Pidove', 'Bellsprout', 'Porygon', 'Entei', 'Shaymin', 'Garchomp-Mega', 'Skiddo', 'Mudbray', 'Deoxys-Attack', 'Roselia', 'Medicham', 'Nincada', 'Simipour', 'Sandygast', 'Snorunt', 'Tentacool', 'Walrein', 'Vibrava', 'Wormadam-Trash', 'Purrloin', 'Phanpy', 'Sceptile-Mega', 'Arceus-Dark', 'Silvally-Fairy', 'Spinda', 'Ferrothorn', 'Silcoon', 'Igglybuff', 'Eelektross', 'Spoink', 'Thundurus', 'Trapinch', 'Tyrantrum', 'Arceus-Fire', 'Cacnea', 'Pyukumuku', 'Cherubi', 'Flabebe', 'Tranquill', 'Arbok', 'Lucario', 'Monferno', 'Silvally', 'Charmander', 'Cranidos', 'Totodile', 'Abomasnow-Mega', 'Wormadam', 'Zoroark', 'Chesnaught', 'Combusken', 'Frillish', 'Marowak-Alola-Totem', 'Kangaskhan', 'Meditite', 'Venusaur', 'Torterra', 'Bounsweet', 'Graveler-Alola', 'Dratini', 'Glalie-Mega', 'Donphan', 'Gallade-Mega', 'Abra', 'Latios', 'Ledian', 'Chansey', 'Fennekin', 'Cobalion', 'Torkoal', 'Golurk', 'Zigzagoon', 'Goldeen', 'Aggron', 'Unown', 'Silvally-Poison', 'Ducklett', 'Drampa', 'Machop', 'Weezing', 'Mismagius', 'Pikachu-Unova', 'Tsareena', 'Type: Null', 'Scrafty', 'Seedot', 'Dugtrio', 'Grimer', 'Flygon', 'Golbat', 'Meowstic-F', 'Skitty', 'Beartic', 'Surskit', 'Marshtomp', 'Litten', 'Camerupt-Mega', 'Heatran', 'Keldeo-Resolute', 'Munchlax', 'Kricketot', 'Electrode', 'Fletchling', 'Skarmory', 'Silvally-Fighting', 'Magmar', 'Wishiwashi', 'Feebas', 'Heracross-Mega', 'Espurr', 'Bunnelby', 'Magikarp', 'Dunsparce', 'Sentret', 'Hoopa-Unbound', 'Primarina', 'Ninetales-Alola', 'Cofagrigus', 'Jumpluff', 'Tropius', 'Zweilous', 'Arceus-Steel', 'Arghonaut', 'Grumpig', 'Dewgong', 'Malamar', 'Lucario-Mega', 'Magmortar', 'Trubbish', 'Cascoon', 'Hoothoot', 'Nihilego', 'Volcanion', 'Bagon', 'Geodude', 'Herdier', 'Virizion', 'Staryu', 'Audino', 'Espeon', 'Muk', 'Magnemite', 'Ampharos', 'Swanna', 'Stantler', 'Bruxish', 'Kommo-o-Totem', 'Porygon-Z', 'Venomoth', 'Kommo-o', 'Miltank', 'Ursaring', 'Honchkrow', 'Gurdurr', 'Argalis', 'Sandshrew-Alola', 'Gigalith', 'Bronzor', 'Timburr', 'Silvally-Grass', 'Treecko', 'Emolga', 'Klink', 'Teddiursa', 'Magearna', 'Lumineon', 'Bouffalant', 'Drifloon', 'Illumise', 'Luxray', 'Azurill', 'Fomantis', 'Minun', 'Medicham-Mega', 'Gothitelle', 'Mankey', 'Phione', 'Sunflora', 'Hypno', 'Umbreon', 'Alomomola', 'Pinsir', 'Skrelp', 'Mimikyu-Busted-Totem', 'Articuno', 'Meowth', 'Noibat', 'Watchog', 'Arceus-Flying', 'Clauncher', 'Xatu', 'Salandit', 'Necrozma-Ultra', 'Tapu Koko', 'Duosion', 'Archeops', 'Pupitar', 'Barboach', 'Dragonair', 'Mewtwo-Mega-Y', 'Serperior', 'Gallade', 'Petilil', 'Spritzee', 'Mesprit', 'Landorus-Therian', 'Arceus-Poison', 'Luvdisc', 'Victini', 'Comfey', 'Munna', 'Nidoran-F', 'Sableye', 'Crobat', 'Incineroar', 'Pidgeot-Mega', 'Pikachu-Partner', 'Lanturn', 'Seaking', 'Doublade', 'Hitmonchan', 'Clefairy', 'Mienfoo', 'Ivysaur', 'Manaphy', 'Venusaur-Mega', 'Sigilyph', 'Zubat', 'Clamperl', 'Cherrim', 'Jellicent', 'Brionne', 'Flaaffy', 'Galvantula', 'Lilligant', 'Poochyena', 'Diglett', 'Rattata', 'Gogoat', 'Smoochum', 'Kyurem-Black', 'Pikachu', 'Druddigon', 'Meowstic-M', 'Tyrunt', 'Genesect', 'Magneton', 'Haunter', 'Diancie', 'Yveltal', 'Mudkip', 'Avalugg', 'Torracat', 'Mimikyu', 'Vaporeon', 'Latias', 'Politoed', 'Salamence-Mega', 'Banette', 'Tyranitar', 'Purugly', 'Fearow', 'Gumshoos', 'Sudowoodo', 'Steelix', 'Arceus-Dragon', 'Lairon', 'Kadabra', 'Palossand', 'Wailord', 'Jolteon', 'Tynamo', 'Silvally-Ground', 'Groudon', 'Cottonee', 'Deino', 'Swadloon', 'Arceus-Ice', 'Corphish', 'Sunkern', 'Linoone', 'Pikipek', 'Popplio', 'Shaymin-Sky', 'Pikachu-Starter', 'Pumpkaboo-Large', 'Tapu Bulu', 'Yanma', 'Silvally-Dark', 'Kabutops', 'Castform', 'Dugtrio-Alola', 'Dartrix', 'Diggersby', 'Blissey', 'Blaziken-Mega', 'Dedenne', 'Sneasel', 'Alakazam', 'Ludicolo', 'Beldum', 'Palkia', 'Pumpkaboo-Super', 'Bewear', 'Raikou', 'Pikachu-Alola', 'Vivillon-Fancy', 'Delcatty', 'Gyarados', 'Ninjask', 'Sableye-Mega', 'Necrozma-Dusk Mane', 'Oddish', 'Heracross', 'Vullaby', 'Weepinbell', 'Aipom', 'Meganium', 'Graveler', 'Snubbull', 'Glalie', 'Vileplume', 'Azelf', 'Mew', 'Pichu', 'Magcargo', 'Beedrill', 'Sandshrew', 'Gengar-Mega', 'Boldore', 'Furret', 'Silvally-Psychic', 'Castform-Sunny', 'Lycanroc', 'Pachirisu', 'Aegislash', 'Minior', 'Gastrodon', 'Spiritomb', 'Meltan', 'Wigglytuff', 'Relicanth', 'Gliscor', 'Turtwig', 'Fraxure', 'Staraptor', 'Shelgon', 'Skuntank', 'Bulbasaur', 'Emboar', 'Joltik', 'Hippowdon', 'Doduo', 'Butterfree', 'Seismitoad', 'Starly', 'Diglett-Alola', 'Carvanha', 'Rowlet', 'Bergmite', 'Wingull', 'Ferroseed', 'Ponyta', 'Cosmog', 'Cresselia', 'Slugma', 'Solrock', 'Kangaskhan-Mega', 'Gabite', 'Delibird', 'Zapdos', 'Darkrai', 'Swinub', 'Cacturne', 'Arceus-Fairy', 'Baltoy', 'Psyduck', 'Silvally-Flying', 'Croagunk', 'Vikavolt', 'Meowth-Alola', 'Deoxys-Defense', 'Pawniard', 'Castform-Rainy', 'Mareep', 'Pyroar', 'Zeraora', 'Blacephalon', 'Rockruff', 'Numel', 'Bayleef', 'Frogadier', 'Gyarados-Mega', 'Golem-Alola', 'Luxio', 'Scatterbug', 'Mimikyu-Busted', 'Landorus', 'Ribombee', 'Bellossom', 'Araquanid-Totem', 'Cleffa', 'Kakuna', 'Cutiefly', 'Weavile', 'Palpitoad', 'Krokorok', 'Rattata-Alola', 'Raichu-Alola', 'Dustox', 'Swirlix', 'Snivy', 'Scizor-Mega', 'Abomasnow', 'Rhyperior', 'Burmy', 'Magby', 'Bronzong', 'Helioptile', 'Rotom-Frost', 'Simisage', 'Grimer-Alola', 'Nidoran-M', 'Lombre', 'Raticate-Alola', 'Ambipom', 'Slowbro-Mega', 'Delphox', 'Misdreavus', 'Regirock', 'Claydol', 'Finneon', 'Pheromosa', 'Weedle', 'Gardevoir', 'Pumpkaboo', 'Manectric', 'Slowpoke', 'Lurantis', 'Ariados', 'Whiscash', 'Exeggcute', 'Beheeyem', 'Hydreigon', 'Jangmo-o', 'Geodude-Alola', 'Pikachu-Kalos', 'Chatot', 'Lunatone', 'Castform-Snowy', 'Altaria', 'Celebi', 'Keldeo', "Oricorio-Pa'u", 'Quilladin', 'Zygarde', 'Chinchou', 'Pangoro', 'Milotic', 'Staravia', 'Necrozma', 'Mothim', 'Mantine', 'Seadra', 'Torchic', 'Magnezone', 'Komala', 'Exploud', 'Gourgeist-Small', 'Rhyhorn', 'Giratina-Origin', 'Alakazam-Mega', 'Pineco', 'Mantyke', 'Piplup', 'Patrat', 'Rapidash', 'Tirtouga', 'Slowbro', 'Arceus-Rock', 'Wooper', 'Diancie-Mega', 'Floatzel', 'Florges', 'Pikachu-Sinnoh', 'Mandibuzz', 'Hitmontop', 'Omastar', 'Swalot', 'Wishiwashi-School', 'Absol-Mega', 'Necrozma-Dawn Wings', 'Rotom-Wash', 'Tangrowth', 'Poliwag', 'Kyogre', 'Victreebel', 'Sandslash-Alola', 'Roserade', 'Tentacruel', 'Charizard', 'Jigglypuff', 'Lickitung', 'Mawile', 'Trumbeak', 'Maractus', 'Gardevoir-Mega', 'Metagross-Mega', 'Greninja', 'Sharpedo-Mega', 'Chimecho', 'Budew', 'Natu', 'Beedrill-Mega', 'Sliggoo', 'Buzzwole', 'Salamence', 'Spheal', 'Hitmonlee', 'Registeel', 'Feraligatr', 'Gorebyss', 'Zygarde-Complete', 'Moltres', 'Omanyte', 'Duskull', 'Mewtwo', 'Golett', 'Gourgeist-Large', 'Leafeon', 'Corsola', 'Mamoswine', 'Axew', 'Morelull', 'Pancham', 'Grubbin', 'Tapu Lele', 'Gastly', 'Wobbuffet', 'Lickilicky', 'Mienshao', 'Elekid', 'Pinsir-Mega', 'Jynx', 'Charjabug', 'Forretress', 'Oricorio', 'Larvesta', 'Swablu', 'Durant', 'Azumarill', 'Genesect-Douse', 'Heliolisk', 'Tepig', 'Charizard-Mega-Y', 'Sceptile', 'Zygarde-10%', 'Accelgor', 'Groudon-Primal', 'Oranguru', 'Floette', 'Crabominable', 'Mudsdale', 'Volbeat', 'Xurkitree', 'Cinccino', 'Froslass', 'Slowking', 'Cherrim-Sunshine', 'Vulpix-Alola', 'Volcarona', 'Parasect', 'Klinklang', 'Woobat', 'Silvally-Rock', 'Zangoose', 'Dialga', 'Rotom', 'Unfezant', 'Meloetta', 'Chimchar', 'Vanillish', 'Braixen', 'Solgaleo', 'Silvally-Steel', 'Blastoise', 'Darmanitan', 'Electivire', 'Spewpa', 'Primeape', 'Shiinotic', 'Togetic', 'Exeggutor', 'Pignite', 'Latias-Mega', 'Wartortle', 'Dewpider', 'Shellder', 'Oshawott', 'Lugia', 'Talonflame', 'Aurorus', 'Electrike', 'Banette-Mega', 'Shuckle', 'Horsea', 'Gourgeist', 'Giratina', 'Houndour', 'Masquerain', 'Muk-Alola', 'Xerneas', 'Electabuzz', 'Gourgeist-Super', 'Passimian', 'Rayquaza-Mega', 'Arceus-Electric', 'Phantump', 'Golem', 'Stunky', 'Krookodile', 'Houndoom', 'Trevenant', 'Thundurus-Therian'] 

pokeList  = list(pokeSet)
smogon = {}

r =  100

for pokemon in pokeList:
    subprocess.run(["clear"])
    print(f"{len(smogon.keys())}/{len(pokeList)} : {round((len(smogon.keys())*100)/len(pokeList),2)} %")

    driver.get(f"https://www.smogon.com/dex/sm/pokemon/{pokemon}/")
  
    soup = bs(driver.page_source,'lxml')


    # moves
    movesetInfoMoves = []
    try:
        divs = soup.find_all("div",class_="MovesetInfo-moves")

        if len(divs) == 0:
            continue

        for div in divs:
            moves = []
            uls = div.find_all("ul",class_="MoveList")

            for ul in uls:
                anchs = ul.find_all("a",class_="MoveLink")
                if len(anchs) > 1:
                    move = []
                    for a in anchs:
                        move.append(a.find("span").text) 
                    move = " / ".join(move)
                    moves.append(move)
                else:
                    anchs = ul.find_all("a",class_="MoveLink")

                    for a in anchs:
                        move = a.find("span").text
                        moves.append(move)

            movesetInfoMoves.append(moves)
        
        # misc
        movesetInfoMisc = []
        
        divs = soup.find_all("div",class_="MovesetInfo-misc")

        for div in divs:
            
            # items
            misc = {}

            itemList = div.find("ul",class_="ItemList") 
            lis = itemList.find_all("li")

            if len(lis)>1:
                item = []

                for li in lis:
                    spans = li.find_all("span")
                    item.append(spans[len(spans)-1].text)
                
                item = " / ".join(item)
                misc["item"] = item
            else:

                for li in lis:
                    spans = li.find_all("span")
                    item = spans[len(spans)-1].text
                    misc["item"] = item
                
            
            # abilities
            abilityList = div.find("ul",class_="AbilityList")
            lis = abilityList.find_all("li")

            if len(lis)>1:
                ability = []

                for li in lis:
                    ability.append(li.find("span").text)
                ability = " / ".join(ability)
                misc["ability"] = ability
            else:

                for li in lis:
                    misc["ability"] = li.find("span").text
            

            # natures
            natureList = div.find("ul",class_="NatureList")
            lis = natureList.find_all("li")

            if len(lis)>1:
                nature = []

                for li in lis:
                    nature.append(li.find("abbr").text)
                nature = " / ".join(nature)
                misc["nature"] = nature
            else:
                for li in lis:
                    misc["nature"] = li.find("abbr").text
            
            # EVSpread
            evConfig = div.find("ul",class_="evconfig")
            lis = evConfig.find_all("li")
            evs = []

            for li in lis:
                evs.append(li.text)
            evs = " / ".join(evs)
            misc["Evs"] = evs

            movesetInfoMisc.append(misc)

        smogon[str(pokemon).lower()] = [movesetInfoMoves,movesetInfoMisc]   

    except Exception:
        continue

jo = json.dumps(smogon,indent=4)
print(len(smogon.keys()))
with open("SmogonStrat.json", "w") as file:
    file.write(jo)
print("Scraping Has Finshed..")
