#import matplotlib.pyplot as plt
#import numpy as np
#
#fig, ax = plt.subplots()
#ax.plot(np.random.rand(10))

import types
ctrl_zoom = False

def scrolled(event):
    global ctrl_zoom
    if ctrl_zoom: # ctrl+scroll used
        ax=event.inaxes
        ax._pan_start = types.SimpleNamespace(
                lim=ax.viewLim.frozen(),
                trans=ax.transData.frozen(),
                trans_inverse=ax.transData.inverted().frozen(),
                bbox=ax.bbox.frozen(),
                x=event.x,
                y=event.y)
        if event.button == 'up':
            ax.drag_pan(3, event.key, event.x+10, event.y+10)
        else: #event.button == 'down':
            ax.drag_pan(3, event.key, event.x-10, event.y-10)
        fig=ax.get_figure()
        fig.canvas.draw_idle()

def ctrlpressed(event):
    global ctrl_zoom
    if event.key == 'control':
        ctrl_zoom = True

def ctrlreleased(event):
    global ctrl_zoom
    if event.key == 'control':
        ctrl_zoom = False
        
# # Bind to figure
# fig.canvas.mpl_connect('key_press_event', ctrlpressed)
# fig.canvas.mpl_connect('key_release_event', ctrlreleased)
# fig.canvas.mpl_connect('scroll_event', scrolled)
# fig.show()