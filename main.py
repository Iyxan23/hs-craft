import os
import string
import opensimplex
if os.geteuid() != 0:
    print("Please run this script with superuser privilages for keyboard support")
    exit()
import keyboard

# Functions ==================================


def draw(px, py, chunks_):
    playerchunk = chunks_[int(px/len(chunks_))]
    chunkbefore = []
    chunkafter = []
    # TODO: CUSTOMIZEABLE RENDER DISTANCE
    # Temporary Render distance: 1 chunks
    try:
        chunkbefore = chunks_[int(px/len(chunks_)) - 1]
    except IndexError:
        pass

    try:
        chunkafter = chunks_[int(px/len(chunks_)) + 1]
    except IndexError:
        pass

    # Render the player chunk
    playerchunk_rendered = []
    playerchunk_tmp = ""
    for x in range(15):
        for y in range(256):
            if (py + 10) > y > (py - 10):
                playerchunk_tmp += playerchunk[x][y]
        playerchunk_rendered.append(playerchunk_tmp)
        playerchunk_tmp = ""

    # Render chunk before if its not empty
    chunkbefore_rendered = []
    chunkbefore_temp = ""
    try:
        for x in range(0, 15):
            for y in range(0, 256):
                if (py + 10) > y > (py - 10):
                    chunkbefore_temp += chunkbefore[x][y]
            chunkbefore_rendered.append(chunkbefore_temp)
            chunkbefore_temp = ""
    except IndexError:
        for x in range(0, 15):
            for y in range((py - 10), (py + 10)):
                chunkbefore_temp += " "
            chunkbefore_rendered.append(chunkbefore_temp)
            chunkbefore_temp = ""

    # The same as chunk after
    chunkafter_rendered = []
    chunkafter_tmp = ""

    try:
        for x in range(15):
            for y in range(256):
                if py + 10 > y > py - 10:
                    chunkafter_tmp += chunkafter[x][y]
            chunkafter_rendered.append(chunkafter_tmp)
            chunkafter_tmp = ""
    except IndexError:
        for x in range(15):
            for y in range((py-10),(py+10)):
                chunkafter_tmp += " "
            chunkbefore_rendered.append(chunkbefore_tmp)
            chunkbefore_tmp = ""

    # Render 3 of the chunks to a single variable



# Functions ==================================

# Icon support check
confirm = input(" <- Does this character says B? (y/n) ")
if confirm == "n" or confirm == "N" or confirm == "no" or confirm == "No":
    print("Installing Icon support for your terminal..")
    os.mkdir("IconSupport")
    os.chdir("IconSupport")
    os.system("git clone https://github.com/sebastiencs/icons-in-terminal.git")
    os.system("sudo sh install.sh")
    os.chdir("..")
    print("Done Installing icon support for your terminal!")
elif not confirm == "y" or not confirm == "Y" or not confirm == "yes" or not confirm == "Yes":
    print("Error: Please input y or n")
    exit()
print("Starting Game")
ascii_chars = list(string.printable)
os.system("clear")
raw_seed = input("Input seed: ")
seed = int()
seed_chars = ""
for char in raw_seed:
    try:
        seed_chars += str(ascii_chars.index(char))
    except ValueError:
        print("ERROR: Please input a printable number")
seed = int(seed_chars)
print("Converted seed: " + seed_chars)
# TODO: MAKE MENU FOR SAVING WORLDS
# TODO: IMPLEMENT WORLD GENERATION
# Chunk: x:15 y:256
# Init variables
chunks = []
x = 0
y = 0
#
# print("Generating world")
# # Generate world using 1D perlin noise
# # Generate at least 20x20 chunks == 300x300 blocks
# chunk_tmp = []
# y_tmp = []
# noise_gen = opensimplex.OpenSimplex(seed=seed)
# for chunk_y in range(0, 20):
#     for chunk_x in range(0, 20):
#         for x in range(0, 15):
#             for y in range(0, 15):
#                 height = noise_gen.noise2d(y=1, x=x)

# Temporary World generation ========================
chunk = []
chunk_piece = []
for chnks in range(0, 30):
    # Per chunk
    for x in range(0, 15):
        for y in range(0, 256):
            if y < 60:
                chunk_piece.append("#")
            else:
                chunk_piece.append(" ")
        chunk.append(chunk_piece)
        chunk_piece = []
    chunks.append(chunk)
    chunk = []
# Flat world generation =============================

# Game
while True:
    draw(x, y, chunks)
