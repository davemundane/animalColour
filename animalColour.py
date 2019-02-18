import time
import re
from slackclient import SlackClient
import random

slack_client = SlackClient('<SlackAPIKey')
animalcolour_id = None

RTM_READ_DELAY = 1
EXAMPLE_COMMAND = "make"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


def parse_bot_commands(slack_events):
	"""
		Parses a list of events coming from the Slack RTM API to find bot commands.
		If a bot command is found, this function returns a tuple of command and channel.
		If its not found, then this function returns None, None.
	"""
	for event in slack_events:
		if event["type"] == "message" and not "subtype" in event:
			user_id, message = parse_direct_mention(event["text"])
			if user_id == animalcolour_id:
				return message, event["channel"]
	return None, None
	
def parse_direct_mention(message_text):
	"""
		Finds a direct mention (a mention that is at the beginning) in message text
		and returns the user ID which was mentioned. If there is no direct mention, returns None
	"""
	matches = re.search(MENTION_REGEX, message_text)
	# the first group contains the username, the second group contains the remaining message
	return (matches.group(1), matches.group(2).strip()) if matches else (None, None)
	
def handle_command(command, channel):
	"""
		Executes bot command if the command is known
	"""
	# Default response is help text for the user
	default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

	# Finds and executes the given command, filling in response
	response = None
	# This is where you start to implement more commands!
	if command.startswith(EXAMPLE_COMMAND):
		thisColour = getColour()
		thisAnimal = getAnimal()
		response = "Your random name is: " + thisColour + " " + thisAnimal + "\r\n" + "Use it wisely!" 

	# Sends the response back to the channel
	slack_client.api_call(
		"chat.postMessage",
		channel=channel,
		text=response or default_response
	)


def getColour(): 
	
	colours=["Alabaster","Almond","Alpine","Aluminium","Amber","Amethyst","Apache","Apple","Apricot","Aquamarine","Asphalt","Astral","Aubergine","Auburn","Avocado","Azure","Bamboo","Barberry","Beige","Birch","Bismark","Black","Blond","Blue","Blush","Bourbon","Brandy","Brass","Bronze","Brown","Burgundy","Byzantine","Cactus","Calico","Canary","Caper","Capri","Caramel","Cashmere","Casper","Castro","Cedar","Celery","Celeste","Cello","Celtic","Cement","Ceramic","Cerise","Chalky","Chambray","Chantilly","Charcoal","Chenin","Chestnut","Chiffon","Chino","Chocolate","Cinder","Cinnabar","Citron","Citrus","Claret","Clementine","Clover","Coconut","Coffee","Cognac","Cola","Comet","Como","Concrete","Conifer","Copper","Coral","Corduroy","Coriander","Cork","Corn","Cosmos","Cranberry","Cream","Creole","Crimson","Cumin","Cyan","Cyprus","Daffodil","Dawn","Deco","Denim","Derby","Desert","Diamond","Diesel","Dune","Ebony","Eclipse","Eden","Eggshell","Emerald","Espresso","Everglade","Fawn","Fern","Ferra","Fire","Flame","Flax","Flint","Frost","Fuchsia","Ginger","Glitter","Golden","Gothic","Grape","Graphite","Gravel","Gray","Green","Gunmetal","Heather","Hemp","Holly","Honeydew","Iceberg","Indigo","Iris","Iron","Ironstone","Ivory","Jade","Jaffa","Jasmine","Java","Jewel","Juniper","Kelp","Khaki","Korma","Laser","Lava","Lavender","Leather","Lemon","Licorice","Lima","Lime","Linen","Liver","Lotus","Madras","Magenta","Magnolia","Mahogany","Maize","Malachite","Mandalay","Mandarin","Mandy","Manhattan","Marigold","Mariner","Maroon","Marzipan","Masala","Matisse","Mauve","Melon","Mercury","Merino","Merlot","Midnight","Mint","Moccasin","Mocha","Mortar","Muesli","Mulberry","Mustard","Navy","Neptune","Nero","Nickel","Nugget","Nutmeg","Oasis","Ochre","Olive","Onion","Onyx","Opal","Opium","Orange","Orchid","Oregon","Paprika","Parsley","Patina","Peach","Pear","Pearl","Peat","Peppermint","Pewter","Pink","Pistachio","Platinum","Plum","Polar","Porcelain","Primrose","Pumpkin","Purple","Putty","Raspberry","Raven","Rose","Rouge","Ruby","Rum","Rust","Saffron","Sage","Sandstone","Sapphire","Scarlet","Sepia","Silk","Silver","Smoke","Strawberry","Sunset","Tan","Taupe","Teak","Teal","Topaz","Turmeric","Turquoise","Twilight","Ultramarine","Umber","Vanilla","Vermilion","Violet","Walnut","Whiskey","White","Yellow","Zest"]
		
	number = random.randint(0,len(colours))
	thisColour = colours[number]
	return thisColour
		
def getAnimal():

	animals = ["Aardvark","Albatross","Alligator","Alpaca","Angelfish","Anteater","Antelope","Armadillo","Avocet","Axolotl","Baboon","Badger","Balinese","Bandicoot","Barb","Barnacle","Barracuda","Beagle","Bear","Beaver","Beetle","Bison","Bloodhound","Boar","Bobcat","Bombay","Bongo","Bonobo","Budgerigar","Buffalo","Bulldog","Bullfrog","Burmese","Butterfly","Caiman","Camel","Capybara","Caracal","Caribou","Cassowary","Caterpillar","Catfish","Cattle","Centipede","Chameleon","Chamois","Cheetah","Chicken","Chihuahua","Chimpanzee","Chinchilla","Chinook","Chipmunk","Chough","Cichlid","Clam","Coati","Cobra","Cockroach","Collie","Coral","Cormorant","Cougar","Coyote","Crab","Crane","Crocodile","Crow","Curlew","Cuscus","Cuttlefish","Dachshund","Dalmatian","Deer","Dhole","Dingo","Dinosaur","Discus","Dodo","Dogfish","Dolphin","Donkey","Dormouse","Dotterel","Dove","Dragonfly","Drever","Duck","Dugong","Dunker","Dunlin","Eagle","Earwig","Echidna","Eland","Elephant","Falcon","Ferret","Finch","Fish","Flamingo","Flounder","Fossa","Fox","Frigatebird","Frog","Galago","Gaur","Gazelle","Gecko","Gerbil","Gharial","Gibbon","Giraffe","Gnat","Goat","Goldfinch","Goldfish","Goose","Gopher","Gorilla","Goshawk","Grasshopper","Greyhound","Grouse","Guanaco","Gull","Guppy","Hamster","Hare","Harrier","Havanese","Hawk","Hedgehog","Heron","Herring","Himalayan","Hippopotamus","Hornet","Horse","Human","Hummingbird","Hyena","Ibis","Iguana","Impala","Indri","Insect","Jackal","Jaguar","Javanese","Jellyfish","Kakapo","Kangaroo","Kingfisher","Kiwi","Koala","Kouprey","Kudu","Labradoodle","Ladybird","Lapwing","Lark","Lemming","Lemur","Leopard","Liger","Lion","Lionfish","Lizard","Llama","Lobster","Locust","Loris","Louse","Lynx","Lyrebird","Macaw","Magpie","Mallard","Maltese","Manatee","Mandrill","Markhor","Marten","Mastiff","Mayfly","Meerkat","Millipede","Mink","Mole","Molly","Mongoose","Mongrel","Monkey","Moorhen","Moose","Mosquito","Moth","Mouse","Mule","Narwhal","Neanderthal","Newfoundland","Newt","Nightingale","Numbat","Ocelot","Octopus","Okapi","Opossum","Orang-utan","Oryx","Ostrich","Otter","Owl","Ox","Oyster","Pademelon","Panther","Parrot","Partridge","Peacock","Peafowl","Pekingese","Pelican","Penguin","Persian","Pheasant","Pigeon","Pika","Pike","Piranha","Platypus","Pointer","Pony","Poodle","Porcupine","Porpoise","Possum","Prawn","Puffin","Puma","Quail","Quelea","Quetzal","Quokka","Quoll","Rabbit","Raccoon","Ragdoll","Rail","Rattlesnake","Raven","Deer","Panda","Reindeer","Rhinoceros","Robin","Rook","Rottweiler","Ruff","Salamander","Salmon","Sandpiper","Saola","Sardine","Scorpion","Urchin","Seahorse","Seal","Serval","Shark","Sheep","Shrew","Shrimp","Siamese","Siberian","Skunk","Sloth","Snail","Snake","Snowshoe","Somali","Sparrow","Spider","Sponge","Squid","Squirrel","Starfish","Starling","Stingray","Stinkbug","Stoat","Stork","Swallow","Swan","Tang","Tapir","Tarsier","Termite","Tetra","Tiffany","Tiger","Toad","Tortoise","Toucan","Tropicbird","Trout","Tuatara","Turkey","Turtle","Uakari","Uguisu","Umbrellabird","Vicuña","Viper","Vulture","Wallaby","Walrus","Warthog","Wasp","Buffalo","Weasel","Whale","Whippet","Wildebeest","Wolf","Wolverine","Wombat","Woodcock","Woodlouse","Woodpecker","Worm","Wrasse","Wren","Zebra","Zebu"]	

	number = random.randint(0,len(animals))
	thisAnimal = animals[number]
	return thisAnimal
	
	
if __name__ == "__main__":
	if slack_client.rtm_connect(with_team_state=False):
		print("AnimalColour connected and running!")
		# Read bot's user ID by calling Web API method `auth.test`
		animalcolour_id = slack_client.api_call("auth.test")["user_id"]
		while True:
			command, channel = parse_bot_commands(slack_client.rtm_read())
			if command:
				handle_command(command, channel)
				time.sleep(RTM_READ_DELAY)
	else:
		print("Connection failed. Exception traceback printed above.")