import re

genres = {
    "action": ["John Wick", "Mad Max: Fury Road", "Extraction"],
    "comedy": ["The Hangover", "Superbad", "Jumanji: Welcome to the Jungle"],
    "horror": ["The Conjuring", "Talk to Me", "Hereditary"],
    "romance": ["La La Land", "The Notebook", "Me Before You"],
    "thriller": ["Se7en", "Gone Girl", "Prisoners"],
    "sci-fi": ["Interstellar", "Inception", "The Martian"],
}

languages = {
    "english": ["Inception", "John Wick", "Interstellar"],
    "hindi": ["3 Idiots", "Dangal", "Zindagi Na Milegi Dobara"],
    "malayalam": ["Aavesham", "Manjummel Boys", "Premalu"],
    "tamil": ["Leo", "Vikram", "Kaithi"],
}

actors = {
    "tom cruise": ["Top Gun: Maverick", "Mission Impossible: Dead Reckoning"],
    "leonardo dicaprio": ["Inception", "Titanic", "The Wolf of Wall Street"],
    "shah rukh khan": ["Jawan", "Pathaan", "My Name Is Khan"],
}

similar_movies = {
    "interstellar": ["Inception", "Arrival", "The Martian"],
    "inception": ["Interstellar", "Tenet", "Shutter Island"],
    "john wick": ["Nobody", "Extraction", "The Equalizer"],
}

top_movies = ["The Shawshank Redemption", "The Dark Knight", "The Godfather"]

name = ""


def show_movies(title, movies):
    print(f"\n{title}")
    print("-" * len(title))
    for movie in movies:
        print("•", movie)


print("=" * 55)
print("🎬 Welcome to MovieBot 🎬")
print("=" * 55)

while True:

    user = input("\nYou: ").strip().lower()

    # Greeting
    if re.search(r"\b(hi|hello|hey)\b", user):
        print("\nMovieBot: Hello! 👋")

        if not name:
            n = input("MovieBot: What's your name?\nYou: ").strip()
            name = n.title()
            print(f"MovieBot: Nice to meet you, {name}! 😊")

        print("""
I can help you with:
• Recommend movies by genre
• Recommend movies by language
• Recommend movies by actor
• Top Rated Movies
• Similar Movies

Just type something like:
- I want action movies
- Recommend Malayalam movies
- Movies with Tom Cruise
- Top rated movies
- I liked Interstellar
""")

    # Genre
    elif re.search(r"\b(action|comedy|horror|romance|thriller|sci[- ]?fi)\b", user):

        if re.search(r"sci[- ]?fi", user):
            key = "sci-fi"
        else:
            key = re.search(r"action|comedy|horror|romance|thriller", user).group()

        show_movies(f"{key.title()} Movies", genres[key])

    # Language
    elif re.search(r"\b(english|hindi|malayalam|tamil)\b", user):
        lang = re.search(r"english|hindi|malayalam|tamil", user).group()
        show_movies(f"{lang.title()} Movies", languages[lang])

    # Actor
    elif re.search(r"movies? with (.+)", user):
        actor = re.search(r"movies? with (.+)", user).group(1).strip()

        if actor in actors:
            show_movies(f"Movies starring {actor.title()}", actors[actor])
        else:
            print("MovieBot: Sorry! I don't know that actor.")

    # Top movies
    elif re.search(r"\b(top rated|top movies|best movies)\b", user):
        show_movies("Top Rated Movies", top_movies)

    # Similar movies
    elif re.search(r"i liked (.+)", user):
        movie = re.search(r"i liked (.+)", user).group(1).strip()

        if movie in similar_movies:
            show_movies("You may also like", similar_movies[movie])
        else:
            print("MovieBot: Sorry! I don't have recommendations for that movie.")

    # Thanks
    elif re.search(r"\b(thanks|thank you)\b", user):
        print("MovieBot: You're welcome! 😊")

    # Exit
    elif re.search(r"\b(bye|exit|quit|goodbye)\b", user):
        print(f"MovieBot: Goodbye {name if name else ''}! Happy Watching! 🍿")
        break

    # Unknown
    else:
        print("""MovieBot:
Sorry, I didn't understand that.

Try asking:
• I want action movies
• Recommend Malayalam movies
• Movies with Tom Cruise
• Top rated movies
• I liked Interstellar
""")
