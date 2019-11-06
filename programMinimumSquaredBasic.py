# import modules
from random import randint

# define functions
def swing():
  drill = randint(1, 4)
  if drill == 1:
    return 'Deadlifts'
  elif drill == 2:
    return 'Dead-stop Swings'
  elif drill == 3:
    return 'Two-hand Swings'
  elif drill == 4:
    return 'One-hand Swings'
  elif drill == 5:
    return 'Hand-to-hand Swings'
  else:
    return 'Double Swings'

def getup():
  drill = randint(1, 4)
  if drill == 1:
    return 'Arm-bars'
  elif drill == 2:
    return 'Floor Presses'
  elif drill == 3:
    return 'Roll-to-elbow Get-ups'
  elif drill == 4:
    return 'Tall-sit Get-ups'
  elif drill == 5:
    return 'Tactical Lunge Get-ups'
  else:
    return 'Full Get-ups'

def bent_press():
  drill = randint(1, 2)
  if drill == 1:
    return 'Bent Arm-bars'
  elif drill == 2:
    return 'Half-kneeling Bent Presses'
  elif drill == 3:
    return 'Low Windmills'
  elif drill == 4:
    return 'High Windmills'
  elif drill == 5:
    return 'Bent Presses'
  else:
    return 'Two Hands Anyhow'

def snatch():
  drill = randint(1, 2)
  if drill == 1:
    return 'One-Hand Swings'
  elif drill == 2:
    return 'High Pulls'
  elif drill == 3:
    return 'Dead-stop Snatches'
  elif drill == 4:
    return 'Tempo Snatches'
  elif drill == 5:
    return 'Heavy Snatches (2-3 reps with a 5 rm size bell)'
  else:
    return 'Double Snatches'

def volume():
  return randint(1, 6) * 2

# main program

day = input('What day is it? (M/T/W/Th/F) ')

print('''\nWarm-up with 1-3 sets of halos, squats, and bridges for 5-10 reps each.\n''')

if day.lower() == 'm' or day.lower() == 'th':
  print(f'Do {swing()} and {getup()} for {volume()} minutes.')
elif day.lower() == 'w':
  print(f'Stretch whatever feels tight for {volume() // 2} minutes.')
else:
  print(f'Do {snatch()} and {bent_press()} for {volume()} minutes each.')

print('''\nSwings and snatches are to be done for 5-10 reps/set. Get-ups and bent presses are to be done for 1-5 reps/set. Arm-bars are to be done for 5 breaths/set ''')