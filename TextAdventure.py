import tkinter as tk
from tkinter import messagebox

class TextAdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Adventure Game")
        self.has_bow = False
        self.has_bone_knife = False
        self.has_ruby_necklace = False
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Text(self.root, wrap=tk.WORD, height=20, width=70)
        self.text.pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.option1_button = tk.Button(self.button_frame, text="Option 1")
        self.option1_button.pack(side=tk.LEFT, padx=5)

        self.option2_button = tk.Button(self.button_frame, text="Option 2")
        self.option2_button.pack(side=tk.LEFT, padx=5)

        self.option3_button = tk.Button(self.button_frame, text="Option 3")
        self.option3_button.pack(side=tk.LEFT, padx=5)

        self.start_game()

    def start_game(self):
        self.has_bow = False
        self.has_bone_knife = False
        self.has_ruby_necklace = False
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, "Du bist in einem dunklen Wald. Willst du nach links, rechts oder geradeaus gehen?\n")
        self.option1_button.config(text="Nach links gehen", command=self.go_left, state=tk.NORMAL)
        self.option2_button.config(text="Nach rechts gehen", command=self.go_right, state=tk.NORMAL)
        self.option3_button.config(text="Geradeaus gehen", command=self.go_straight, state=tk.NORMAL)

    def go_left(self):
        self.text.insert(tk.END, "Du bist nach links gegangen und hast eine Schatztruhe gefunden. Willst du sie öffnen?\n")
        self.option1_button.config(text="Öffnen", command=self.open_chest)
        self.option2_button.config(text="Nicht öffnen", command=self.leave_chest)
        self.option3_button.config(state=tk.DISABLED)

    def go_right(self):
        self.text.insert(tk.END, "Du bist nach rechts gegangen und triffst auf ein Wildschwein. Willst du kämpfen, weglaufen oder dich verstecken?\n")
        self.option1_button.config(text="Kämpfen", command=self.fight_animal)
        self.option2_button.config(text="Weglaufen", command=self.run_away)
        self.option3_button.config(text="Verstecken", command=self.hide)

    def go_straight(self):
        self.text.insert(tk.END, "Du bist geradeaus gegangen und hast einen Fluss gefunden. Willst du hinüberschwimmen, ein Floß bauen oder dem Fluss folgen?\n")
        self.option1_button.config(text="Hinüberschwimmen", command=self.swim_across)
        self.option2_button.config(text="Floß bauen", command=self.build_raft)
        self.option3_button.config(text="Dem Fluss folgen", command=self.follow_river)

    def open_chest(self):
        self.text.insert(tk.END, "Du hast die Truhe geöffnet und einen Bogen gefunden! Das könnte später nützlich sein.\n")
        self.has_bow = True
        self.option1_button.config(text="Zurückgehen", command=self.go_back_from_chest)
        self.option2_button.config(state=tk.DISABLED)
        self.option3_button.config(state=tk.DISABLED)

    def go_back_from_chest(self):
        self.text.insert(tk.END, "Du gehst zurück zum Ausgangspunkt.\n")
        self.option1_button.config(text="Nach links gehen", command=self.go_left, state=tk.NORMAL)
        self.option2_button.config(text="Nach rechts gehen", command=self.go_right, state=tk.NORMAL)
        self.option3_button.config(text="Geradeaus gehen", command=self.go_straight, state=tk.NORMAL)

    def leave_chest(self):
        self.text.insert(tk.END, "Du hast die Truhe gelassen und deine Reise fortgesetzt. Du gewinnst!\n")
        self.end_game()

    def fight_animal(self):
        if self.has_bow:
            self.text.insert(tk.END, "Du hast den Bogen benutzt, um das Wildschwein zu erschießen und gewonnen! Du schnitzt aus dem Hauer des Wildschweins ein Knochenmesser.\n")
            self.has_bone_knife = True
            self.option1_button.config(text="Zurückgehen", command=self.go_back_from_animal)
            self.option2_button.config(state=tk.DISABLED)
            self.option3_button.config(state=tk.DISABLED)
        else:
            self.text.insert(tk.END, "Du hast versucht, das Wildschwein zu bekämpfen, aber du hast keine Waffe. Du hast verloren!\n")
            self.end_game()

    def go_back_from_animal(self):
        self.text.insert(tk.END, "Du gehst zurück zum Ausgangspunkt.\n")
        self.option1_button.config(text="Nach links gehen", command=self.go_left, state=tk.NORMAL)
        self.option2_button.config(text="Nach rechts gehen", command=self.go_right, state=tk.NORMAL)
        self.option3_button.config(text="Geradeaus gehen", command=self.go_straight, state=tk.NORMAL)

    def run_away(self):
        self.text.insert(tk.END, "Du bist sicher geflüchtet. Du kannst einen anderen Weg wählen.\n")
        self.option1_button.config(text="Nach links gehen", command=self.go_left, state=tk.NORMAL)
        self.option2_button.config(text="Nach rechts gehen", command=self.go_right, state=tk.NORMAL)
        self.option3_button.config(text="Geradeaus gehen", command=self.go_straight, state=tk.NORMAL)

    def hide(self):
        self.text.insert(tk.END, "Du hast dich vor dem Wildschwein versteckt und es ist weggegangen. Du gehst zurück zur Weggabelung.\n")
        self.option1_button.config(text="Nach links gehen", command=self.go_left, state=tk.NORMAL)
        self.option2_button.config(text="Nach rechts gehen", command=self.go_right, state=tk.NORMAL)
        self.option3_button.config(text="Geradeaus gehen", command=self.go_straight, state=tk.NORMAL)

    def swim_across(self):
        self.text.insert(tk.END, "Du bist über den Fluss geschwommen und hast eine rubinrote Halskette am Grund des Flusses gesehen. Willst du nach der Halskette tauchen oder den Fluss entlang gehen?\n")
        self.option1_button.config(text="Nach der Halskette tauchen", command=self.dive_for_necklace)
        self.option2_button.config(text="Den Fluss entlang gehen", command=self.walk_down_river)
        self.option3_button.config(state=tk.DISABLED)

    def dive_for_necklace(self):
        self.text.insert(tk.END, "Du bist nach der Halskette getaucht und hast eine wunderschöne rubinrote Halskette gefunden! Willst du der Straße folgen oder dem Fluss folgen?\n")
        self.has_ruby_necklace = True
        self.option1_button.config(text="Der Straße folgen", command=self.follow_road)
        self.option2_button.config(text="Dem Fluss folgen", command=self.follow_river)
        self.option3_button.config(state=tk.DISABLED)

    def follow_road(self):
        self.text.insert(tk.END, "Du bist der Straße gefolgt und hast ein kleines Dorf gefunden. Du gewinnst!\n")
        self.end_game()

    def go_back_from_necklace(self):
        self.text.insert(tk.END, "Du gehst zurück zum Ausgangspunkt.\n")
        self.option1_button.config(text="Nach links gehen", command=self.go_left, state=tk.NORMAL)
        self.option2_button.config(text="Nach rechts gehen", command=self.go_right, state=tk.NORMAL)
        self.option3_button.config(text="Geradeaus gehen", command=self.go_straight, state=tk.NORMAL)

    def follow_river(self):
        self.text.insert(tk.END, "Du bist dem Fluss gefolgt und hast ein Banditenlager gefunden. Willst du mit den Banditen sprechen, kämpfen oder am Lager vorbeischleichen?\n")
        self.option1_button.config(text="Mit den Banditen sprechen", command=self.talk_to_bandits)
        self.option2_button.config(text="Kämpfen", command=self.fight_bandits)
        self.option3_button.config(text="Vorbeischleichen", command=self.sneak_past_bandits)

    def build_raft(self):
        if self.has_bone_knife:
            self.text.insert(tk.END, "Du hast das Knochenmesser benutzt, um ein Floß zu bauen und bist den Fluss hinunter gesegelt. Du gehst direkt in ein Banditenlager. Willst du mit den Banditen sprechen, kämpfen oder am Lager vorbeischleichen?\n")
            self.option1_button.config(text="Mit den Banditen sprechen", command=self.talk_to_bandits)
            self.option2_button.config(text="Kämpfen", command=self.fight_bandits)
            self.option3_button.config(text="Vorbeischleichen", command=self.sneak_past_bandits)
        else:
            self.text.insert(tk.END, "Du brauchst ein Knochenmesser, um ein Floß zu bauen. Du gehst zurück zum Ausgangspunkt.\n")
            self.option1_button.config(text="Nach links gehen", command=self.go_left, state=tk.NORMAL)
            self.option2_button.config(text="Nach rechts gehen", command=self.go_right, state=tk.NORMAL)
            self.option3_button.config(text="Geradeaus gehen", command=self.go_straight, state=tk.NORMAL)

    def follow_river(self):
        self.text.insert(tk.END, "Du bist dem Fluss gefolgt und hast ein Banditenlager gefunden. Willst du mit den Banditen sprechen, kämpfen oder am Lager vorbeischleichen?\n")
        self.option1_button.config(text="Mit den Banditen sprechen", command=self.talk_to_bandits)
        self.option2_button.config(text="Kämpfen", command=self.fight_bandits)
        self.option3_button.config(text="Vorbeischleichen", command=self.sneak_past_bandits)

    def talk_to_bandits(self):
        if self.has_ruby_necklace:
            self.text.insert(tk.END, "Du hast die Banditen mit der rubinroten Halskette bestochen und sie haben dich durchgelassen. Du gewinnst!\n")
        else:
            self.text.insert(tk.END, "Du hast mit den Banditen gesprochen und sie überzeugt, dich durchzulassen. Du gewinnst!\n")
        self.end_game()

    def fight_bandits(self):
        if self.has_bow:
            self.text.insert(tk.END, "Du hast den Bogen benutzt, um die Banditen zu bekämpfen und gewonnen! Du gewinnst!\n")
            self.end_game()
        else:
            self.text.insert(tk.END, "Du hast versucht, die Banditen zu bekämpfen, aber du hast keine Waffe. Du hast verloren!\n")
            self.end_game()

    def sneak_past_bandits(self):
        self.text.insert(tk.END, "Du bist erfolgreich an den Banditen vorbeigeschlichen. Du gewinnst!\n")
        self.end_game()

    def end_game(self):
        self.option1_button.config(text="Spiel neu starten", command=self.restart_game, state=tk.NORMAL)
        self.option2_button.config(state=tk.DISABLED)
        self.option3_button.config(state=tk.DISABLED)
        messagebox.showinfo("Spiel beendet", "Danke fürs Spielen!")

    def restart_game(self):
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = TextAdventureGame(root)
    root.mainloop()