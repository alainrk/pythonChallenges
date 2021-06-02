def sort_csv_columns(csv_data):
  rows = [[col for col in row.split(',')] for row in csv_data.split('\n')]
  preSortHeaders = { col: pos for pos, col in enumerate(rows[0]) }
  rows[0].sort()

  # At index i of this array there is index j | j = old_index for that column
  mappingNew2OldIdx = [preSortHeaders[col] for col in rows[0]]
  for idx in range(1, len(rows)):
    row = rows[idx]
    newRow = []
    for newIdx in range(len(row)):
      newRow.append(row[mappingNew2OldIdx[newIdx]])
    rows[idx] = newRow

  return