from soils import soils

def advice_generator(crop_option_list):
    if crop_option_list == 'crop_option_rice':
        s1 = 'Planting rice is easy; getting it to grow through harvest is challenging. Ideally, you need at least 40 continuous days of warm temps over 70 F. (21 C.). Those of you who live in the South or in California will have the best luck, but the rest of us can also try our hand at growing rice indoors, under lights if necessary.'
        s2 = 'First off, you need to find one or several plastic containers without holes. One or several depending upon how many miniature pseudo rice paddies you want to create. Next, either purchase rice seed from a gardening supplier or buy long grain brown rice from a bulk foods store or in a bag. Organically grown rice is best and it can’t be white rice, which has been processed.'
        s3 = 'Fill the bucket or plastic container with 6 inches of dirt or potting soil. Add water up to 2 inches over the soil level. Add a handful of the long grain rice to the bucket. The rice will sink to the dirt. Keep the bucket in a warm, sunny area and move it to a warm place at night.'
        points_s1 = 'Rice plants don’t need too much care from here on out. Keep the water level at 2 inches or so above the dirt. When the rice plants are 5-6 inches tall, increase the water depth to 4 inches. Then, allow the water level to lower on its own over a period of time. Ideally, by the time you harvest them, the plants should no longer be in standing water.'
        points_s2 = 'If all goes well, rice is ready to harvest in its fourth month. The stalks will go from green to gold to indicate it is time to harvest. Harvesting rice means cutting and gathering the panicles attached to the stalks. To harvest the rice, cut the stalks and allow them to dry, wrapped in a newspaper, for two to three weeks in a warm, dry place.'
        points_s3 = 'Once the rice stalks have dried, roast in a very low heat oven (under 200 F./93 C.) for around an hour, then remove the hulls by hand. That’s it; you can now cook with your very own home grown, long grain brown rice.'
        return {'message':[s1,s2,s3],'points':[points_s1, points_s2, points_s3]}

    elif crop_option_list == 'crop_option_wheat':
        s1 = 'Depending on the planting season, choose from winter or spring wheat varieties. Hard red wheat cultivars are the most common used for baking and are available in both warm and cool season varieties.'
        s2 = 'Once you’ve chosen the variety of wheat you wish to grow, the rest is fairly simple. Wheat prefers a neutral soil of about 6.4 pH. First, till the soil to a depth of 6 inches in a sunny area of the garden. If your soil is lacking, amend a couple of inches of compost in as you till. '
        s3 = 'Next, broadcast the seeds by hand or with a crank seeder. Rake the soil to work the seed into the top 2 inches of soil. To aid in moisture conservation and help control weeds, follow up with a 2-to 4-inch layer of loose straw mulch spread out over the wheat plot.'
        points_s1 = 'Winter wheat is planted in the fall and grows until early winter and then goes dormant. Spring’s warm temps stimulate new growth and seed heads are formed in about two months.'
        points_s2 = 'Spring wheat is planted in the spring and ripens in mid to late summer. It can stand drier weather than winter wheat but doesn’t tend to yield as highly.'
        return {'message':[s1,s2,s3],'points':[points_s1, points_s2]}

    elif crop_option_list == 'crop_option_sugarcane':
        s1 = 'Studies have shown the main sugarcane nutrient requirements are nitrogen, phosphorus, magnesium, sulfur and silicon. The exact amounts of these nutrients depend upon your soil, but at least it’s a place to start. The soil pH will affect the plant’s ability to absorb and added nutrients and must be 6.0 to 6.5 for optimal results.'
        s2 = 'Other factors will affect the exact amount of nutrient absorbed, such as heavy soil, which can minimize uptake of nitrogen. If all factors are considered and amended, a general guideline on feeding sugarcane plants will help develop an annual fertilizer program.'
        points_s1 = 'Often micronutrients are found in the soil, but when cropping, these get depleted and require replacement. Sulfur use is not a nutrient additive but is used to reduce soil pH where necessary in order to enhance absorption of nutrients. Therefore, it should only be used after a pH test to amend soil. '
        points_s2 = 'Similarly, silicon is not essential but can be beneficial. If soil tests low, current recommendations are 3 tons per acre/.40ha. Magnesium can come from dolomite to maintain a soil pH of at least 5.5. '
        points_s3 = 'All of these require soil testing for optimal nutrient levels and may change annually.'
        return {'message':[s1,s2],'points':[points_s1, points_s2, points_s3]}

    elif crop_option_list == 'crop_option_groundnut':
        s1 = 'Tubers or young plants are available from a few nurseries, or of course, you can risk it and dig them up yourself if they grow in your neck of the woods. Wear heavy gloves and long pants and shirt sleeves to protect from the poison ivy no doubt growing with the groundnuts.'
        points_s1 = 'Plant the groundnuts in spring, ideally in a raised bed in light, well-draining soil. Provide the plants with a support since groundnuts have an upright vining habit. '
        points_s2 = 'Keep the garden free of weeds to discourage pests but be gentle around the root ball of the tubers. Seedlings need at least two growing years and a minimum photoperiod of 14 hours to stimulate blooms. '
        points_s3 = 'Harvest the tubers in the fall after the first frost has killed of the foliage.'
        return {'message':[s1],'points':[points_s1, points_s2, points_s3]}

    elif crop_option_list == 'crop_option_apple':
        s1 = 'Before fertilizing apple trees, know your boundaries. Mature trees have large root systems that can extend outwards 1 ½ times the diameter of the canopy and can be 4 feet deep. These deep roots absorb water and store excess nutrients for the successive year, but there are also smaller feeder roots that reside in the top foot of soil that absorb most nutrients.'
        s2 = 'Fertilizer for apples needs to be broadcast evenly on the surface, beginning a foot away from the trunk and extending well beyond the drip line. The best time to fertilize an apple tree is in the fall once the leaves have dropped.'
        s3 = 'If you are fertilizing apple trees with a 10-10-10, spread at the rate of one pound per inch of trunk diameter measured one foot from the ground up. The maximum amount of 10-10-10 used is 2 ½ pounds per year.'
        s4 = 'Alternatively, you may spread a 6-inch band of calcium nitrate with the drip line at a rate of 2/3 pound per 1 inch of trunk diameter along with ½ pound per 1-inch trunk diameter of sulfate of potash-magnesia. Don’t exceed 1 ¾ pound of calcium nitrate or 1 ¼ pound of sulfate of potash-magnesia (sul-po-mag).'
        s5 = 'Young apple trees, from 1-3 years of age, should grow about a foot or more per year. If they aren’t, increase the fertilizer (10-10-10) in the second and third year by 50%. Trees that are 4 years or older may or may not need nitrogen depending upon their growth, so if they grow less than 6 inches, follow the above rate, but if they grow more than a foot, apply the sul-po-mag and boron if needed. No 10-10-10 or calcium nitrate!'
        points_s1 = 'Boron deficiency is common amongst apple trees. If you notice brown, corky spots on the inside of the apples or bud death at shoot ends, you may have a boron deficiency. An easy fix is the application of borax every 3-4 years in the amount of ½ pound per full sized tree.'
        points_s2 = 'Calcium deficiencies result in soft apples that rapidly spoil. Apply lime as a preventative in the amount of 2-5 pounds per 100 square feet. Monitor the soil pH to see if this is necessary, and after application, make sure it doesn’t go over 6.5-7.0.'
        points_s3 = 'Potassium improves fruit size and color and protects from frost damage in the spring. For a normal application, apply 1/5 pound potassium per 100 square feet per year. Deficiencies in potassium result in leaf curl and browning of older leaves along with paler than normal fruit. If you see sign of deficiency, apply between 3/10 and 2/5 of a pound of potassium per 100 square feet.'
        return {'message':[s1,s2,s3,s4,s5],'points':[points_s1, points_s2, points_s3]}

    elif crop_option_list == 'crop_option_strawberry':
        s1 = 'There are three types of strawberry plants: June bearing, which fruits in June; spring bearing, which provides fruit early in the season; and everbearing, which will fruit all summer long.'
        s2 =  'If you want to know when to plant strawberries, you’ll plant them as soon as the ground is workable in the spring, with March or April being best time in most areas. This gives them ample time to get established before the warm weather.'
        s3 = 'If you are wondering how to plant strawberries, do it on a cloudy day. This is so that the plants do not wilt while you are planting them and before you get to the point where you can water them. Do not cover the crown of the plant with dirt. Just barely cover the roots. After planting them, make sure you water them. This gives them a great start.'
        points_s1 = 'There are different ways to plant your strawberries: First, there is a matted row system. In this system, the plants should be set about 18 to 30 inches (46-76 cm.) apart and rows should be about 3 feet (.91 m.) apart. This allows the daughters to roam throughout the garden area set aside for strawberries. When taking care of strawberries, leave these daughters alone so they can form. This is best for June and spring bearing plants since the more daughters the better.'
        points_s2 = 'If you are planting everbearing strawberries, you’ll want to use the hill system. This system doesn’t allow for daughters, and everbearing grows bigger strawberries, which require one main plant.'
        points_s3 ='Sun – The number one tip on how to grow strawberries is that they need sun. Make sure that the spot you choose for your strawberry plants get plenty of full sun. Many strawberries produce their blossoms in the early spring. Making sure that they are in a sunny spot will help keep late frosts from killing off those blossoms. Plus, the more sun strawberry plants get, the bigger and better the strawberries they produce.'
        points_s4 = 'Drainage – Another good tip is to make sure where you plant them has good drainage. If your yard is clay-heavy or does not have good drainage, you’ll want to consider either creating a mound of your strawberry plants to grow on or building a raised bed for your strawberries.'
        points_s5 = 'Compost – Compost is another key to growing a strawberry patch that produces big, sweet berries. Make sure that the soil has been fully amended with good compost and composted manure.'
        points_s6 = 'Space – Strawberry plants like to spread out. If you give the strawberry plant runners room, they’ll spread and create more strawberry plants for next year.'
        points_s7 = 'Pinching – I know it can be hard, but with most strawberry plants you will want to pinch the blossoms and strawberry plant runners the first year. This will ensure that your strawberries develop a good root system and will be better able to grow the best strawberry possible.'
        return {'message':[s1, s2, s3],'points':[points_s1, points_s2, points_s3, points_s4, points_s5, points_s5, points_s6, points_s7]}

    elif crop_option_list == 'crop_option_maize':
        s1 = 'If you want to grow your own corn, you need to know how to grow corn from seed. There aren’t many people who actually start corn plants first; it just isn’t feasible.'
        points_s1 = 'Corn enjoys growing in an area that allows for full sunshine. If you want to grow corn from seed, be sure you plant the seeds in well drained soil, which will increase your yield dramatically. Make sure your soil has a lot of organic matter, and fertilize before you plant the corn. Good soil preparation is very important.'
        points_s2 = 'Wait for the temperature of the soil to reach 60 F. (18 C.) or above. Make sure there have been plenty of frost-free days before putting the corn into the soil. Otherwise, your crop will be sparse. '
        points_s3 = 'If you’re thinking about how to grow corn from seed, there are only a few rules to follow. First, make sure you make your rows 24-30 inches (60-76 cm.) apart from each other. Plant the corn 1 to 2 inches (2.5 to 5 cm.) deep in the soil about 9 to 12 inches (23-30 cm.) apart. '
        points_s4 = 'Mulch will help keep your corn weed-free and will retain moisture during hot, dry weather.'
        return {'message':[s1],'points':[points_s1,points_s2,points_s3,points_s4]}

    elif crop_option_list == 'crop_option_grapes':
        s1 = 'If you are still in the planning stages with regards to grapevines, now is the time to amend the soil. Use a home testing kit to determine the makeup of your soil. Generally, but dependent upon the grape variety, you want a soil pH of 5.5 to 7.0 for optimal growth. To raise a soil pH, add dolomitic limestone; to lower a pH, amend with sulfur following the manufacturer’s instructions. '
        points_s1 = 'If the results of your test show the soil pH is fine but magnesium is lacking, add 1 pound of Epsom salts for each 100 square feet.'
        points_s2 = 'Should you find your soil is lacking in phosphorus, apply triple phosphate (0-45-0) in the amount of ½ pound, superphosphate (0-20-0) at the rate of ¼ pound or bone meal (1-11-1) in the amount of 2 ¼ pounds (6 ¾ cups) per 100 square feet.'
        points_s3 = 'Lastly, if the soil is low in potassium, add ¾ pound of potassium sulfate or 10 pounds of greensand.'
        return {'message':[s1],'points':[points_s1, points_s2, points_s3]}

    elif crop_option_list == 'crop_option_coffee':
        s1 = 'Ideally to grow coffee bean plants, you should start with a freshly picked coffee cherry, but most of us don’t live in a coffee producing country, so this is a bit problematic. If, however, you do happen to reside in a coffee producing country, pick ripe coffee cherries by hand, pulp them, wash, and ferment in a container until the pulp flops off. '
        s2 = 'After this, rewash, discarding any beans that float. Then dry the beans on a mesh screen in open, dry air but not direct sun. The beans should be slightly soft and moist inside and dry on the outside; bite into it to find out. '
        points_s1 = 'Since most of us don’t live in a coffee-producing region, green coffee can be bought from a green coffee supplier. Make sure it is from a fresh, recent crop. Although the bean can be germinated for almost four months, surer results are had if fresh.'
        points_s2 = 'You will probably want to plant many seeds to get one plant; they’re kind of finicky. Fresh seeds germinate in 2 ½ months while older seeds take about 6 months.'
        return {'message':[s1,s2],'points':[points_s1,points_s2]}

def advice(soil_type, crop_type):
    if soil_type == 'soil_type_alluvial':
        data = soils.alluvial_soil_data()
    elif soil_type == 'soil_type_black':
        data = soils.black_soil_data()
    elif soil_type == 'soil_type_red':
        data = soils.red_soil_data()
    elif soil_type == 'soil_type_mountain':
        data = soils.mountain_soil_data()
    elif soil_type == 'soil_type_laterite':
        data = soils.laterite_soil_data()
    elif soil_type == 'soil_type_desert':
        data = soils.desert_soil_data()
    soil_type_name = soils.soil_name_converter(soil_type)
    crop_option = soils.crop_name_converter(crop_type)
    advice_dictionary = {}
    advice_dictionary['crop_option'] = crop_option
    advice_dictionary['soil_type'] = soil_type_name
    generator_data = advice_generator(crop_type)
    advice_dictionary['advice_messages'] = generator_data['message']
    advice_dictionary['advice_points'] = generator_data['points']
    if crop_option in data['crop']:
        advice_dictionary['compatibility'] = ""+crop_option+" is recommended for "+soil_type_name
    else :
        advice_dictionary['compatibility'] = ""+crop_option+" is not recommended for "+soil_type_name

    return advice_dictionary
