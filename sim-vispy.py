import os
os.environ["QT_LOGGING_RULES"] = "qt.qpa.*=false"
from vispy import scene
from vispy import app
from vispy.visuals.transforms import STTransform
from variables import *
from physics import run_simulation
phistory = run_simulation(p, v, m, t, dt, l, rc, k, r0)


canvas = scene.SceneCanvas(keys='interactive', 
                  show=True, 
                  size=(800, 600))

view = canvas.central_widget.add_view()

view.camera = 'turntable'

view.camera.center = (l/2, l/2, l/2)

view.camera.distance = 5*l


axis = scene.visuals.XYZAxis(parent=view.scene)
axis.transform = STTransform(scale=(l, l, l))


markers = scene.visuals.Markers(parent=view.scene)

markers.set_data(pos=phistory[0], face_color='blue', size=15)


frame_index = 0

def update(event):
    global frame_index
    markers.set_data(pos=phistory[frame_index], face_color='blue', size=15)
    frame_index += 1
    if frame_index >= len(phistory):
        frame_index = 0


timer = app.Timer(interval=1/60.0)

timer.connect(update)

timer.start()

app.run()