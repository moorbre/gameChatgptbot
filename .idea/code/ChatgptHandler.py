from openai import OpenAI
import configparser
import random

#approx cost of an excuse = $0.00008, my $5 62,500 excuses
class ChatgptHandler:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../config/config.ini')
        self.api_key = config['openai']['api_key']
        self.client = OpenAI(
            api_key = self.api_key,
        )
        self.default_model = "gpt-3.5-turbo-1106" ##"gpt-4-1106-preview"
        self.default_temperature = 1.2 # default is 1, setting too high can take too long. Effectively changes the randomeness
        self.persona_list = ['someone who can only communicate in rhyme','a regular person', 'trump', 'an egirl', 'a really sarcastic person']
    def refresh_client(self):
        print("refreshing client")
        self.client = OpenAI(
            api_key = self.api_key,
        )
    def cs2_died_excuse(self):
        blame_targets = ["my teammates","my marriage", "my son", "W.O.M.B.L.E", "womble", "my equipment", "the economy", "the enemy whilst complimenting them", "myself from wasting time writing up excuses", "pay to win mechanics", "my upbringing", "the schools",
                         "my incredible ability to fumble in any situation", "boomers", "gen z", "literally anything unrelated to the game", "I thought I was playing valorant", "my low self esteem",
                         "the fragility of human life", "my ego", "lack of moral support", "capitalism", "being busy eating a random messy snack", "barry buying a scout"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "limit your answers to a couple of sentences "}, # + "and answer in the persona of " + random.choice(self.persona_list)},
                {"role": "user", "content": "create a phrase that is an excuse on why you failed to win a 1v1 in counter strike, make it very obscure. Start the phrase with I only died because."},
                #{"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure and blame " + random.choice(blame_targets)}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)

    def cs2_survived_excuse(self):
        blame_targets = ["my teammates","my marriage", "my son", "my equipment", "the economy", "the enemy whilst complimenting them", "discord", "skype", "literally anything unrelated to the game", "moral support", "the enemy's incompetence", "pay to win mechanics"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "limit your answers to a couple of sentences "}, # + "and answer in the persona of " + random.choice(self.persona_list)},
                {"role": "user", "content": "create a phrase that is a reason why you survied a round in counter strike, make it very obscure."},
               # {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure and the reason I survived was because of " + random.choice(blame_targets)}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)
    def cs2_sean_excuse2(self):
        blame_targets = ["his teammates","his relationship status", "W.O.M.B.L.E", "womble", "his equipment", "the economy", "the enemy whilst complimenting them", "pay to win mechanics", "his upbringing", "the schools",
                         "his incredible ability to fumble in any situation", "literally anything unrelated to the game", "He thought he was playing fall guys", "his low self esteem",
                         "the fragility of human life", "his ego", "lack of moral support", "capitalism", "being busy eating a random messy snack", "barry buying a scout", "he's too busy setting up his soundboard",
                         "what you see is what you get", "his obsession with butter chicken", "he forgot whether he is a shawn or a sean", "the IRA"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "speak in uwu speak "}, # + "and answer in the persona of " + random.choice(self.persona_list)},
                {"role": "user", "content": "create a phrase that is a reason why sean wasn't performing in counter strike."},
                # {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure and the reason sean couldn't perform was because of " + random.choice(blame_targets)}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)


    def cs2_sean_excuse(self):
        blame_targets = ["his teammates","his relationship status", "W.O.M.B.L.E", "womble", "his equipment", "the economy", "the enemy whilst complimenting them", "pay to win mechanics", "his upbringing", "the schools",
                         "his incredible ability to fumble in any situation", "literally anything unrelated to the game", "He thought he was playing fall guys", "his low self esteem",
                         "the fragility of human life", "his ego", "lack of moral support", "capitalism", "being busy eating a random messy snack", "barry buying a scout", "he's too busy setting up his soundboard",
                         "what you see is what you get", "his obsession with butter chicken", "he forgot whether he is a shawn or a sean", "the IRA"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                #{"role": "system", "content": "speak in uwu speak "}, # + "and answer in the persona of " + random.choice(self.persona_list)},
                {"role": "user", "content": "create an acronym with the letters D.A.Y.B.R.E.A.K.E.R that is stands for amazing gaming skills, start the answer with Daybreaker stands for :"},
                # {"role": "user", "content": "make itudw even more obscure"},
                #{"role": "user", "content": "make it even more obscure and the reason sean couldn't perform was because of " + random.choice(blame_targets)}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)
    def dota2_died_excuse(self):
        blame_targets = ["my teammates","my marriage", "my son", "my equipment", "physics", "the enemy whilst complimenting them", "myself from wasting time writing up excuses", "my upbringing", "the schools", "literally anything unrelated to the game"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                #{"role": "system", "content": "You can only respond in 130 characters or less"},
                {"role": "user", "content": "create a phrase that is an excuse on why you died in a game of dota2, make it very obscure. Start the phrase with I only died because."},
                {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure and blame " + random.choice(blame_targets)}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)


    def rocketleague_scored(self):
        despite_targets = ["my teammates","my marriage", "my son", "my equipment", "the economy", "the enemy whilst complimenting them", "myself from wasting time writing up excuses", "discord", "skype", "my upbringing", "the schools",
                           "my incredible ability to fumble in any situation", "boomers", "gen z", "literally anything unrelated to the game", "I thought I was playing fifa", "my low self esteem",
                           "the fragility of human life", "my ego", "lack of moral support", "capitalism", "being busy eating a random messy snack"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "You can only respond in 200 characters or less"},
                {"role": "user", "content": "create a phrase celebrating our goal in rocket league"},
                {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure and add in that is was despite " + random.choice(despite_targets) + ""}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)

    def rocketleague_scored_against(self):
        blame_targets = ["my teammates","my marriage", "my son", "my equipment", "the economy", "the enemy whilst complimenting them", "myself from wasting time writing up excuses", "discord", "skype", "my upbringing", "the schools",
                         "my incredible ability to fumble in any situation", "boomers", "gen z", "literally anything unrelated to the game", "I thought I was playing fifa", "my low self esteem",
                         "the fragility of human life", "my ego", "lack of moral support", "capitalism", "being busy eating a random messy snack"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "You can only respond in 200 characters or less"},
                {"role": "user", "content": "create a phrase making an excuse of why we got scored on in rocket league"},
                {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure and add in that is was despite " + random.choice(blame_targets) + ""}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)

    def rocketleague_phrase(self):
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                #{"role": "system", "content": "You can only respond in 200 characters or less"},
                {"role": "user", "content": "create a short quick chat message for rocket league, make it similar but not the same to the real rocket league quick chat messages "},
                {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure"}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)

    def pause_phrase(self):
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                #{"role": "system", "content": "You can only respond in 200 characters or less"},
                {"role": "user", "content": "create a message venting frustration of a game being paused"},
                {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure"}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)

    def funfact_phrase(self):
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "You can only respond in 300 characters or less"},
                {"role": "user", "content": "give me a fun fact"},
                {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure"}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)
    def wife_message(self):
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "You can only respond in 500 characters or less"},
                {"role": "user", "content": "write a message to my wife telling her how much I love her"},
                {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure"}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)

    def clean_text(self, text):
        if text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        elif text.startswith("'") and text.endswith("'"):
            return text[1:-1]
        else:
            return text