import time
import sys
import winsound

try:
    print("                                                             Python Timer")
    print()
    user = input("Set the Timer(Ex 15:30) :- ")
    print()
    print()

    if (":" in user):
        user1 = user.split(':')
        mi = int(user1[0])
        sec = int(user1[1])
        t_sec = (mi*60) + sec

        while t_sec > 0:
            mint = int(t_sec / 60)
            second = t_sec % 60

            sys.stdout.write("\033[F")  # Move cursor up one line
            sys.stdout.write("\033[K")  # Clear line
            sys.stdout.flush()          # Force it to update

            if second < 10:
                print("                                      " + str(mint) + ":0" + str(second))
                if t_sec <= 10:
                    winsound.Beep(450, 250)
                else:
                    winsound.Beep(300, 200)
            else:
                print("                                      " + str(mint) + ":" + str(second))
                winsound.Beep(300, 200)

            time.sleep(0.8)
            t_sec -= 1

        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear line
        sys.stdout.flush()          # Force it to update

        print("                                      " + "0:00")
        winsound.Beep(1800, 800)
        print("=====================================================================================")
    else:
        print("Wrong Timer!")

    input()

except Exception:
    print("Wrong Timer!")