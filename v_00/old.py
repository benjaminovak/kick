urls = ['https://www.kickstarter.com/projects/martinmonk/alpha-girl-alphamadchen-short-film?ref=city',
        'https://www.kickstarter.com/projects/buildbearhq/buildbearhq-our-shipping-container-diner?ref=category',
        'https://www.kickstarter.com/projects/1713137134/friday-feature-documentary?ref=city',
        'https://www.kickstarter.com/projects/martinmonk/alpha-girl-alphamadchen-short-film?ref=city',
        'https://www.kickstarter.com/projects/347698129/dialect-a-game-about-language-and-how-it-dies?ref=home_potd',
        'https://www.kickstarter.com/projects/viktorhertz/andy-warhol-pictogram-poster?ref=category_location',
        'https://www.kickstarter.com/projects/anrong/grandpa-by-an-rong-xu?ref=category']

#urls = ['https://www.kickstarter.com/projects/1713137134/friday-feature-documentary?ref=city']

t = datetime.datetime.now()
j = 0
for url in urls:
    try:
        wp = Project(url)
        wp.find_features()
        jsn = {'Url': wp.url,
               'Title' : wp.title,
               'Campaign year': wp.year,
               'Campaign month': wp.month,
               'Category': wp.category, 
               'Subcategory':  wp.subcategory,
               'Author': 
               {
                    'Length of description': wp.cdataLength,
                    'Description': wp.cdata, 
                    'Facebook connection': wp.pcreator[0],
                    'Number of backed projects': wp.pcreator[1], 
                    'Number of created projects': wp.pcreator[2]
                },
               'Title length': wp.titleLength,
               'Goal': wp.goal, 
               'Duration': wp.num_of_days, 
               'Number of pledge levels': wp.num_of_rewards, 
               'Minimum pledge tiers': wp.min_reward,
               'Maximum pledge tiers': wp.max_reward, 
               'Length of project description': wp.num_characters, 
               'Project description': wp.text,
               'Abstract': wp.abstract,
               'Length of abstract': wp.abstractLength,
               'Number of images': wp.num_of_pictures, 
               'Number of Faq items': wp.faq,
               'Number of videos': wp.video, 
               'Has a video': wp.hasVideo, 
               'Success': wp.success
              }

        dirc = "data/" + str(wp.year) + "/" + str(wp.month)
        if not os.path.exists(dirc):
            os.makedirs(dirc)
        with open(dirc + "/" + str(wp.datetime) + '.json', 'w') as fp:
            json.dump(jsn, fp, indent=4)
            
    except Exception as inst:
        j++
        continue
print("Errors: ", j)
tK = datetime.datetime.now()
print("Time: ", abs(t-tK).seconds)