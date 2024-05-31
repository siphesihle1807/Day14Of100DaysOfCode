#Creating a higher lower game 
import random 
import os

oomf_data = [
    {
        'xhandle': '@sipheshezie',
        'follower_count': 14.5,
        'known_for': 'Switch and coding',

    },
    {
        'xhandle': 'Kylie Jenner',
        'follower_count': 172,
        'known_for': 'Reality TV personality and businesswoman and Self-Made Billionaire',
 
    },
    {
        'xhandle': 'Kim Kardashian',
        'follower_count': 167,
        'known_for': 'Reality TV personality and businesswoman',

    },
    {
        'xhandle': 'Lionel Messi',
        'follower_count': 149,
        'known_for': 'Footballer',
 
    },
    {
        'xhandle': 'Beyoncé',
        'follower_count': 145,
        'known_for': 'Musician',
    
    },
    {
        'xhandle': 'Neymar',
        'follower_count': 138,
        'known_for': 'Footballer',
    },
    {
        'xhandle': 'National Geographic',
        'follower_count': 135,
        'known_for': 'Magazine',
    },
    {
        'xhandle': 'Justin Bieber',
        'follower_count': 133,
        'known_for': 'Musician',
    },
    {
        'xhandle': 'Taylor Swift',
        'follower_count': 131,
        'known_for': 'Musician',
    },
    {
        'xhandle': 'Kendall Jenner',
        'follower_count': 127,
        'known_for': 'Reality TV personality and Model',
    },
    {
        'xhandle': 'Jennifer Lopez',
        'follower_count': 119,
        'known_for': 'Musician and actress',
    },
    {
        'xhandle': 'Nicki Minaj',
        'follower_count': 113,
        'known_for': 'Musician',
    },
    {
        'xhandle': 'Nike',
        'follower_count': 109,
        'known_for': 'Sportswear multinational',

    },
    {
        'xhandle': 'Khloé Kardashian',
        'follower_count': 108,
        'known_for': 'Reality TV personality and businesswoman',
    },
    {
        'xhandle': 'Miley Cyrus',
        'follower_count': 107,
        'known_for': 'Musician and actress',

    },
    
]



higher_lower = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def random_oomf():
    return random.choice(oomf_data)

def play():
    print(higher_lower)
    score = 0
    oomf_a = random_oomf()
    oomf_b = random_oomf()

    while oomf_a == oomf_b:
        oomf_b = random_oomf()
        #this ensures that there are not the same oomf or data. 

    while True:
     
        print(f"Compare oomf A: {oomf_a['xhandle']}, known for {oomf_a['known_for']}")
        print(vs)
        print(f"Against oomf B: {oomf_b['xhandle']}, known for {oomf_b['known_for']}")

        user_guess = input("Who has many followers? Type 'A' or 'B': ")
        if (user_guess == 'A' and oomf_a['follower_count'] > oomf_b['follower_count']) or (user_guess == 'B' and oomf_b['follower_count'] > oomf_a['follower_count']):
            score +=1
            print(f"Correct!")
            oomf_a = oomf_b
            oomf_b = random_oomf()
            while oomf_a == oomf_b :
                oomf_b = random_oomf()

        else:
            print(f"Oops, that's incorrect. Here's your final score: {score}.")
            break

def play_again():
    while True:
        command = 'cls' if os.name == 'nt' else 'clear'
        os.system(command)
        play()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("The game has ended. Bye, bye!")
            break


play_again()