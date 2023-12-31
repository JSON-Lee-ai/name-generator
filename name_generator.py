from random import randint

adjectives = ["admiring",
		"adoring",
		"agitated",
		"angry",
		"backstabbing",
		"berserk",
		"boring",
		"clever",
		"cocky",
		"compassionate",
		"condescending",
		"cranky",
		"desperate",
		"determined",
		"distracted",
		"dreamy",
		"drunk",
		"ecstatic",
		"elated",
		"elegant",
		"evil",
		"fervent",
		"focused",
		"furious",
		"gloomy",
		"goofy",
		"grave",
		"happy",
		"high",
		"hopeful",
		"hungry",
		"insane",
		"jolly",
		"jovial",
		"kickass",
		"lonely",
		"loving",
		"mad",
		"modest",
		"naughty",
		"nostalgic",
		"pensive",
		"prickly",
		"reverent",
		"romantic",
		"sad",
		"serene",
		"sharp",
		"sick",
		"silly",
		"sleepy",
		"stoic",
		"stupefied",
		"suspicious",
		"tender",
		"thirsty",
		"trusting"]

animals = ["aardvark",
        "albatross",
        "alligator",
        "alpaca",
        "ant",
        "anteater",
        "antelope",
        "ape",
        "armadillo",
        "baboon",
        "badger",
        "barracuda",
        "bat",
        "bear",
        "beaver",
        "bee",
        "bison",
        "boar",
        "buffalo",
        "butterfly",
        "camel",
        "capybara",
        "caribou",
        "cassowary",
        "cat",
        "caterpillar",
        "cattle",
        "chamois",
        "cheetah",
        "chicken",
        "chimpanzee",
        "chinchilla",
        "chough",
        "clam",
        "cobra",
        "cockroach",
        "cod",
        "cormorant",
        "coyote",
        "crab",
        "crane",
        "crocodile",
        "crow",
        "curlew",
        "deer",
        "dinosaur",
        "dog",
        "dogfish",
        "dolphin",
        "donkey",
        "dotterel",
        "dove",
        "dragonfly",
        "duck",
        "dugong",
        "dunlin",
        "eagle",
        "echidna",
        "eel",
        "eland",
        "elephant",
        "elephant-seal",
        "elk",
        "emu",
        "falcon",
        "ferret",
        "finch",
        "fish",
        "flamingo",
        "fly",
        "fox",
        "frog",
        "gaur",
        "gazelle",
        "gerbil",
        "giant-panda",
        "giraffe",
        "gnat",
        "gnu",
        "goat",
        "goose",
        "goldfinch",
        "goldfish",
        "gorilla",
        "goshawk"]

def generate_name():
    return adjectives[randint(0, len(adjectives) - 1)] + "-" + animals[randint(0, len(animals) - 1)]

if __name__ == "__main__":
    print(generate_name())