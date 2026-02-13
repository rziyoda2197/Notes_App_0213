from storage import load_notes, save_notes


def add_note():
    title = input("Title: ")
    content = input("Content: ")

    notes = load_notes()
    notes.append({
        "title": title,
        "content": content
    })

    save_notes(notes)
    print("Note saved ✅")


def show_notes():
    notes = load_notes()
    if not notes:
        print("No notes")
        return

    for i, note in enumerate(notes, 1):
        print(f"\n{i}. {note['title']}")
        print(note['content'])


def delete_note():
    notes = load_notes()
    show_notes()

    index = int(input("\nDelete number: ")) - 1

    if 0 <= index < len(notes):
        notes.pop(index)
        save_notes(notes)
        print("Deleted 🗑")
    else:
        print("Wrong index")


def search_note():
    word = input("Search: ").lower()
    notes = load_notes()

    for note in notes:
        if word in note["title"].lower() or word in note["content"].lower():
            print(f"\n{note['title']}")
            print(note['content'])
