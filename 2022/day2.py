ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

def rock_paper_scissors_part1(theirs, mine):
  # theirs: A - Rock, B - Paper, C - Scissors
  # mine:   X - Rock, Y - Paper, Z - Scissors
  choice = 0
  result = LOSE
  if mine == "X":
    choice = ROCK
    if theirs == "C":
      result = WIN
    elif theirs == "A":
      result = DRAW
  elif mine == "Y":
    choice = PAPER
    if theirs == "A":
      result = WIN
    elif theirs == "B":
      result = DRAW
  elif mine == "Z":
    choice = SCISSORS
    if theirs == "B":
      result = WIN
    elif theirs == "C":
      result = DRAW
  return choice + result

def rock_paper_scissors_part2(theirs, mine):
  # theirs: A - Rock, B - Paper, C - Scissors
  # mine:   X - Lose, Y - Draw,  Z - Win
  choice = 0
  result = LOSE
  if mine == "X":
    if theirs == "A":
      choice = SCISSORS
    elif theirs == "B":
      choice = ROCK
    else:
      choice = PAPER
  elif mine == "Y":
    result = DRAW
    if theirs == "A":
      choice = ROCK
    elif theirs == "B":
      choice = PAPER
    else:
      choice = SCISSORS
  elif mine == "Z":
    result = WIN
    if theirs == "A":
      choice = PAPER
    elif theirs == "B":
      choice = SCISSORS
    else:
      choice = ROCK
  return choice + result

input = open("input.txt", "r").read().splitlines()

score_part1 = 0
score_part2 = 0

for line in input:
  theirs, mine = line.split()
  score_part1 = score_part1 + rock_paper_scissors_part1(theirs, mine)
  score_part2 = score_part2 + rock_paper_scissors_part2(theirs, mine)

print("Part1: " + str(score_part1))
print("Part2: " + str(score_part2))
