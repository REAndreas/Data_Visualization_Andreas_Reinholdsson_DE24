import taipy.gui.builder as tgb
from taipy.gui import Gui

palindrom_word = ""
image_to_show = ""
points = 0
point_mark = ""

def clear_result(state):
     state.palindrom_word = ""

def check_palindrom(state):
    palindrom_word = state.palindrom_word
    palindrom_word_reverese = state.palindrom_word.replace(" ", "").lower()[::-1]

    if state.palindrom_word.replace(" ", "").lower() == palindrom_word_reverese:
        state.image_to_show = "fake_cat"
        state.points += 1
    else:
        state.image_to_show = "fake_sad_rabbit"
        state.points -= 1        
    state.point_mark = "⭐"
    state.point_mark = state.point_mark * state.points

    

with tgb.Page() as page:
    tgb.text("# Palindrom game", mode="md")

    with tgb.layout("2 1"):
        with tgb.part(class_name="card"):
            tgb.text("Skriv in ett ord eller mening för att se om det är ett palindrom")
            tgb.input("{palindrom_word}")
            tgb.button(label="Submit", class_name="plain", on_action=check_palindrom)

            tgb.text("{palindrom_word}")

        with tgb.part(class_name="card"):
                tgb.image("assets/{image_to_show}.png")
                tgb.text("{point_mark}")

if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)