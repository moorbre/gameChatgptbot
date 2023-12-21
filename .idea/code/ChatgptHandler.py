from openai import OpenAI
import random

#approx cost of an excuse = $0.00008, my $5 62,500 excuses
class ChatgptHandler:

    def __init__(self):
        self.api_key = ''
        self.client = OpenAI(
            api_key = self.api_key,
        )
        self.default_model = "gpt-3.5-turbo-1106" ##"gpt-4-1106-preview"
        self.default_temperature = 1.2 # default is 1, setting too high can take too long. Effectively changes the randomeness

    def refresh_client(self):
        print("refreshing client")
        self.client = OpenAI(
            api_key = self.api_key,
        )
    def cs2_died_excuse(self):
        blame_targets = ["my teammates","my wife", "my son", "W.O.M.B.L.E", "womble", "my equipment", "the economy", "the enemy whilst complimenting them", "myself from wasting time writing up excuses", "discord", "skype", "my upbringing", "the schools",
                         "my incredible ability to fumble in any situation", "bee movie", "boomers", "gen z", "the price of bitcoin", "literally anything unrelated to the game", "I thought I was playing valorant", "my low self esteem",
                         "the fragility of human life", "my ego", "lack of moral support", "capitalism"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "limit your answers to a couple of sentences"},
                {"role": "user", "content": "create a phrase that is an excuse on why you failed to win a 1v1 in counter strike, make it very obscure. Start the phrase with I only died because."},
                #{"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure and blame " + random.choice(blame_targets)}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)

    def cs2_survived_excuse(self):
        blame_targets = ["my teammates","my wife", "my son", "my equipment", "the economy", "the enemy whilst complimenting them", "discord", "skype", "literally anything unrelated to the game", "moral support", "the enemy's incompetence"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "limit your answers to a couple of sentences"},
                {"role": "user", "content": "create a phrase that is a reason why you survied a round in counter strike, make it very obscure."},
               # {"role": "user", "content": "make it even more obscure"},
                {"role": "user", "content": "make it even more obscure and the reason I survived was because of " + random.choice(blame_targets)}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)


    def dota2_died_excuse(self):
        blame_targets = ["my teammates","my wife", "my son", "my equipment", "physics", "the enemy whilst complimenting them", "myself from wasting time writing up excuses", "my upbringing", "the schools", "literally anything unrelated to the game"]
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


    def rocketleague_scored_verbose(self):
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                #{"role": "system", "content": "You can only respond in 130 characters or less"},
                {"role": "user", "content": "create a phrase that is very verbose, that states that we have iterated our score by 1 and therefore have brought our team closer to winning in rocket league"}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)

    def rocketleague_scored_against_verbose(self):
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                #{"role": "system", "content": "You can only respond in 130 characters or less"},
                    {"role": "user", "content": "create a phrase that is very verbose, that states that the opposing team have iterated their score by 1 and therefore have brought their team closer to winning in rocket league"}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)


    def rocketleague_scored(self):
        despite_targets = ["my teammates","my wife", "my son", "my equipment", "the economy", "the enemy whilst complimenting them", "skype", "my upbringing", "the schools", "literally anything unrelated to the game", "my low self esteem"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "You can only respond in 200 characters or less"},
                {"role": "user", "content": "create a phrase celebrating our goal in rocket league"},
                {"role": "user", "content": "make it even more obscure and add in that is was despite " + random.choice(despite_targets) + ""},
                {"role": "user", "content": "make it even more obscure"}
            ]
        )
        print(response.choices[0].message.content)
        return self.clean_text(response.choices[0].message.content)

    def rocketleague_scored_against(self):
        blame_targets = ["my teammates","my wife", "my son", "my equipment", "the economy", "the enemy whilst complimenting them", "myself from wasting time writing up excuses", "discord", "skype", "my upbringing", "the schools", "my upbringing", "the schools", "literally anything unrelated to the game", "my low self esteem", "psyonix", "my boomer skills", "my incredible ability to fumble in any situation"]
        response = self.client.chat.completions.create(
            model=self.default_model,
            temperature=self.default_temperature,
            messages=[
                {"role": "system", "content": "You can only respond in 200 characters or less"},
                {"role": "user", "content": "create an excuse for why we just got scored on in rocket league , make to sure blame " + random.choice(blame_targets)},
                {"role": "user", "content": "make it even more obscure"}
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

    def clean_text(self, text):
        if text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        elif text.startswith("'") and text.endswith("'"):
            return text[1:-1]
