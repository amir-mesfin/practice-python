"""
Animated Text Adventure (PyQt5)

Save this file as `TextAdventure_GUI_animated.py` and run:
    pip install PyQt5
    python TextAdventure_GUI_animated.py

Assets folder (optional but recommended):
  assets/
    bg_forest.jpg       (background image for forest)
    bg_cave.jpg         (background image for cave)
    click.wav           (button click sound)
    victory.wav         (victory sound)

The program gracefully degrades if assets are missing.
"""

import sys
import random
import os
from functools import partial
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QByteArray, QPoint
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout,
    QHBoxLayout, QGridLayout, QFrame, QListWidget, QListWidgetItem, QStackedLayout,
    QGraphicsOpacityEffect, QMessageBox
)

# Try import sound class (may not work on some platforms)
try:
    from PyQt5.QtMultimedia import QSoundEffect
    SOUND_AVAILABLE = True
except Exception:
    SOUND_AVAILABLE = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE_DIR, 'assets')

# Utility: safe load pixmap
def load_pixmap(name):
    path = os.path.join(ASSETS, name)
    if os.path.exists(path):
        return QPixmap(path)
    return None

class AnimatedLabel(QLabel):
    """A label that types text like a terminal and supports fade animations."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWordWrap(True)
        self._full_text = ""
        self._index = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self.setFont(QFont('Consolas', 11))

    def type_text(self, text, speed=10):
        self._full_text = text
        self._index = 0
        self.setText("")
        interval = max(4, 40 - speed)
        self._timer.start(interval)

    def _tick(self):
        if self._index >= len(self._full_text):
            self._timer.stop()
            return
        self.setText(self.text() + self._full_text[self._index])
        self._index += 1

    def immediate(self, text):
        self._timer.stop()
        self.setText(text)

    def fade_in(self, duration=350):
        eff = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(eff)
        anim = QPropertyAnimation(eff, b"opacity")
        anim.setDuration(duration)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        anim.start(QPropertyAnimation.DeleteWhenStopped)


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Adventure - Animated Edition")
        self.resize(900, 600)
        self.player_health = 100
        self.player_gold = 0
        self.inventory = []
        self.location = 'forest'
        self.game_over = False

        # Sounds
        self.sounds = {}
        if SOUND_AVAILABLE:
            self._load_sounds()

        # Build UI
        self._build_ui()
        self._apply_styles()
        self.show_forest(initial=True)

    def _load_sounds(self):
        def s(name, file):
            path = os.path.join(ASSETS, file)
            se = QSoundEffect()
            if os.path.exists(path):
                se.setSource(QUrl.fromLocalFile(path))
            self.sounds[name] = se
        try:
            from PyQt5.QtCore import QUrl
            s('click', 'click.wav')
            s('victory', 'victory.wav')
        except Exception:
            pass

    def _build_ui(self):
        # Background frame
        self.bg = QLabel(self)
        self.bg.setGeometry(0, 0, self.width(), self.height())
        self.bg.setScaledContents(True)

        # Left: Game output & actions
        left = QVBoxLayout()
        left.setSpacing(8)

        self.header_label = QLabel()
        self.header_label.setFixedHeight(70)
        self.header_label.setFont(QFont('Segoe UI', 10, QFont.Bold))
        self.header_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.output = AnimatedLabel()
        self.output.setMinimumHeight(300)
        self.output.setStyleSheet('background: rgba(0,0,0,0.3); padding: 10px; border-radius: 8px;')

        # Buttons grid
        self.btn_grid = QGridLayout()
        self.btn_grid.setSpacing(8)
        self.buttons = [QPushButton() for _ in range(4)]
        for i, b in enumerate(self.buttons):
            b.setCursor(Qt.PointingHandCursor)
            b.setFixedHeight(44)
            b.clicked.connect(partial(self._button_clicked, i))
            self.btn_grid.addWidget(b, i, 0)

        left.addWidget(self.header_label)
        left.addWidget(self.output, stretch=1)
        left.addLayout(self.btn_grid)

        # Right: Inventory + mini map / stats
        right = QVBoxLayout()
        right.setSpacing(12)

        stats_frame = QFrame()
        stats_layout = QHBoxLayout()
        stats_frame.setLayout(stats_layout)
        self.health_label = QLabel()
        self.gold_label = QLabel()
        stats_layout.addWidget(self.health_label)
        stats_layout.addStretch()
        stats_layout.addWidget(self.gold_label)

        inv_label = QLabel("Inventory")
        inv_label.setFont(QFont('Segoe UI', 11, QFont.Bold))
        self.inventory_list = QListWidget()
        self.inventory_list.setFixedWidth(220)
        self.inventory_list.setFixedHeight(300)

        right.addWidget(stats_frame)
        right.addWidget(inv_label)
        right.addWidget(self.inventory_list)
        right.addStretch()

        # Main layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.addLayout(left, stretch=1)
        main_layout.addLayout(right)

        # Responsive: stack for screens if needed
        self.setLayout(main_layout)

    def _apply_styles(self):
        self.setStyleSheet('''
            QWidget { background: #0b1020; color: #e6eef8; }
            QPushButton { background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2b6ea3, stop:1 #2b9bd3); border-radius:8px; color: white; font-weight:600; }
            QPushButton:hover { transform: scale(1.02); }
            QListWidget { background: rgba(255,255,255,0.03); border-radius:6px; }
        ''')
        self.health_label.setFont(QFont('Segoe UI', 10))
        self.gold_label.setFont(QFont('Segoe UI', 10))

    # ------------------------- GAME UI HELPERS -------------------------
    def _button_clicked(self, idx):
        # Play click sound
        if SOUND_AVAILABLE and 'click' in self.sounds:
            try:
                self.sounds['click'].play()
            except Exception:
                pass
        # Map button text to action
        text = self.buttons[idx].text()
        text = text.lower()
        if 'cave' in text and 'go' in text:
            self.show_cave()
        elif 'river' in text and 'go' in text:
            self.show_river()
        elif 'search' in text and 'forest' in text:
            self.search_forest()
        elif 'inventory' in text or 'check' in text:
            self.show_inventory()
        elif 'treasure' in text:
            self.find_treasure()
        elif 'fight' in text or 'monster' in text:
            self.fight_monster()
        elif 'drink' in text:
            self.drink_water()
        elif 'fish' in text:
            self.fish()
        elif 'follow' in text:
            self.follow_river()
        elif 'return' in text:
            # determine where to return
            if 'forest' in text:
                self.show_forest()
            elif 'river' in text:
                self.show_river()
            elif 'cave' in text:
                self.show_cave()
        elif 'run' in text or 'escape' in text:
            self.show_forest()
        else:
            # fallback: try exact match mapping
            mapping = {
                'go to cave': self.show_cave,
                'go to river': self.show_river,
                'search forest': self.search_forest,
                'check inventory': self.show_inventory,
            }
            for k, fn in mapping.items():
                if k in text:
                    fn()
                    return

    def update_header(self):
        self.header_label.setText(f"  Health: {self.player_health}   |   Gold: {self.player_gold}   |   Location: {self.location.capitalize()}")
        self.health_label.setText(f"HP: {self.player_health}")
        self.gold_label.setText(f"Gold: {self.player_gold}")
        # inventory list
        self.inventory_list.clear()
        for it in self.inventory:
            QListWidgetItem(it, self.inventory_list)

    def set_background_for(self, loc):
        pix = None
        if loc == 'forest':
            pix = load_pixmap('bg_forest.jpg')
        elif loc == 'cave':
            pix = load_pixmap('bg_cave.jpg')
        elif loc == 'river':
            pix = load_pixmap('bg_river.jpg')
        if pix:
            self.bg.setPixmap(pix)
        else:
            # fallback gradient background via palette
            pal = QPalette()
            pal.setBrush(QPalette.Window, QBrush(Qt.black))
            self.setPalette(pal)

    # ------------------------- SCENES -------------------------
    def show_forest(self, initial=False):
        self.location = 'forest'
        self.update_header()
        self.set_background_for('forest')
        text = (
            "You are in a dark, misty forest. Tall trees whisper in the wind.\n"
            "Paths lead in different directions."
        )
        self._animate_output(text)
        self._set_buttons([('Go to Cave',), ('Go to River',), ('Search Forest',), ('Check Inventory',)])

    def show_cave(self):
        self.location = 'cave'
        self.update_header()
        self.set_background_for('cave')
        if 'torch' not in self.inventory:
            text = "You step into a black cave. It's too dark — you need a torch to continue."
            self._animate_output(text)
            self._set_buttons([('Return to Forest',), ('',), ('',), ('',)])
            return
        text = "You light your torch and enter the cave. Glitter catches your eye."
        self._animate_output(text)
        self._set_buttons([('Search Treasure',), ('Fight Monster',), ('Return to Forest',), ('',)])

    def show_river(self):
        self.location = 'river'
        self.update_header()
        self.set_background_for('river')
        text = "You arrive by a calm river. The water glitters and cools your face."
        self._animate_output(text)
        self._set_buttons([('Drink Water',), ('Fish',), ('Follow River',), ('Return to Forest',)])

    # ------------------------- ACTION LOGIC -------------------------
    def search_forest(self):
        found_items = [
            ("a shiny gold coin", "gold", 5),
            ("a healing herb", "herb", 0),
            ("an old torch", "torch", 0),
            ("a sharp stone", "stone", 0),
            ("nothing useful", None, 0)
        ]
        item, action, value = random.choice(found_items)
        msg = f"You search the forest and found {item}."
        if action == 'gold':
            self.player_gold += value
            msg += f" +{value} gold."
        elif action == 'herb':
            healed = min(100 - self.player_health, 20)
            self.player_health = min(100, self.player_health + 20)
            msg += f" You use the herb and recover {healed} HP."
        elif action and action not in self.inventory:
            self.inventory.append(action)
            msg += f" {action.capitalize()} added to inventory."
        self.update_header()
        self._animate_output(msg)
        self._return_button('forest')

    def find_treasure(self):
        treasure = random.randint(20, 50)
        self.player_gold += treasure
        text = f"You pry open a chest and find {treasure} gold coins."
        if random.random() > 0.7:
            special = random.choice(['diamond', 'ancient sword', 'magic amulet'])
            self.inventory.append(special)
            text += f"\nYou also find a {special}!"
        self.update_header()
        self._animate_output(text)
        self._return_button('cave')

    def fight_monster(self):
        text = "A giant spider lunges at you!"
        # Simple fight: exchange blows until someone falls or random outcome
        monster_hp = 30
        fight_log = text + '\n'
        while monster_hp > 0 and self.player_health > 0:
            dmg = random.randint(6, 16)
            monster_hp -= dmg
            fight_log += f"You hit the monster for {dmg} damage.\n"
            if monster_hp <= 0:
                reward = random.randint(10, 30)
                self.player_gold += reward
                fight_log += f"You slay the beast and take {reward} gold.\n"
                break
            mdmg = random.randint(5, 14)
            self.player_health -= mdmg
            fight_log += f"The monster bites you for {mdmg} damage.\n"
            if self.player_health <= 0:
                fight_log += "You are mortally wounded..."
                break
        self.update_header()
        self._animate_output(fight_log)
        if self.player_health <= 0:
            self._game_over()
        else:
            self._return_button('cave')
            # victory sound
            if SOUND_AVAILABLE and 'victory' in self.sounds:
                try:
                    self.sounds['victory'].play()
                except Exception:
                    pass

    def drink_water(self):
        gain = min(100 - self.player_health, 10)
        self.player_health = min(100, self.player_health + 10)
        self.update_header()
        self._animate_output(f"You drink the cool water and recover {gain} HP.")
        self._return_button('river')

    def fish(self):
        if random.random() > 0.3:
            heal = random.randint(5, 15)
            self.player_health = min(100, self.player_health + heal)
            self.update_header()
            self._animate_output(f"You catch a fish and regain {heal} HP.")
        else:
            self._animate_output("You try to fish, but catch nothing.")
        self._return_button('river')

    def follow_river(self):
        msg = "You follow the river and discover a hidden village. Villagers greet you warmly."
        if self.player_health < 100:
            heal = 100 - self.player_health
            self.player_health = 100
            msg += f" They heal you fully (+{heal} HP)."
        if self.player_gold < 30:
            gift = random.randint(10, 20)
            self.player_gold += gift
            msg += f" They gift you {gift} gold."
        self.update_header()
        self._animate_output(msg)
        self._return_button('river')

    def show_inventory(self):
        if not self.inventory:
            self._animate_output("Your inventory is empty.")
        else:
            items = '\n'.join([f"- {i}" for i in self.inventory])
            self._animate_output(f"Inventory:\n{items}")
        self._return_button('forest')

    # ------------------------- UI Helpers -------------------------
    def _set_buttons(self, texts):
        # texts: list of tuples (label, )
        for i in range(4):
            label = texts[i][0] if i < len(texts) and texts[i] else ''
            btn = self.buttons[i]
            if label:
                btn.setText(label)
                btn.show()
                btn.setEnabled(True)
                # animate slide-in
                anim = QPropertyAnimation(btn, b"pos")
                anim.setDuration(350)
                anim.setEasingCurve(QEasingCurve.OutBack)
                start = btn.pos() + QPoint(0, 20)
                anim.setStartValue(start)
                anim.setEndValue(btn.pos())
                anim.start(QPropertyAnimation.DeleteWhenStopped)
            else:
                btn.setText('')
                btn.hide()

    def _animate_output(self, text):
        # Use typewriter effect then fade in
        self.output.immediate('')
        self.output.type_text(text, speed=20)
        self.output.fade_in()

    def _return_button(self, where):
        # Replace buttons with a single return button linked to `where`
        if where == 'forest':
            self._set_buttons([('Return to Forest',), ('',), ('',), ('',)])
        elif where == 'river':
            self._set_buttons([('Return to River',), ('',), ('',), ('',)])
        elif where == 'cave':
            self._set_buttons([('Return to Cave',), ('',), ('',), ('',)])

    def _game_over(self):
        self.game_over = True
        self._animate_output("GAME OVER\nYou have been defeated.")
        for b in self.buttons:
            b.setEnabled(False)
        QMessageBox.information(self, "Game Over", f"You died. Final gold: {self.player_gold}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GameWindow()
    win.show()
    sys.exit(app.exec_())
