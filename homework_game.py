import tkinter as tk
import random as rnd
import time

lives_amount = 5
opp_lives_amount = 5

window = tk.Tk()
window.title("Камень, ножницы, бумага")
window.geometry("400x380")
window.resizable(False, False)
def create_frame():
    frame = tk.Frame(window)
    def current_lives(liv_amount):
        result = ""
        while liv_amount >= 1:
            result += '♡'
            liv_amount = liv_amount - 1
        return result
    def opp_current_lives(liv_amount):
        result = ""
        while liv_amount >= 1:
            result += '♥'
            liv_amount = liv_amount - 1
        return result

    def compare_picks(pl_pick, opp_pick):
        global lives_amount
        global opp_lives_amount
        if pl_pick == opp_pick:
            compare_result = "Ничья!"
            return compare_result
        elif pl_pick == 1 and opp_pick == 3 or pl_pick > opp_pick:
            compare_result = "Вы проиграли!"
            lives_amount = lives_amount - 1
            hearts.config(text = f"Жизней:  {current_lives(lives_amount)}")
            if lives_amount <= 0:
                game_end("lose")
            return compare_result
        elif pl_pick == 3 and opp_pick == 1 or pl_pick < opp_pick:
            compare_result = "Вы выиграли!"
            opp_lives_amount = opp_lives_amount - 1
            opp_hearts.config(text = f"Жизней противника:  {opp_current_lives(opp_lives_amount)}")
            if opp_lives_amount <= 0:
                game_end("win")
            return compare_result

    def opp_picked(opp_pick):
        if opp_pick == 1:
            result = "камень"
        elif opp_pick == 2:
            result = "ножницы"
        elif opp_pick == 3:
            result = "бумагу"
        return result

    def opp_think():
        button_rock.config(state=tk.DISABLED)
        button_sci.config(state=tk.DISABLED)
        button_pap.config(state=tk.DISABLED)
        round_result.config(text = "Противник думает.")
        window.update()
        time.sleep(0.3)
        round_result.config(text = "Противник думает..")
        window.update()
        time.sleep(0.3)
        round_result.config(text = "Противник думает...")
        window.update()
        time.sleep(0.3)
        button_rock.config(state=tk.NORMAL)
        button_sci.config(state=tk.NORMAL)
        button_pap.config(state=tk.NORMAL)

    def rock():
        opp_pick = rnd.randint(1,3)
        opp_think()
        round_result.config(text = f"Противник выбрал {opp_picked(opp_pick)}. {compare_picks(1, opp_pick)}")

    def pap():
        opp_pick = rnd.randint(1,3)
        opp_think()
        round_result.config(text = f"Противник выбрал {opp_picked(opp_pick)}. {compare_picks(2, opp_pick)}")

    def sci():
        opp_pick = rnd.randint(1,3)
        opp_think()
        round_result.config(text = f"Противник выбрал {opp_picked(opp_pick)}. {compare_picks(3, opp_pick)}")
    frame.columnconfigure(0, minsize = 133)
    frame.columnconfigure(1, minsize = 133)
    frame.columnconfigure(2, minsize = 133)
    greetings = tk.Label(frame, text = "Сыграем в камень, ножницы, бумагу? Выбирай свой ход!")
    greetings.grid(row=0, column=0, columnspan=3, pady = 10)
    hearts = tk.Label(frame, text = f"Жизней:  {current_lives(lives_amount)}")
    hearts.grid(row = 1, column = 0, padx = 5, pady = 10)
    opp_hearts = tk.Label(frame, text = f"Жизней противника:  {opp_current_lives(opp_lives_amount)}")
    opp_hearts.grid(row = 1, column = 1, columnspan = 2,)
    button_rock = (tk.Button(frame, text = "Камень", width=10, height = 5, command = rock))
    button_rock.grid(row = 3, column = 0, pady = 10)
    button_sci = tk.Button(frame, text = "Ножницы", width=10, height = 5, command = pap)
    button_sci.grid(row = 3, column = 1)
    button_pap = tk.Button(frame, text = "Бумага", width=10, height = 5, command = sci)
    button_pap.grid(row = 3, column = 2)
    round_result = tk.Label(frame, text = "Начнём, пожалуй!")
    round_result.grid(row = 4, column = 0, columnspan = 3, pady = 10)
    results = tk.Label(frame, text = "")
    results.grid(row = 5, column = 1)
    button_exit = tk.Button(frame, text="Выход", width=10, height = 5, command=window_exit)
    button_exit.grid(row = 5, column = 2, pady = 20)
    def game_end(match_result):
        button_rock.config(state=tk.DISABLED)
        button_sci.config(state=tk.DISABLED)
        button_pap.config(state=tk.DISABLED)
        button_reset = tk.Button(frame, text="Ещё раз!", width=10, height = 5, command=window_reset)
        button_reset.grid(row=5, column=0, pady = 20)
        if match_result == "win":
            results_text = "ПОБЕДА!"
        else:
            results_text = "ПОРАЖЕНИЕ!"
        results.config(text = results_text)
    return frame
def window_exit():
    window.quit()
def window_reset():
    global frame
    global lives_amount
    global opp_lives_amount
    lives_amount = 5
    opp_lives_amount = 5
    frame.destroy()
    frame = create_frame()
    frame.pack()

frame = create_frame()
frame.pack()

window.mainloop()
