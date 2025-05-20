import pyautogui
import keyboard
import time
import threading
import tkinter as tk
from tkinter import messagebox


PossiblePasswords = [
    "able", "acid", "aged", "airy", "ally", "anti", "area", "army", "atom", "auto", "axis", "baby", "back", "bait", "bake", "bald", "ball", "band", "bank", "bark",
    "barn", "bath", "bead", "beak", "beam", "beef", "beer", "bell", "belt", "bend", "bent", "best", "beta", "bias", "biff", "bike", "bill", "bird", "bite", "blow",
    "blue", "blur", "boat", "body", "bold", "bolt", "bomb", "bone", "book", "boot", "born", "boss", "both", "bowl", "brag", "brow", "buck", "bull", "bump", "burn",
    "busy", "cage", "cake", "call", "camp", "card", "care", "case", "cash", "cast", "cave", "cell", "chef", "chew", "chip", "city", "clan", "clap", "claw", "clay",
    "clip", "club", "clue", "coal", "coat", "code", "coin", "cold", "coma", "comb", "cone", "cook", "cool", "copy", "core", "corn", "cost", "cozy", "crab", "crew",
    "crop", "crow", "cube", "cuff", "cure", "cute", "damp", "dare", "dark", "dart", "dash", "data", "date", "dawn", "dead", "deal", "deck", "deed", "deep", "dent",
    "deny", "desk", "dial", "diet", "dime", "dine", "dire", "dirt", "dish", "diva", "dive", "does", "doll", "done", "doom", "door", "dose", "down", "drag", "draw",
    "drip", "drop", "drug", "drum", "dual", "duck", "duel", "duet", "dull", "dump", "dune", "dunk", "dust", "duty", "earn", "ease", "east", "easy", "echo", "edge",
    "edit", "eery", "else", "envy", "epic", "etch", "ever", "evil", "exam", "exit", "expo", "face", "fact", "fade", "fail", "fake", "fall", "fame", "fang", "farm",
    "fast", "fate", "fear", "feed", "feel", "feet", "fill", "film", "find", "fine", "fire", "firm", "fish", "fist", "fits", "five", "flag", "flak", "flap", "flat",
    "flaw", "flew", "flex", "flip", "flop", "flow", "flux", "foam", "foil", "folk", "food", "fool", "foot", "fork", "form", "fort", "foul", "foxy", "frat", "free",
    "frog", "fuel", "full", "fund", "funk", "fury", "fuzz", "gain", "game", "gang", "gasp", "gate", "gaze", "gear", "germ", "girl", "give", "glow", "goal", "goat",
    "gold", "golf", "gone", "good", "grab", "grid", "grin", "grip", "grow", "gulf", "guru", "hack", "half", "hall", "halo", "hard", "hawk", "head", "hear", "heat",
    "hell", "help", "hemp", "herd", "here", "hero", "hide", "hill", "hint", "hire", "hiss", "hive", "hoax", "hold", "hole", "holy", "home", "hood", "hook", "hope",
    "horn", "host", "hour", "huge", "hulk", "hunt", "hurl", "hurt", "husk", "hymn", "hype", "idea", "idle", "idly", "idol", "iffy", "inch", "iris", "iron", "itch",
    "item", "jack", "jail", "jaws", "jazz", "jeep", "jive", "jobs", "join", "joke", "jolt", "jump", "junk", "jury", "just", "keep", "kick", "kill", "kilo", "kind",
    "king", "kiss", "kite", "kiwi", "knee", "knob", "know", "lack", "lady", "lair", "lake", "lama", "lamb", "lame", "lamp", "land", "lane", "lard", "lash", "last",
    "lawn", "lazy", "lead", "leaf", "lean", "leap", "left", "lend", "lens", "less", "levy", "liar", "life", "lift", "like", "lily", "limb", "lime", "line", "link",
    "lint", "lips", "list", "live", "load", "loaf", "loan", "lock", "logo", "long", "look", "loop", "loot", "lord", "lore", "lose", "loss", "lost", "love", "luck",
    "lump", "lush", "lynx", "made", "mail", "main", "make", "mark", "mask", "mass", "mate", "math", "maze", "meal", "mean", "menu", "mesh", "mess", "mild", "mile",
    "milk", "mini", "mint", "miss", "mist", "mojo", "monk", "mono", "mood", "moon", "more", "most", "moth", "move", "much", "mule", "muse", "must", "mute", "nail",
    "name", "navy", "near", "neat", "neck", "need", "neon", "nest", "news", "next", "nice", "nine", "none", "noon", "nose", "nosy", "note", "noun", "nuke", "numb",
    "oboe", "odds", "oily", "omen", "omit", "once", "only", "open", "oval", "oven", "over", "pack", "page", "paid", "park", "pass", "past", "path", "pawn", "peak",
    "peel", "pelt", "perk", "pest", "pick", "pipe", "plan", "play", "plot", "plug", "plum", "poem", "poke", "pole", "pony", "pool", "pope", "pork", "port", "pose",
    "post", "prop", "puck", "pull", "pulp", "puma", "pump", "punk", "pure", "push", "quit", "quiz", "race", "raft", "rage", "raid", "rail", "rain", "ramp", "rank",
    "rant", "rare", "rash", "rate", "rear", "redo", "rely", "rent", "rest", "rice", "rich", "ride", "riff", "rift", "ring", "riot", "ripe", "rise", "risk", "road",
    "roar", "robe", "rock", "roof", "room", "rope", "rose", "rosy", "rude", "ruin", "rule", "runt", "ruse", "rush", "rust", "safe", "salt", "same", "sand", "sane",
    "save", "scan", "scar", "seal", "seed", "seen", "sell", "semi", "send", "shoe", "shop", "shot", "show", "sick", "side", "sift", "sign", "silk", "sing", "sink",
    "site", "size", "skin", "skip", "skit", "slam", "slap", "slay", "slim", "slip", "slot", "slow", "slug", "slur", "snag", "snap", "snip", "snow", "snug", "soak",
    "soap", "sock", "soda", "sofa", "soft", "sold", "some", "song", "soon", "sort", "soul", "soup", "sour", "spam", "span", "spin", "spit", "spot", "spur", "stab",
    "star", "stay", "stem", "step", "stew", "stir", "stun", "such", "suit", "sure", "swan", "swim", "taco", "take", "tale", "talk", "tall", "tame", "tank", "task",
    "taxi", "tear", "teen", "tell", "tend", "tent", "term", "test", "text", "that", "them", "then", "they", "thin", "this", "tick", "tide", "tidy", "tier", "ties",
    "tile", "tilt", "time", "tire", "toad", "told", "toll", "tone", "took", "tool", "torn", "town", "trap", "tree", "trim", "trio", "trip", "true", "tsar", "tuba",
    "tube", "tuna", "tune", "turk", "turn", "twig", "twin", "type", "tzar", "ugly", "undo", "unit", "urge", "used", "user", "vase", "vast", "verb", "very", "vest",
    "vibe", "vice", "view", "vine", "visa", "void", "volt", "vote", "wage", "wait", "wake", "walk", "wall", "want", "warm", "warp", "wart", "wash", "wasp", "wave",
    "weak", "weed", "week", "were", "west", "when", "whip", "wife", "wild", "will", "wind", "wine", "wing", "wire", "wise", "wolf", "wood", "wool", "word", "work",
    "worm", "yank", "yard", "yarn", "yawn", "year", "yell", "yeti", "yoga", "your", "zone", "zoom"
]

running = False
FilteredPasswords = []

def console_log(message):
    console.configure(state='normal')
    console.insert(tk.END, message + '\n')
    console.see(tk.END)
    console.configure(state='disabled')

def update_count(*args):
    prefix = prefix_var.get().lower()
    use_prefix = use_prefix_var.get()
    use_suffix = use_suffix_var.get()

    global FilteredPasswords

    if not (use_prefix or use_suffix):
        red_label.config(text="")
    elif len(prefix) != 2:
        red_label.config(text="NEEDS 2 CHARACTERS")
    else:
        red_label.config(text="")

    if len(prefix) != 2 and (use_prefix or use_suffix):
        FilteredPasswords = []
        count_label.config(text=f"Matching: 000 | Max time: 00.00 min")
        avg_label.config(text=f"| Avg time: 00.00 min")
        return

    if use_prefix:
        FilteredPasswords = [word for word in PossiblePasswords if word.startswith(prefix)]
    elif use_suffix:
        FilteredPasswords = [word for word in PossiblePasswords if word.endswith(prefix)]
    else:
        FilteredPasswords = PossiblePasswords.copy()

    count = len(FilteredPasswords)
    max_time = (count * 4) / 60
    expected_trials = (count + 1) / 2
    avg_time = (expected_trials * 4) / 60
    count_label.config(text=f"Matching: {count:03d} | Max time: {max_time:05.2f} min")
    avg_label.config(text=f"| Avg time: {avg_time:05.2f} min")

def limit_entry_length(*args):
    value = prefix_var.get()
    if len(value) > 2:
        prefix_var.set(value[:2])
    value2 = skipto_var.get()
    if len(value2) > 1:
        skipto_var.set(value2[:1])

def start_typing():
    global running
    if running:
        return

    update_count()

    if not FilteredPasswords:
        messagebox.showinfo("Info", "No matching words found.")
        return

    skip_letter = skipto_var.get().lower()
    if skip_letter and (not skip_letter.isalpha() or len(skip_letter) != 1):
        messagebox.showerror("Error", "Skip To Letter must be a single alphabet letter.")
        return

    running = True

    def typing_loop():
        console_log("Starting in 10 seconds...")
        time.sleep(10)
        skip_letter = skipto_var.get().lower()
        skip_reached = True if not skip_letter else False
        total = len(FilteredPasswords)
        count = 0
        for index, phrase in enumerate(FilteredPasswords, start=1):
            if not running or keyboard.is_pressed('f9'):
                break
            log_text = f"{index:03d}/{total:03d}: {phrase} ({total - index} remaining)"
            console_log(log_text)
            if not skip_reached:
                if phrase.startswith(skip_letter):
                    skip_reached = True
                else:
                    continue
            count += 1
            pyautogui.write(phrase)
            pyautogui.press('enter')
            time.sleep(4)
        console_log(f"Typing finished. {count} words typed.")
        stop_typing()

    threading.Thread(target=typing_loop, daemon=True).start()

def stop_typing():
    global running
    running = False
    console_log("Stopped.")

def toggle_prefix():
    if use_prefix_var.get():
        use_suffix_var.set(False)
    update_count()

def toggle_suffix():
    if use_suffix_var.get():
        use_prefix_var.set(False)
    update_count()

root = tk.Tk()
root.title("Terminal Cracker")
root.geometry("272x287")
root.resizable(False, False)

use_prefix_var = tk.BooleanVar()
use_suffix_var = tk.BooleanVar()
prefix_var = tk.StringVar()
skipto_var = tk.StringVar()

prefix_var.trace_add("write", limit_entry_length)
prefix_var.trace_add("write", update_count)
skipto_var.trace_add("write", limit_entry_length)
use_prefix_var.trace_add("write", update_count)
use_suffix_var.trace_add("write", update_count)

prefix_cb = tk.Checkbutton(root, text="Use Prefix", variable=use_prefix_var, command=toggle_prefix)
suffix_cb = tk.Checkbutton(root, text="Use Suffix", variable=use_suffix_var, command=toggle_suffix)
prefix_label = tk.Label(root, text="<-- 2 Letter Filter")
prefix_entry = tk.Entry(root, textvariable=prefix_var, width=5)

skipto_label = tk.Label(root, text="<-- Skip To Letter")
skipto_entry = tk.Entry(root, textvariable=skipto_var, width=5)

count_label = tk.Label(root, text="Matching: 000 | Max time: 00.00 min", font=("Consolas", 10))
red_label = tk.Label(root, text="", fg="red", font=("Arial", 11, "bold"))
avg_label = tk.Label(root, text="| Avg time: 00.00 min", font=("Consolas", 9))

start_btn = tk.Button(root, text="Start", command=start_typing)
stop_btn = tk.Button(root, text="Stop", command=stop_typing)

console = tk.Text(root, height=9, width=43, state='disabled', bg='black', fg='lime', font=("Consolas", 8))

prefix_cb.place(x=5, y=5)
suffix_cb.place(x=5, y=30)
red_label.place(x=90, y=15)
prefix_entry.place(x=10, y=55)
prefix_label.place(x=45, y=55)
skipto_label.place(x=45, y=80)
skipto_entry.place(x=10, y=80)
count_label.place(x=10, y=105)
start_btn.place(x=10, y=130)
stop_btn.place(x=60, y=130)
avg_label.place(x=108, y=130)
console.place(x=5, y=160)

update_count()
root.mainloop()