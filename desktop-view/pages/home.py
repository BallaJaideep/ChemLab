

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QFrame
)
from PyQt5.QtCore import Qt


class HomePage(QWidget):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate
        self.build_ui()

    
    def build_ui(self):
        root = QVBoxLayout(self)
        root.setSpacing(32)
        root.setContentsMargins(48, 36, 48, 28)

        hero = QVBoxLayout()
        hero.setSpacing(12)

        title = QLabel('Chem<span style="color:#2563eb;">Lab</span>')
        title.setTextFormat(Qt.RichText)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:50px;
            font-weight:900;
            letter-spacing:0.8px;
        """)

        tagline = QLabel(
            "The ultimate professional environment for chemical data processing.\n"
            "Upload, analyze, and visualize with laboratory precision."
        )
        tagline.setAlignment(Qt.AlignCenter)
        tagline.setStyleSheet("""
            font-size:15px;
            color:#64748b;
        """)

        hero.addWidget(title)
        hero.addWidget(tagline)
        root.addLayout(hero)

        
        upload_card = QFrame()
        upload_card.setCursor(Qt.PointingHandCursor)
        upload_card.setStyleSheet("""
            QFrame {
                background: #f8fafc;
                border-radius: 16px;
                padding: 28px;
                border: 2px dashed #2563eb;
            }
            QFrame:hover {
                background: #eef2ff;
                border-color: #1d4ed8;
            }
        """)
        upload_card.mousePressEvent = lambda e: self.on_navigate("upload")

        up_layout = QHBoxLayout(upload_card)
        up_layout.setContentsMargins(24, 20, 24, 20)

        text_stack = QVBoxLayout()
        text_stack.setSpacing(8)

        up_title = QLabel("Start New Analysis")
        up_title.setStyleSheet("""
            font-size:22px;
            font-weight:800;
            color:#0f172a;
        """)

        up_desc = QLabel(
            "Initialize your CSV dataset for automated processing"
        )
        up_desc.setStyleSheet("""
            font-size:14px;
            color:#64748b;
        """)

        text_stack.addWidget(up_title)
        text_stack.addWidget(up_desc)

        upload_btn = QPushButton("Upload Dataset")
        upload_btn.setFixedHeight(44)
        upload_btn.setStyleSheet("""
            QPushButton {
                background:#2563eb;
                color:white;
                font-weight:700;
                border-radius:10px;
                padding: 0 28px;
            }
            QPushButton:hover {
                background:#1d4ed8;
            }
        """)
        upload_btn.clicked.connect(lambda: self.on_navigate("upload"))

        up_layout.addLayout(text_stack)
        up_layout.addStretch()
        up_layout.addWidget(upload_btn)

        root.addWidget(upload_card)

        
        grid = QGridLayout()
        grid.setSpacing(20)
        grid.setContentsMargins(0, 12, 0, 12)

        grid.addWidget(
            self.feature_card(
                "Inventory View",
                "Verify detailed equipment summaries and distribution records.",
                "#7c3aed",
                lambda: self.on_navigate("upload")
            ),
            0, 0
        )

        grid.addWidget(
            self.feature_card(
                "Metric Analysis",
                "Compute automated summary statistics and equipment averages.",
                "#2563eb",
                lambda: self.on_navigate("analysis")
            ),
            0, 1
        )

        grid.addWidget(
            self.feature_card(
                "Visual Analytics",
                "Render high-fidelity graphical data for technical interpretation.",
                "#059669",
                lambda: self.on_navigate("charts")
            ),
            1, 0
        )

        grid.addWidget(
            self.feature_card(
                "Report Archive",
                "Access historical analytics and export professional PDF documents.",
                "#d97706",
                lambda: self.on_navigate("history")
            ),
            1, 1
        )

        root.addLayout(grid)
        root.addStretch()

        
        footer = QHBoxLayout()

        brand = QLabel("⬢ ChemLab Analytics")
        brand.setStyleSheet("""
            font-weight:700;
            color:#0f172a;
        """)

        contact = QLabel(
            "Developer: Jaideep  |  ballajaideep@gmail.com"
        )
        contact.setStyleSheet("""
            color:#64748b;
            font-size:13px;
        """)

        footer.addWidget(brand)
        footer.addStretch()
        footer.addWidget(contact)

        root.addLayout(footer)

    
    def feature_card(self, title, desc, accent, callback):
        card = QFrame()
        card.setCursor(Qt.PointingHandCursor)
        card.setFixedHeight(140)

        card.setStyleSheet(f"""
            QFrame {{
                background: white;
                border-radius: 16px;
                border: 1px solid #e5e7eb;
            }}
            QFrame:hover {{
                background: #f8fafc;
                border-color: {accent};
            }}
        """)
        card.mousePressEvent = lambda e: callback()

        layout = QVBoxLayout(card)
        layout.setContentsMargins(18, 16, 18, 16)
        layout.setSpacing(8)

        # Accent bar (TOP)
        accent_bar = QFrame()
        accent_bar.setFixedHeight(4)
        accent_bar.setStyleSheet(f"""
            background:{accent};
            border-radius:2px;
        """)

        t = QLabel(title)
        t.setStyleSheet("""
            font-size:18px;
            font-weight:800;
            color:#0f172a;
        """)

        d = QLabel(desc)
        d.setWordWrap(True)
        d.setStyleSheet("""
            font-size:13px;
            color:#64748b;
        """)

        layout.addWidget(accent_bar)
        layout.addSpacing(6)
        layout.addWidget(t)
        layout.addWidget(d)
        layout.addStretch()

        return card
