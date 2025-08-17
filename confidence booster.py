import random
import time

def confidence_booster():
    # Motivational quotes
    quotes = [
        "Believe in yourself and all that you are!",
        "You are capable of amazing things.",
        "Every day is a chance to get better.",
        "Your potential is endless.",
        "Confidence comes from practice, not perfection."
    ]

    # Eye contact practice tips
    exercises = [
        "Look into the mirror and maintain eye contact with yourself for 30 seconds.",
        "When talking to someone, focus on their eyes for 3-5 seconds before looking away.",
        "Practice smiling while making eye contact.",
        "Imagine you are talking to your best friend—it makes eye contact natural.",
        "During conversations, glance at the eyes, then nose, then mouth—it reduces pressure."
    ]

    print("🌟 Welcome to the Confidence Booster App 🌟\n")
    while True:
        print("Choose an option:")
        print("1. Get a motivational quote")
        print("2. Practice eye contact tip")
        print("3. Daily confidence challenge")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            print("\n💡 " + random.choice(quotes) + "\n")
        
        elif choice == "2":
            print("\n👀 " + random.choice(exercises) + "\n")
        
        elif choice == "3":
            print("\n🔥 Your challenge: ")
            print("For the next 5 minutes, maintain eye contact with someone you talk to,")
            print("and remind yourself: 'I am confident and calm.'\n")
            for i in range(5, 0, -1):
                print(f"⏳ Challenge time: {i} minutes left...")
                time.sleep(1)  # You can change this to time.sleep(60) for real minutes
            print("\n✅ Challenge complete! You did it!\n")

        elif choice == "4":
            print("\nThank you for using Confidence Booster App! Stay confident! 💪")
            break
        else:
            print("\n⚠️ Invalid choice. Try again.\n")


# Run the app
if __name__ == "__main__":
    confidence_booster()
