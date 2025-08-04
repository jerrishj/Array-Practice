# The game.py script is a Python demo built with the Ursina game engine that visually illustrates 3D object sorting based on camera distance. It sets up a simple 3D scene with a stationary gray wall and multiple "soldiers" placed at varying depths along the Z-axis. 
# As the soldiers move forward toward the camera, the script continuously calculates and prints their sorted order based on true Euclidean distance — not just Z-values — to simulate how game engines like Call of Duty determine which objects to render first (back-to-front).
#  The camera is placed behind the scene and slightly elevated to give a clear view, and an EditorCamera allows the user to orbit and inspect the scene. This project is ideal for demonstrating why dynamic render order is critical for transparent object handling in 3D graphics.

from ursina import *
from random import uniform

app = Ursina()

# ---------- camera ----------
camera.position  = (0, 2, -10)
camera.rotation_x = 10
EditorCamera()                      # mouse-look so you can orbit the scene

# ---------- parameters ----------
NUM_SOLDIERS   = 5                  # how many red soldiers to spawn
START_Z_RANGE  = (0, 100)            # z-positions (behind the wall to in-front)

# ---------- assets ----------
SOLDIER_MODEL  = 'soldier.glb'      # use your GLB-v2 here (falls back to cube)
FALLBACK_MODEL = 'cube'

# ---------- entities ----------
wall = Entity( model='cube',
               color=color.gray,
               scale=(4, 3, .5),
               position=(0, 0, 100),
               name='Wall')

soldiers = []
for i in range(NUM_SOLDIERS):
    z_pos   = uniform(*START_Z_RANGE)      # random depth
    soldier = Entity(model=SOLDIER_MODEL if load_model(SOLDIER_MODEL) else FALLBACK_MODEL,
                     #color=color.rgba(255, 0, 0, 150),  # semi-transparent red
                     scale=1,
                     position=(uniform(-20, 20), 0, z_pos),
                     name=f'Soldier{i+1}')
    soldiers.append(soldier)

entities = soldiers + [wall]               # everything we want to sort

# ---------- helper ----------
def sort_back_to_front():
    return sorted(entities,
                  key=lambda e: distance(camera.world_position, e.world_position),
                  reverse=True)

# ---------- one-time print ----------
print('\nInitial render order (back-to-front):')
for i, ent in enumerate(sort_back_to_front(), 1):
    print(f'{i}. {ent.name:8}  z={ent.z:5.2f}')

def pretty_print(order):
    print('\nBack-to-front render order:')
    for i, ent in enumerate(order, 1):
        d = distance(camera.world_position, ent.world_position)
        print(f'{i}. {ent.name:8}  z = {ent.z:6.2f}  dist = {d:5.2f}')

# ---------- main loop ----------
def update():
    # march soldiers slowly toward the camera
    for s in soldiers:
        s.z -= time.dt * .5

    # each frame: sort & report
    ordered = sort_back_to_front()
    pretty_print(ordered)
    print('\nDynamic render order:')
    for i, ent in enumerate(ordered, 1):
        dist = distance(camera.world_position, ent.world_position)
        print(f'{i}. {ent.name:8}  z={ent.z:6.2f}  (dist {dist:5.2f})')

app.run()
