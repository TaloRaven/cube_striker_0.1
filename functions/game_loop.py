#!/usr/bin/env python3
from src.functions.next_wave import next_wave
from src.classess.Level import Level
from src.functions.utlis import cls, query_yes_no
from colorama import init, Fore
init(autoreset=True)
from colorama import init

init(autoreset=True)

def game_loop():
    lvl = 0
    level = Level(lvl)
    game_state = 'active'
    level, game_state = next_wave(level, game_state)
    print(f'''
              Goal of the game survive as long as you can
              You can break cubes only if at least 2 of them are same color,
              you get score for breaking yellow blocks,
              the more adjusted yellow blocks are, the bigger score reward
              Good luck !
              ''')
    input('press enter to start ')

    while game_state == 'active':
        print(f'Round {lvl + 1}')
        print(f'Wave {level.grid.current_wave} / {level.mine.mine_len}   Total Score: {level.grid.total_score} ')
        level.grid.display_grid()
        player_input = input()

        if player_input == '/exit':
            game_state = 'game_over'
        if player_input == '':
            level, game_state = next_wave(level, game_state)

        else:
            try:
                level.grid = level.grid.break_group(int(player_input))
            except:
                print('')

        if level.grid.grid[-1][-1].colour != Fore.WHITE:
            gamestate = 'break'

        if game_state == 'level_complited':
            print(f"""
                ===============================Round {lvl} COMPLITED  =========================
                ===============================================================================

                Current  score {level.grid.total_score}""")

            input('press enter to contiunue')
            lvl = lvl + 1
            total_score = level.grid.total_score
            level = Level(lvl)
            level.grid.total_score = total_score
            game_state = 'active'
        if game_state == 'game_over':
            print(f"""
                    Game Over
                    Best Round {lvl}
                    Total Score {level.grid.total_score}
            """)
            question = query_yes_no('Play aagain ?')
            if question:
                game_state = 'active'
                lvl = 0
                level = Level(lvl)
