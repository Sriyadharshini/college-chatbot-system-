
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
guestbot = ChatBot(name='guestBot',read_only=True)
guest=open(r'C:\Users\ELCOT\chatbot\chatrbot\guest.txt','r')
List=guest.readlines()
newList=[line.strip() for line in List]
 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(guestbot)
trainer.train(conversation)
trainer.train(newList)
newList=[line.strip() for line in List]
# Training with English Corpus Data 
 
 
'''
trainer_corpus = ChatterBotCorpusTrainer(guestbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)'''
staffbot = ChatBot(name='staffBot',read_only=True)
staff=open(r'C:\Users\ELCOT\chatbot\chatrbot\staff.txt','r')
List=staff.readlines()
newList=[line.strip() for line in List]

 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(staffbot)
trainer.train(conversation)
trainer.train(newList)
newList=[line.strip() for line in List]
# Training with English Corpus Data 
'''
trainer_corpus = ChatterBotCorpusTrainer(staffbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) '''
parentbot = ChatBot(name='parentBot',read_only=True)
parent=open(r'C:\Users\ELCOT\chatbot\chatrbot\parent.txt','r')
List=parent.readlines()
newList=[line.strip() for line in List]

 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(parentbot)
#trainer.train(conversation)

trainer.train(newList)
newList=[line.strip() for line in List]
print(newList[:5])
# Training with English Corpus Data 
'''trainer_corpus = ChatterBotCorpusTrainer(parentbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) '''


studentbot = ChatBot(name='studentBot',storage_adapter='chatterbot.storage.SQLStorageAdapter',logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'threshold': 0.25,
            'default_response': 'i couldnt understand'
        }],read_only=True)
student=open(r'C:\Users\ELCOT\chatbot\chatrbot\student.txt','r')
List=student.readlines()
newList=[line.strip() for line in List]
#Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(studentbot)
trainer.train(conversation)
trainer.train(newList)
newList=[line.strip() for line in List]
#Training with English Corpus Data 
#trainer_corpus = ChatterBotCorpusTrainer(studentbot)
#trainer_corpus.train(
#    'chatterbot.corpus.english'
#) 

