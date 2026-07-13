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


def show_movies(title, movies):
    print(f"\n{title}")
    print("-" * len(title))
    for movie in movies:
        print("•", movie)


def continue_chat():
    while True:
        choice = (
            input("\nWould you like another recommendation? (yes/no): ").strip().lower()
        )
        if re.fullmatch(r"(yes|y)", choice):
            return True
        elif re.fullmatch(r"(no|n)", choice):
            return False
        else:
            print("Please enter yes or no.")


print("=" * 50)
print("🎬 Welcome to MovieBot 🎬")
print("=" * 50)

name = input("MovieBot: Hi! What's your name?\nYou: ").strip().title()
print(f"\nMovieBot: Nice to meet you, {name}! 😊")

while True:

    print("\nHow can I help you?")
    print("1. Recommend by Genre")
    print("2. Recommend by Language")
    print("3. Recommend by Actor")
    print("4. Top Rated Movies")
    print("5. Similar Movies")
    print("6. Exit")

    choice = input("\nEnter your choice: ").strip().lower()

    if re.fullmatch(r"(1|genre)", choice):

        genre = (
            input("Enter a genre (Action, Comedy, Horror, Romance, Thriller, Sci-Fi): ")
            .strip()
            .lower()
        )

        if re.search(r"action", genre):
            show_movies("Action Movies", genres["action"])

        elif re.search(r"comedy", genre):
            show_movies("Comedy Movies", genres["comedy"])

        elif re.search(r"horror", genre):
            show_movies("Horror Movies", genres["horror"])

        elif re.search(r"romance", genre):
            show_movies("Romance Movies", genres["romance"])

        elif re.search(r"thriller", genre):
            show_movies("Thriller Movies", genres["thriller"])

        elif re.search(r"sci[- ]?fi", genre):
            show_movies("Sci-Fi Movies", genres["sci-fi"])

        else:
            print("Genre not found.")

    elif re.fullmatch(r"(2|language)", choice):

        lang = (
            input("Enter a language (English, Hindi, Malayalam, Tamil): ")
            .strip()
            .lower()
        )

        if lang in languages:
            show_movies(f"{lang.title()} Movies", languages[lang])
        else:
            print("Language not found.")

    elif re.fullmatch(r"(3|actor)", choice):

        actor = input("Enter actor name: ").strip().lower()

        if actor in actors:
            show_movies(f"Movies starring {actor.title()}", actors[actor])
        else:
            print("Actor not found.")

    elif re.fullmatch(r"(4|top)", choice):
        show_movies("Top Rated Movies", top_movies)

    elif re.fullmatch(r"(5|similar)", choice):

        movie = input("Enter a movie you liked: ").strip().lower()

        if movie in similar_movies:
            show_movies("You may also like", similar_movies[movie])
        else:
            print("Sorry! No similar movies found.")

    elif re.fullmatch(r"(6|exit|bye|quit)", choice):
        print(f"\nMovieBot: Goodbye {name}! Happy Watching! 🍿")
        break

    else:
        print("Invalid choice.")
        continue

    if not continue_chat():
        print(f"\nMovieBot: Goodbye {name}! Happy Watching! 🍿")
        break
