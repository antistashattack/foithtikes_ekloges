import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton,
    QPushButton, QHBoxLayout, QButtonGroup, QMessageBox, QScrollArea
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

questions = {
    "aponekrwsh_sullogwn": "Θες να απονεκρωθούν οι φοιτητικοί σύλλογοι;",
    "eksousia_stis_gs": "Θες όλη η εξουσία να είναι στις Γενικές Συνελεύσεις;",
    "sullogoi_tampela": "Οι φοιτητικοί σύλλογοι είναι ταμπέλες που τους κάνεις ό,τι θέλεις;",
    "kleinw_khnhmata": "Κλείνεις κάθε χρόνο τα κινήματα;",
    "kata_tis_gnwshs": "Είσαι κατά της γνώσης;",
    "o_kosmos_xazos": "Πιστεύεις πως ο κόσμος είναι χαζός και δεν καταλαβαίνει αν πεις τη λέξη 'καπιταλισμός';",
    "anasugkrothsh_sullogwn": "Θες ανασυγκρότηση φοιτητικών συλλόγων;",
    "thetiko_protagma": "Έχεις θετικό πρόταγμα για το πανεπιστήμιο των αναγκών μας;",
    "enantia_se_kubernhsh_susthma_ee": "Είσαι συνολικά ενάντια σε κυβέρνηση, σύστημα και Ε.Ε.;",
    "ereuna_gia_anagkes": "Θες έρευνα και γνώση για τις κοινωνικές ανάγκες;",
    "sundesh_ergatiko": "Θες σύνδεση του φοιτητικού με το εργατικό και τα ταξικά σωματεία;",
    "antifasismos": "Είσαι ενάντια στον φασισμό;",
    "patriarxia": "Στηρίζεις την πατριαρχία;",
    "polemos": "Είσαι υπέρ του πολέμου;",
    "diagrafes_didaktra": "Στηρίζεις διαγραφές και δίδακτρα στα μεταπτυχιακά;",
    "idiwtika_panep": "Στηρίζεις ιδιωτικά πανεπιστήμια;",
    "upoxrhmatodothsh": "Στηρίζεις υποχρηματοδότηση και έρευνα για στρατό και επιχειρήσεις;",
    "katarg_asilou": "Είσαι υπέρ της κατάργησης του ασύλου;",
    "mnhmonia_mexri_na_sbhsei_o_hlios_o_prasinos": "Στηρίζεις μνημόνια μέχρι να σβήσει ο ήλιος ο πράσινος;"
}


def foithtikes_ekloges(**a):
    conditions = {
        "aponekrwsh": a["aponekrwsh_sullogwn"],
        "pasok": all([
            a["diagrafes_didaktra"],
            a["idiwtika_panep"],
            a["upoxrhmatodothsh"],
            a["katarg_asilou"],
            a["mnhmonia_mexri_na_sbhsei_o_hlios_o_prasinos"]
        ]),
        "pks": not a["eksousia_stis_gs"] and a["sullogoi_tampela"] and a["kleinw_khnhmata"],
        "asummetria": not a["eksousia_stis_gs"] and not a["thetiko_protagma"] and a["kata_tis_gnwshs"] and a["o_kosmos_xazos"],
        "attack": (
            all([
                a["eksousia_stis_gs"],
                a["anasugkrothsh_sullogwn"],
                a["thetiko_protagma"],
                a["ereuna_gia_anagkes"],
                a["sundesh_ergatiko"],
                a["antifasismos"],
                not a["patriarxia"],
                not a["polemos"],
                not a["diagrafes_didaktra"],
                not a["idiwtika_panep"],
                not a["upoxrhmatodothsh"],
                not a["katarg_asilou"]
            ]) or a["enantia_se_kubernhsh_susthma_ee"]
        )
    }

    outcomes = {
        "aponekrwsh": "Δεν μπορούμε να αγωνιστούμε χωρίς συλλόγους. Κάτσε σπίτι σου.",
        "pasok": "ΠΑΣΟΚ",
        "pks": "ΠΚΣ",
        "asummetria": "Αναφη στο τετράγωνο / Ασυμμετρία",
        "attack": "Αντίσταση - ATTACK"
    }

    return next((msg for key, msg in outcomes.items() if conditions.get(key)),
                "ΑΝΑΠΟΦΑΣΙΣΤΟ! Πρέπει να συζητήσουμε από κοντά!")


class QuestionWidget(QWidget):
    def __init__(self, key, text):
        super().__init__()
        self.key = key
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.yes = QRadioButton("Ναι")
        self.no = QRadioButton("Όχι")
        self.group = QButtonGroup(self)
        self.group.addButton(self.yes, id=1)
        self.group.addButton(self.no, id=0)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        buttons = QHBoxLayout()
        buttons.addWidget(self.yes)
        buttons.addWidget(self.no)
        layout.addLayout(buttons)

        self.setLayout(layout)

    def get_answer(self):
        id = self.group.checkedId()
        if id == -1:
            return None
        return bool(id)

    def mark_unanswered(self):
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, QColor("red"))
        self.label.setPalette(palette)

    def clear_mark(self):
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, QColor("black"))
        self.label.setPalette(palette)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🗳️ Φοιτητικές Εκλογές")
        self.resize(700, 700)

        self.questions_widgets = []
        self.layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()

        for key, text in questions.items():
            widget = QuestionWidget(key, text)
            self.questions_widgets.append(widget)
            scroll_layout.addWidget(widget)

        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        self.submit_button = QPushButton("Υποβολή")
        self.submit_button.clicked.connect(self.evaluate)

        self.layout.addWidget(scroll_area)
        self.layout.addWidget(self.submit_button)
        self.setLayout(self.layout)

    def evaluate(self):
        answers = {}
        all_answered = True

        for widget in self.questions_widgets:
            answer = widget.get_answer()
            if answer is None:
                widget.mark_unanswered()
                all_answered = False
            else:
                widget.clear_mark()
                answers[widget.key] = answer

        if not all_answered:
            QMessageBox.warning(self, "Ανεπαρκείς Απαντήσεις", "Πρέπει να απαντήσεις σε όλες τις ερωτήσεις!")
        else:
            result = foithtikes_ekloges(**answers)
            QMessageBox.information(self, "Αποτέλεσμα", f"📢 Πρέπει να ψηφίσεις: {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Arial", 11))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
