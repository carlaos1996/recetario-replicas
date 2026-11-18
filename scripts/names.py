"""Nombres legibles para marcas y perfumes a partir de los 'slugs' de Fragrantica."""
import re

BRANDS = {
    'yves-saint-laurent': 'Yves Saint Laurent', 'dolce-gabbana': 'Dolce & Gabbana', 'lancome': 'Lancôme',
    'tom-ford': 'Tom Ford', 'dior': 'Dior', 'mugler': 'Mugler', 'chanel': 'Chanel', 'hermes': 'Hermès',
    'versace': 'Versace', 'calvin-klein': 'Calvin Klein', 'maison-francis-kurkdjian': 'Maison Francis Kurkdjian',
    'chloe': 'Chloé', 'creed': 'Creed', 'lalique': 'Lalique', 'paco-rabanne': 'Paco Rabanne',
    'giorgio-armani': 'Giorgio Armani', 'jean-paul-gaultier': 'Jean Paul Gaultier', 'viktor-rolf': 'Viktor&Rolf',
    'narciso-rodriguez': 'Narciso Rodriguez', 'carolina-herrera': 'Carolina Herrera', 'armaf': 'Armaf',
    'guerlain': 'Guerlain', 'lolita-lempicka': 'Lolita Lempicka', 'maison-martin-margiela': 'Maison Margiela',
    'davidoff': 'Davidoff', 'prada': 'Prada', 'donna-karan': 'DKNY', 'issey-miyake': 'Issey Miyake',
    'nina-ricci': 'Nina Ricci', 'kenzo': 'Kenzo', 'britney-spears': 'Britney Spears', 'aquolina': 'Aquolina',
    'cacharel': 'Cacharel', 'elizabeth-arden': 'Elizabeth Arden', 'ariana-grande': 'Ariana Grande',
    'nautica': 'Nautica', 'by-kilian': 'By Kilian', 'givenchy': 'Givenchy', 'byredo': 'Byredo', 'moschino': 'Moschino',
    'marc-jacobs': 'Marc Jacobs', 'parfums-de-marly': 'Parfums de Marly', 'juicy-couture': 'Juicy Couture',
    'montblanc': 'Montblanc', 'hugo-boss': 'Hugo Boss', 'burberry': 'Burberry', 'joop': 'Joop!', 'xerjoff': 'Xerjoff',
    'mancera': 'Mancera', 'gucci': 'Gucci', 'lacoste-fragrances': 'Lacoste', 'bvlgari': 'Bvlgari',
    'lattafa-perfumes': 'Lattafa', 'nasomatto': 'Nasomatto', 'estee-lauder': 'Estée Lauder', 'elie-saab': 'Elie Saab',
    'jimmy-choo': 'Jimmy Choo', 'montale': 'Montale', 'diptyque': 'Diptyque', 'bentley': 'Bentley',
    'frederic-malle': 'Frédéric Malle', 'cerruti': 'Cerruti', 'sarah-jessica-parker': 'Sarah Jessica Parker',
    'zadig-voltaire': 'Zadig & Voltaire', 'clinique': 'Clinique', 'amouage': 'Amouage', 'afnan': 'Afnan',
    'chopard': 'Chopard', 'tommy-hilfiger': 'Tommy Hilfiger', 'nishane': 'Nishane', 'bottega-veneta': 'Bottega Veneta',
    'tiziana-terenzi': 'Tiziana Terenzi', 'azzaro': 'Azzaro', 'jo-malone-london': 'Jo Malone London',
    'paloma-picasso': 'Paloma Picasso', 'balenciaga': 'Balenciaga', 'agent-provocateur': 'Agent Provocateur',
    'salvador-dali': 'Salvador Dalí', 'valentino': 'Valentino', 'acqua-di-parma': 'Acqua di Parma', 'cartier': 'Cartier',
    'vera-wang': 'Vera Wang', 'guy-laroche': 'Guy Laroche', 'avon': 'Avon', 'sol-de-janeiro': 'Sol de Janeiro',
    'trussardi': 'Trussardi', 'roberto-cavalli': 'Roberto Cavalli', 'tauer-perfumes': 'Tauer Perfumes',
    'ralph-lauren': 'Ralph Lauren', 'escada': 'Escada', 'dsquared2': 'Dsquared²', 'kenneth-cole': 'Kenneth Cole',
    'rasasi': 'Rasasi', 'al-haramain-perfumes': 'Al Haramain', 'initio-parfums-prives': 'Initio Parfums Privés',
    'louis-vuitton': 'Louis Vuitton', 'le-labo': 'Le Labo', 'serge-lutens': 'Serge Lutens',
    'van-cleef-arpels': 'Van Cleef & Arpels', 'jeanne-arthes': 'Jeanne Arthes', 'zara': 'Zara',
    'victoria-s-secret': "Victoria's Secret", 'bath-and-body-works': 'Bath & Body Works',
    'abercrombie-fitch': 'Abercrombie & Fitch', 'kayali-fragrances': 'Kayali', 'maison-crivelli': 'Maison Crivelli',
    'penhaligon-s': "Penhaligon's", 'atelier-cologne': 'Atelier Cologne', 'l-occitane-en-provence': "L'Occitane en Provence",
    'ellis-brooklyn': 'Ellis Brooklyn', 'kim-kardashian': 'Kim Kardashian', 'paris-hilton': 'Paris Hilton',
    'jennifer-lopez': 'Jennifer Lopez', 'katy-perry': 'Katy Perry', 'taylor-swift': 'Taylor Swift', 'rihanna': 'Rihanna',
    'beyonce': 'Beyoncé', 'nicki-minaj': 'Nicki Minaj', 'lady-gaga': 'Lady Gaga', 'justin-bieber': 'Justin Bieber',
    'boucheron': 'Boucheron', 'rochas': 'Rochas', 'lanvin': 'Lanvin', 'ermenegildo-zegna': 'Ermenegildo Zegna',
    'ferrari': 'Ferrari', 'adidas': 'Adidas', 'antonio-banderas': 'Antonio Banderas', 'oriflame': 'Oriflame',
    'natura': 'Natura', 'o-boticario': 'O Boticário', 'mercedes-benz': 'Mercedes-Benz', 'swiss-arabian': 'Swiss Arabian',
    'ajmal': 'Ajmal', 'maison-alhambra': 'Maison Alhambra', 'orientica': 'Orientica', 'ex-nihilo': 'Ex Nihilo',
    'memo-paris': 'Memo Paris', 'roja-dove': 'Roja Parfums', 'roja-parfums': 'Roja Parfums', 'clean': 'Clean',
    'philosophy': 'Philosophy', 'demeter-fragrance': 'Demeter', 'the-body-shop': 'The Body Shop',
    'comme-des-garcons': 'Comme des Garçons', 'etat-libre-d-orange': "État Libre d'Orange",
    'histoires-de-parfums': 'Histoires de Parfums', 'juliette-has-a-gun': 'Juliette Has A Gun',
    'escentric-molecules': 'Escentric Molecules', 'goutal': 'Goutal', 'annick-goutal': 'Annick Goutal',
    'l-artisan-parfumeur': "L'Artisan Parfumeur", 'parfums-de-nicolai': 'Parfums de Nicolaï', 'miu-miu': 'Miu Miu',
    'michael-kors': 'Michael Kors', 'coach': 'Coach', 'kate-spade': 'Kate Spade', 'guess': 'Guess',
    'benetton': 'Benetton', 'mexx': 'Mexx', 'jil-sander': 'Jil Sander', 'lacoste': 'Lacoste',
    'emporio-armani': 'Emporio Armani', 'diesel': 'Diesel', 'police': 'Police', 'puma': 'Puma', 'nike': 'Nike',
    'yardley': 'Yardley', 'bond-no-9': 'Bond No. 9', 'bdk-parfums': 'BDK Parfums', 'french-avenue': 'French Avenue',
    'khadlaj': 'Khadlaj', 'arabian-oud': 'Arabian Oud', 'sospiro-perfumes': 'Sospiro', 'franck-boclet': 'Franck Boclet',
    'm-micallef': 'M. Micallef', 'carner-barcelona': 'Carner Barcelona', 'kilian': 'Kilian', 'ormonde-jayne': 'Ormonde Jayne',
    'stephane-humbert-lucas-777': 'Stéphane Humbert Lucas 777', 'les-parfums-de-rosine': 'Les Parfums de Rosine',
    'gres': 'Grès', 'tiffany': 'Tiffany & Co.', 'rosendo-mateu-olfactive-expressions': 'Rosendo Mateu',
    'giorgio-beverly-hills': 'Giorgio Beverly Hills', 'salvatore-ferragamo': 'Salvatore Ferragamo',
}

UPPER = {'ck', 'dkny', 'xj', 'xs', 'ii', 'iii', 'iv', 'xxv', 'vip', 'edp', 'edt', 'ysl', 'nyc', 'usa', 'uv', 'bdk',
         'mfk', 'xl', 'ck1'}
SMALL = {'de', 'la', 'le', 'les', 'du', 'des', 'pour', 'of', 'the', 'by', 'in', 'et', 'en', 'di', 'del', 'a', 'al',
         'for', 'and', 'y', 'au', 'sur', 'with', 'on', 'da', 'do', 'dei', 'della', 'or', 'par'}
ACCENTS = {
    'hermes': 'Hermès', 'chloe': 'Chloé', 'tresor': 'Trésor', 'poeme': 'Poème', 'fraiche': 'Fraîche', 'cherie': 'Chérie',
    'elysees': 'Élysées', 'memoire': 'Mémoire', 'mediterranee': 'Méditerranée', 'desert': 'Désert', 'premiere': 'Première',
    'imperatrice': 'Impératrice', 'poudree': 'Poudrée', 'extreme': 'Extrême', 'reve': 'Rêve', 'gio': 'Giò',
    'boise': 'Boisé', 'epices': 'Épices', 'ete': 'Été', 'eclat': 'Éclat', 'eternite': 'Éternité', 'demon': 'Démon',
    'elegance': 'Élégance', 'creme': 'Crème', 'legere': 'Légère', 'lumiere': 'Lumière', 'n05': 'N°5', 'n5': 'N°5',
    'cafe': 'Café', 'precieuse': 'Précieuse', 'pi': 'π', 'eternelle': 'Éternelle', 'delice': 'Délice',
    'reglisse': 'Réglisse', 'tiare': 'Tiaré', 'naive': 'Naïve', 'privee': 'Privée', 'secrete': 'Secrète',
    'ideal': 'Idéal', 'elephant': 'Éléphant', 'anais': 'Anaïs', 'panthere': 'Panthère',
}

# Nombres completos que la regla automática no arma bien (clave: marca/slug).
OVERRIDES = {
    'dolce-gabbana/d-g-anthology-l-imperatrice-3': "D&G Anthology L'Impératrice 3",
    'mugler/a-men': 'A*Men', 'mugler/a-men-pure-havane': 'A*Men Pure Havane', 'mugler/a-men-pure-malt': 'A*Men Pure Malt',
    'calvin-klein/ck-one': 'CK One', 'calvin-klein/ck-one-shock-for-him': 'CK One Shock for Him',
    'calvin-klein/ck-in2u-for-her': 'CK IN2U for Her', 'donna-karan/dkny-be-delicious': 'Be Delicious',
    'xerjoff/xj-1861-naxos': 'XJ 1861 Naxos', 'tauer-perfumes/02-l-air-du-desert-marocain': "L'Air du Désert Marocain",
    'by-kilian/angels-share': "Angels' Share", 'by-kilian/love-don-t-be-shy': "Love, Don't Be Shy",
    'chanel/chanel-n05-eau-premiere': 'N°5 Eau Première', 'chanel/chanel-no-5-parfum': 'N°5 Parfum',
    'chanel/chanel-no-5-eau-de-parfum': 'N°5 Eau de Parfum', 'chanel/chanel-no-5-l-eau': "N°5 L'Eau",
    'chanel/chanel-no-19-eau-de-parfum': 'N°19 Eau de Parfum', 'chanel/egoiste': 'Égoïste',
    'chanel/egoiste-platinum': 'Égoïste Platinum', 'dior/j-adore': "J'adore", 'paco-rabanne/1-million': '1 Million',
    'giorgio-armani/acqua-di-gio': 'Acqua di Giò', 'giorgio-armani/si': 'Sì', 'giorgio-armani/si-passione': 'Sì Passione',
    'cerruti/1881': '1881 pour Femme', 'tom-ford/fucking-fabulous': 'F*cking Fabulous',
    'givenchy/ange-ou-demon': 'Ange ou Démon', 'givenchy/ange-ou-demon-le-secret': 'Ange ou Démon Le Secret',
    'givenchy/l-interdit-eau-de-parfum-rouge': "L'Interdit Rouge",
    'acqua-di-parma/acqua-di-parma-blu-mediterraneo-fico-di-amalfi': 'Blu Mediterraneo Fico di Amalfi',
    'giorgio-armani/emporio-armani-stronger-with-you': 'Stronger With You',
    'giorgio-armani/emporio-armani-stronger-with-you-intensely': 'Stronger With You Intensely',
    'dior/dior-homme-2020': 'Dior Homme (2020)', 'dior/dior-homme': 'Dior Homme (2011)',
    'dior/miss-dior-2012': 'Miss Dior (2012)', 'moschino/cheap-chic-i-love-love': 'Cheap & Chic I Love Love',
    'lalique/encre-noire-a-l-extreme': "Encre Noire à l'Extrême", 'carolina-herrera/212-vip-rose': '212 VIP Rosé',
    'kenzo/kenzo-jungle-l-elephant': "Jungle L'Éléphant", 'nina-ricci/l-air-du-temps': "L'Air du Temps",
    'lolita-lempicka/l-de-lolita-lempicka': 'L de Lolita Lempicka', 'givenchy/pi': 'π (Pi)',
    'jean-paul-gaultier/le-male-le-parfum': 'Le Male Le Parfum', 'jean-paul-gaultier/le-beau-le-parfum': 'Le Beau Le Parfum',
    'dolce-gabbana/dolce-gabbana-pour-femme': 'Dolce & Gabbana pour Femme', 'gucci/memoire-d-une-odeur': "Mémoire d'une Odeur",
    'paco-rabanne/black-xs': 'Black XS', 'paco-rabanne/black-xs-for-her': 'Black XS for Her',
}


def _tok(t, first):
    if t in ACCENTS:
        return ACCENTS[t]
    if t in UPPER:
        return t.upper()
    if not first and t in SMALL:
        return t
    return t[:1].upper() + t[1:]


def perfume_name(brand_slug, slug):
    key = f'{brand_slug}/{slug}'
    if key in OVERRIDES:
        return OVERRIDES[key]
    toks = slug.split('-')
    # quitar el año final que Fragrantica usa para distinguir ediciones (el año ya se muestra aparte)
    if len(toks) > 1 and re.fullmatch(r'(19|20)\d\d', toks[-1]):
        toks = toks[:-1]
    out = []
    i = 0
    while i < len(toks):
        t = toks[i]
        if t in ('l', 'd', 'j', 'qu') and i + 1 < len(toks):
            nxt = _tok(toks[i + 1], True)
            pre = t.upper() if (not out or t == 'l') else t
            out.append(f"{pre}'{nxt}")
            i += 2
            continue
        if t in ('t', 's') and out:
            out[-1] = out[-1] + "'" + t
            i += 1
            continue
        out.append(_tok(t, not out))
        i += 1
    return ' '.join(out)


def brand_name(slug):
    if slug in BRANDS:
        return BRANDS[slug]
    return ' '.join(_tok(t, i == 0) for i, t in enumerate(slug.split('-')))
