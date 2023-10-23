def sing_the_song(notes_list, singed_notes_list, start_note_index):
    number_of_notes = len(notes_list)

    song = [notes_list[start_note_index]]
    current_note_index = start_note_index

    for new_note_index in singed_notes_list:
        current_note_index = (current_note_index + new_note_index) % number_of_notes
        song.append(notes_list[current_note_index])

    return song


def main():
    notes_list_size = int(input('Enter size of notes list: '))
    notes_list = [str(input('Enter a value: ')) for _ in range(notes_list_size)]

    singed_notes_list_size = int(input('Enter size of notes singed list: '))
    singed_notes_list = [int(input('Enter a value: ')) for _ in range(singed_notes_list_size)]

    start_note_index = int(input('Enter index of starting note: '))

    song = sing_the_song(notes_list, singed_notes_list, start_note_index)

    print(song)


if __name__ == "__main__":
    main()
