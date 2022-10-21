from datetime import datetime, timedelta
from msvcrt import kbhit, getch
from time import sleep
from typing import List
from winsound import MessageBeep, MB_OK


def main() -> None:
    focus_periods = [25, 25, 25, 25]
    break_periods = [5, 5, 5, 15]
    counter = 0
    while True:
        next_break_time = get_future_time(focus_periods[counter])
        countdown_to("break", next_break_time)
        acknowledge("break", break_periods[counter])
        next_focus_time = get_future_time(break_periods[counter])
        countdown_to("focus", next_focus_time)
        counter = (counter + 1) % len(focus_periods)
        acknowledge("focus", focus_periods[counter])


def get_future_time(minutes: int) -> datetime:
    return datetime.now() + timedelta(minutes=minutes)


def countdown_to(countdown_type: str, next_time: datetime) -> None:
    while datetime.now() < next_time:
        time_until = next_time - datetime.now()
        [minutes, seconds] = parse_timedelta(time_until)
        print(f"{minutes:02d}:{seconds:02d} until next {countdown_type}...", end="\r")
        sleep(0.5)
    end_countdown()


def parse_timedelta(delta: timedelta) -> List[int]:
    minutes = delta.seconds // 60
    seconds = delta.seconds % 60
    return [minutes, seconds]


def end_countdown() -> None:
    flush_input_buffer()
    play_beep()
    for _ in range(2):
        sleep(2)
        play_beep()


def flush_input_buffer():
    while kbhit():
        getch()


def play_beep() -> None:
    MessageBeep(MB_OK)


def acknowledge(period_type: str, minutes: int) -> None:
    input(f"Time for a {minutes}-minute {period_type}! Press ENTER to acknowledge...")


if __name__ == "__main__":
    main()
