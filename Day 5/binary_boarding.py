def get_row(rows, characters):
    row_range = [0, rows - 1]
    row = 0
    for char in characters:
        if char == 'F':
            row_range[1] = (row_range[0] + row_range[1]) // 2
            row = row_range[0]
        elif char == 'B':
            row_range[0] = round((row_range[0] + row_range[1]) / 2)
            row = row_range[1]
        else:
            raise NameError('Not a F or B in the chars')
    return row


def get_column(columns, characters):
    column_range = [0, columns - 1]
    column = 0
    for char in characters:
        if char == 'L':
            column_range[1] = (column_range[0] + column_range[1]) // 2
            column = column_range[0]
        elif char == 'R':
            column_range[0] = round((column_range[0] + column_range[1]) / 2)
            column = column_range[1]
        else:
            raise NameError('Not a R or L in the chars')
    return column


highest_seat_id = 0
seat_ids = []
seats = open('input', 'r')

for seat in seats:
    seat = seat.rstrip()
    seat_id = (get_row(128, seat[:7]) * 8) + get_column(8, seat[7:])
    seat_ids.append(seat_id)
    if highest_seat_id < seat_id:
        highest_seat_id = seat_id

print(highest_seat_id)
seat_ids.sort()
for idx, val in enumerate(seat_ids[:-1]):
    if val+1 != seat_ids[idx+1]:
        print(val+1)
