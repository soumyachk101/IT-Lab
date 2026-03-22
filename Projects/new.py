import tkinter as tk
import math
import random
import time

W, H = 1000, 650
FPS_MS = 16  # ~60 FPS


def lerp(a, b, t):
    return int(a + (b - a) * t)


def lerp_color(c1, c2, t):
    return "#%02x%02x%02x" % tuple(lerp(int(c1[i:i+2], 16), int(c2[i:i+2], 16), t)
                                   for i in (0, 2, 4))


class AnimatedScene:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=W, height=H, highlightthickness=0)
        self.canvas.pack()
        root.title("Decorative Animation — GitHub Copilot")
        self.t = 0.0

        # Decorative elements state
        self.stars = [self._rand_star() for _ in range(90)]
        self.comets = []
        self.ball = {'x': W * 0.25, 'y': H * 0.6, 'vx': 4.5, 'vy': -6.0, 'r': 36}
        self.poly = {'cx': W * 0.7, 'cy': H * 0.35, 'r': 70, 'sides': 6, 'angle': 0.0}
        self.message = "Welcome to the College Lab Demo!  "
        self.msg_x = W
        self._last_time = time.time()

        # draw static decorative frame
        self._draw_frame()
        self._loop()

    def _rand_star(self):
        return {
            'x': random.uniform(0, W),
            'y': random.uniform(0, H * 0.6),
            'size': random.uniform(1.2, 3.8),
            'phase': random.uniform(0, math.pi * 2),
            'speed': random.uniform(0.0005, 0.0016)
        }

    def _draw_gradient_bg(self):
        # Vertical gradient from deep blue -> purple -> pink -> gold
        stops = [
            ("001a33", 0.0),
            ("0f2b4a", 0.35),
            ("6b3f8b", 0.65),
            ("f49a57", 1.0)
        ]
        self.canvas.delete("grad")
        segments = 200
        for i in range(segments):
            t = i / (segments - 1)
            # find proper stop range
            for j in range(len(stops) - 1):
                if stops[j][1] <= t <= stops[j+1][1]:
                    local_t = (t - stops[j][1]) / (stops[j+1][1] - stops[j][1])
                    c = lerp_color(stops[j][0], stops[j+1][0], local_t)
                    break
            y0 = int(i * H / segments)
            y1 = int((i + 1) * H / segments)
            self.canvas.create_rectangle(0, y0, W, y1, fill=c, width=0, tags="grad")

    def _draw_frame(self):
        pad = 12
        self.canvas.create_rectangle(pad, pad, W - pad, H - pad, outline="#dddddd", width=3)
        # corner flourishes
        self.canvas.create_arc(6, 6, 140, 140, start=90, extent=90, style=tk.ARC, outline="#cccccc", width=3)
        self.canvas.create_arc(W-140, 6, W-6, 140, start=0, extent=90, style=tk.ARC, outline="#cccccc", width=3)
        self.canvas.create_arc(6, H-140, 140, H-6, start=180, extent=90, style=tk.ARC, outline="#cccccc", width=3)
        self.canvas.create_arc(W-140, H-140, W-6, H-6, start=270, extent=90, style=tk.ARC, outline="#cccccc", width=3)
        # bottom caption
        self.canvas.create_text(W/2, H-28, text="Animated Demo — Show for your college lab teacher",
                                fill="#ffffff", font=("Helvetica", 14, "bold"))

    def _update_stars(self, dt):
        # twinkle and subtle vertical drift
        for s in self.stars:
            s['phase'] += s['speed'] * dt * 1000
            s['y'] += 0.01 * dt
            if s['y'] > H * 0.6:
                s.update(self._rand_star())

    def _draw_stars(self):
        self.canvas.delete("star")
        for s in self.stars:
            glow = 0.5 + 0.5 * math.sin(s['phase'])
            size = int(s['size'] * (0.8 + 0.6 * glow))
            cval = int(200 + 55 * glow)
            color = f"#{cval:02x}{cval:02x}{255:02x}"
            x, y = int(s['x']), int(s['y'])
            self.canvas.create_oval(x - size, y - size, x + size, y + size,
                                    fill=color, outline="", tags="star")

    def _maybe_spawn_comet(self):
        if random.random() < 0.012:
            y = random.uniform(20, H * 0.5)
            self.comets.append({
                'x': -20, 'y': y, 'vx': random.uniform(6.0, 11.0), 'vy': random.uniform(-0.5, 0.8),
                'life': 1.0
            })

    def _update_comets(self, dt):
        for c in list(self.comets):
            c['x'] += c['vx'] * dt / 16
            c['y'] += c['vy'] * dt / 16
            c['life'] -= 0.02 * dt / 16
            if c['x'] > W + 50 or c['life'] <= 0:
                self.comets.remove(c)

    def _draw_comets(self):
        self.canvas.delete("comet")
        for c in self.comets:
            x, y = c['x'], c['y']
            tail_len = 80
            self.canvas.create_line(x, y, x - tail_len, y + 6, fill="#fff2b8",
                                    width=2, smooth=1, tags="comet")
            self.canvas.create_oval(x - 6, y - 3, x + 6, y + 3, fill="#fff8d6", outline="", tags="comet")

    def _update_ball(self, dt):
        b = self.ball
        b['vy'] += 0.35 * dt / 16  # gravity
        b['x'] += b['vx'] * dt / 16
        b['y'] += b['vy'] * dt / 16
        # bounce floor
        floor = H - 110
        if b['y'] + b['r'] > floor:
            b['y'] = floor - b['r']
            b['vy'] = -abs(b['vy']) * 0.72
            b['vx'] *= 0.99
        # walls
        if b['x'] - b['r'] < 30 or b['x'] + b['r'] > W - 30:
            b['vx'] *= -1

    def _draw_ball(self):
        self.canvas.delete("ball")
        b = self.ball
        # glow
        for i, alpha in enumerate((0.06, 0.04, 0.02), start=1):
            r = b['r'] + 18 * i
            color = f"#{int(240):02x}{int(140 + 40*i):02x}{int(100 + 50*i):02x}"
            self.canvas.create_oval(b['x'] - r, b['y'] - r, b['x'] + r, b['y'] + r,
                                    fill=color, outline="", tags="ball")
        # main ball with simple highlight
        self.canvas.create_oval(b['x'] - b['r'], b['y'] - b['r'], b['x'] + b['r'], b['y'] + b['r'],
                                fill="#ff8b4b", outline="", tags="ball")
        self.canvas.create_oval(b['x'] - b['r']*0.5, b['y'] - b['r']*0.9,
                                b['x'] - b['r']*0.15, b['y'] - b['r']*0.6,
                                fill="#ffd6ba", outline="", tags="ball")

    def _update_poly(self, dt):
        p = self.poly
        p['angle'] += 0.0035 * dt
        p['r'] = 60 + 12 * math.sin(self.t * 0.6)

    def _draw_poly(self):
        self.canvas.delete("poly")
        p = self.poly
        pts = []
        for i in range(p['sides']):
            a = p['angle'] + i * 2 * math.pi / p['sides']
            x = p['cx'] + p['r'] * math.cos(a)
            y = p['cy'] + p['r'] * math.sin(a)
            pts.extend((x, y))
        # shadow
        self.canvas.create_polygon([coord + (6 if idx % 2 == 0 else 6) for idx, coord in enumerate(pts)],
                                   fill="#222222", outline="", tags="poly")
        # main rotating polygon with gradient-ish fill by stroke layers
        for i in range(5):
            shade = 200 - i * 28
            color = f"#{shade:02x}{int(120 + i*8):02x}{255:02x}"
            self.canvas.create_polygon(pts, fill=color, outline="", tags="poly")
        # inner highlight
        inner = [(p['cx'] + 0.6*(x-p['cx']), p['cy'] + 0.6*(y-p['cy'])) for x, y in zip(pts[::2], pts[1::2])]
        flat = [c for pt in inner for c in pt]
        self.canvas.create_polygon(flat, fill="#eeeeee", outline="", tags="poly")

    def _draw_message(self):
        self.canvas.delete("msg")
        self.msg_x -= 1.6  # scroll speed
        if self.msg_x < -len(self.message) * 14:
            self.msg_x = W
        # decorative rounded rect behind text
        x0 = self.msg_x - 18
        y0 = H - 72
        x1 = self.msg_x + 820
        y1 = H - 40
        self.canvas.create_rectangle(x0, y0, x1, y1, fill="#333333", outline="", tags="msg")
        # message text repeated for smoothness
        for i in range(2):
            self.canvas.create_text(self.msg_x + i * 420, H - 56, anchor="w",
                                    text=self.message + "   ", font=("Arial", 18, "bold"),
                                    fill="#fff3b8", tags="msg")

    def _loop(self):
        now = time.time()
        dt = (now - self._last_time) * 1000
        self._last_time = now
        self.t += dt / 1000.0

        self._draw_gradient_bg()
        self._maybe_spawn_comet()
        self._update_stars(dt)
        self._update_comets(dt)
        self._update_ball(dt)
        self._update_poly(dt)

        self._draw_stars()
        self._draw_comets()
        self._draw_ball()
        self._draw_poly()
        self._draw_message()

        self.root.after(FPS_MS, self._loop)


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedScene(root)
    root.mainloop()