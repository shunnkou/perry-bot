import chatterbot
from chatterbot import ChatBot, comparisons, response_selection
from chatterbot.trainers import ChatterBotCorpusTrainer


bot = ChatBot(
    'Bot Boy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
    ],
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90

        },
        {
            "import_path": "chatterbot.logic.TimeLogicAdapter"
        }
    ],
    statement_comparison_function= chatterbot.comparisons.levenshtein_distance,
    response_selection_method = chatterbot.response_selection.get_first_response,
    read_only=False
)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.botprofile",
    "chatterbot.corpus.english.ai",
    "chatterbot.corpus.english.computers",
    "chatterbot.corpus.english.emotion",
    "chatterbot.corpus.english.food",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.health",
    "chatterbot.corpus.english.history",
    "chatterbot.corpus.english.humor",
    "chatterbot.corpus.english.literature",
    "chatterbot.corpus.english.politics",
    "chatterbot.corpus.english.science",
    "chatterbot.corpus.english.trivia",
    "chatterbot.corpus.english.psychology",
)

print("Train complete.")