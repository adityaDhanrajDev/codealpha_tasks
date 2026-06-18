"""
BASIC CHATBOT
A simple rule-based chatbot that responds to user inputs.
"""

import random
import time
from datetime import datetime
import string

class SimpleChatbot:
    def __init__(self):
        self.bot_name = "CodeAlphaBot"
        self.running = True
        
        # Define response patterns
        self.responses = {
            # Greetings
            "hello": ["Hi there! 👋", "Hello! 😊", "Hey! How can I help you?", "Greetings! 🌟"],
            "hi": ["Hello! 👋", "Hi there!", "Hey! Nice to see you!"],
            "hey": ["Hey! 👋", "Hello!", "Hi! How are you?"],
            
            # How are you
            "how are you": ["I'm doing great, thanks for asking! 🤖", "I'm fantastic! How about you?", "All systems operational! 😊"],
            "how do you do": ["I'm doing well, thank you!", "Pleased to meet you! I'm functioning perfectly!"],
            
            # Name related
            "your name": [f"My name is {self.bot_name}! 🤖", f"I'm {self.bot_name}, your virtual assistant!", "You can call me CodeAlphaBot!"],
            "who are you": [f"I'm {self.bot_name}, a simple rule-based chatbot!", "I'm your friendly AI assistant!", "I'm a chatbot created to help you!"],
            
            # Feelings
            "i am happy": ["That's wonderful! 😊", "Happiness is contagious!", "I'm glad to hear that! 🎉"],
            "i am sad": ["I'm sorry to hear that. 😔", "Things will get better!", "Want to talk about it? I'm here to listen."],
            "i am good": ["Great to hear! 👍", "Awesome! Keep it up!", "That's fantastic!"],
            "i am fine": ["Good to know! 😊", "Excellent!", "I'm happy you're doing well!"],
            
            # Help
            "help": ["I can respond to greetings, answer basic questions, and chat with you!", 
                    "Try saying: hello, how are you, tell me a joke, what can you do"],
            "what can you do": ["I can chat with you, tell jokes, give you the time, and more!", 
                               "Try asking me for a joke or the current time!"],
            
            # Time
            "time": [],  # Will be filled by get_time method
            "what time is it": [],  # Will be filled by get_time method
            
            # Age
            "how old are you": ["I'm as old as Python itself!", "Age is just a number for AI!", "I was born when you ran this program!"],
            
            # Creator
            "who made you": ["I was created by a talented Python developer!", "My creator is learning Python programming!", "A developer built me for the CodeAlpha internship!"],
            
            # Weather
            "weather": ["I can't check real weather, but I hope it's nice where you are! 🌞", 
                       "I'm not connected to weather services, but stay comfortable!"],
            
            # Goodbye
            "bye": ["Goodbye! 👋", "See you later! 😊", "Take care! 👋", "Bye! Come back soon!"],
            "goodbye": ["Goodbye! 👋", "See you next time!", "Farewell! 😊"],
            "exit": ["Goodbye! 👋", "Exiting now. Take care!"],
            "quit": ["Quitting. Goodbye! 👋", "See you later!"],
            
            # Jokes
            "tell me a joke": [],  # Will be filled by get_joke method
            "joke": []  # Will be filled by get_joke method
        }
        
        # Fallback responses (when no pattern matches)
        self.fallback_responses = [
            "Interesting! Tell me more. 😊",
            "I'm not sure how to respond to that. Could you rephrase?",
            "That's cool! What else would you like to talk about?",
            "Hmm, I'm still learning. Can you ask me something else?",
            f"I'm a simple chatbot. Try asking me 'help' to see what I can do!",
            "That's beyond my knowledge right now. Want to hear a joke instead?"
        ]
        
        self.conversation_history = []
    
    def get_joke(self):
        """Return a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😂",
            "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
            "What do you call a fake noodle? An impasta! 🍝",
            "Why don't eggs tell jokes? They'd crack each other up! 🥚",
            "What's the best thing about Switzerland? I don't know, but the flag is a big plus! 🇨🇭",
            "Why did the bicycle fall over? Because it was two-tired! 🚲",
            "What do you call a bear with no teeth? A gummy bear! 🐻",
            "Why did the math book look so sad? Because it had too many problems! 📚",
            "What do you call a fish wearing a bowtie? So-fish-ticated! 🐟",
            "Why did the coffee file a police report? It got mugged! ☕"
        ]
        return random.choice(jokes)
    
    def get_time(self):
        """Return current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}. ⏰"
    
    def preprocess_input(self, user_input):
        """Clean and prepare user input for matching"""
        # Convert to lowercase
        user_input = user_input.lower().strip()
        # Remove punctuation
        user_input = user_input.translate(str.maketrans('', '', string.punctuation))
        return user_input
    
    def find_best_response(self, user_input):
        """Find the best matching response for user input"""
        processed_input = self.preprocess_input(user_input)
        
        # Check for time-related queries first
        if "time" in processed_input and ("what" in processed_input or "current" in processed_input):
            return self.get_time()
        
        # Check for joke-related queries
        if "joke" in processed_input or "tell me a" in processed_input:
            return self.get_joke()
        
        # Check for exact matches in response patterns
        for pattern, response_list in self.responses.items():
            if pattern in processed_input:
                if response_list:  # If list is not empty
                    return random.choice(response_list)
                else:
                    # Handle empty lists (like time and joke which have special handlers)
                    if pattern == "time" or pattern == "what time is it":
                        return self.get_time()
                    elif pattern == "tell me a joke" or pattern == "joke":
                        return self.get_joke()
        
        # Check for keywords
        keywords = {
            'love': ["Love is beautiful! ❤️", "Aww, that's sweet!", "Love makes the world go round!"],
            'hate': ["I'm sorry to hear that.", "Maybe try to focus on the positive?", "That's unfortunate."],
            'work': ["Work hard, play hard! 💪", "Keep up the great work!", "Don't forget to take breaks!"],
            'sleep': ["Sleep is important! 😴", "Get some rest!", "Sweet dreams!"],
            'food': ["Food is amazing! 🍕", "Now I'm hungry!", "What's your favorite food?"],
            'python': ["Python is awesome! 🐍", "Great choice of programming language!", "Keep coding in Python!"],
            'good': ["I'm glad to hear that! 👍", "That's wonderful!", "Awesome!"],
            'bad': ["Sorry to hear that. Hope things get better! 🌈", "Tomorrow is a new day!", "Stay positive!"]
        }
        
        for keyword, responses in keywords.items():
            if keyword in processed_input:
                return random.choice(responses)
        
        # No match found - return fallback response
        return random.choice(self.fallback_responses)
    
    def display_banner(self):
        """Display welcome banner"""
        print("\n" + "="*60)
        print(f"🤖 WELCOME TO {self.bot_name.upper()} 🤖")
        print("="*60)
        print("I'm a simple rule-based chatbot!")
        print("Try talking to me - I understand greetings, questions, and more!")
        print("\n💡 Quick commands:")
        print("   • 'help' - See what I can do")
        print("   • 'tell me a joke' - Hear a joke")
        print("   • 'time' - Get current time")
        print("   • 'bye' - Exit the chat")
        print("="*60)
    
    def typing_animation(self):
        """Simulate typing animation"""
        print("🤖 ", end="", flush=True)
        for _ in range(3):
            time.sleep(0.2)
            print(".", end="", flush=True)
        time.sleep(0.2)
        print()
    
    def run(self):
        """Main chatbot loop"""
        self.display_banner()
        
        # Welcome message
        print(f"\n{self.bot_name}: Hello! I'm {self.bot_name}. Type 'bye' to exit.\n")
        
        while self.running:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Check for empty input
                if not user_input:
                    continue
                
                # Add to conversation history
                self.conversation_history.append(f"You: {user_input}")
                
                # Check for exit commands
                if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
                    response = random.choice(self.responses['bye'])
                    print(f"\n{self.bot_name}: {response}")
                    print("\n" + "="*40)
                    print("📊 Chat Session Summary:")
                    print(f"   Total exchanges: {len(self.conversation_history)}")
                    print("="*40)
                    break
                
                # Get bot response
                self.typing_animation()
                response = self.find_best_response(user_input)
                
                # Display response
                print(f"{self.bot_name}: {response}\n")
                
                # Add to conversation history
                self.conversation_history.append(f"{self.bot_name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.bot_name}: Goodbye! Thanks for chatting! 👋")
                break
            except Exception as e:
                print(f"\n{self.bot_name}: Oops! Something went wrong. Let's continue chatting! 😊")
                print(f"Error: {e}")

# Run the chatbot
if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.run()
