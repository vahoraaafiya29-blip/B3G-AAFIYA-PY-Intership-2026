library={101:{"title":"phython Basics","author":"john","copies":5},
         102:{"title":"Data Science","author":"Alice","copies":3},
         103:{"title":"AI Guide","author":"Bob","copies":4}
        }

book_id=102

if book_id in library and library[book_id]["copies"]>0:
    library[book_id]["copies"]-=1

    print(library)