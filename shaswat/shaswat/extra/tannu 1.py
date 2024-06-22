from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Frame 1
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(0, 0, 160, 600))
        self.frame1.setStyleSheet("background-color: lightblue;")
        self.frame1.setObjectName("frame1")
        
        # Buttons on Frame 1
        self.button1 = QtWidgets.QPushButton(self.frame1)
        self.button1.setGeometry(QtCore.QRect(20, 20, 120, 40))
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(lambda: self.show_section(self.frame1))
        
        self.button2 = QtWidgets.QPushButton(self.frame1)
        self.button2.setGeometry(QtCore.QRect(20, 80, 120, 40))
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(lambda: self.show_section(self.frame2))
        
        self.button3 = QtWidgets.QPushButton(self.frame1)
        self.button3.setGeometry(QtCore.QRect(20, 140, 120, 40))
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(lambda: self.show_section(self.frame3))
        
        self.button4 = QtWidgets.QPushButton(self.frame1)
        self.button4.setGeometry(QtCore.QRect(20, 200, 120, 40))
        self.button4.setObjectName("button4")
        self.button4.clicked.connect(lambda: self.show_section(self.frame4))
        
        self.button5 = QtWidgets.QPushButton(self.frame1)
        self.button5.setGeometry(QtCore.QRect(20, 260, 120, 40))
        self.button5.setObjectName("button5")
        self.button5.clicked.connect(lambda: self.show_section(self.frame5))
        
        self.button6 = QtWidgets.QPushButton(self.frame1)
        self.button6.setGeometry(QtCore.QRect(20, 320, 120, 40))
        self.button6.setObjectName("button6")
        self.button6.clicked.connect(lambda: self.show_section(self.frame6))
        
        self.button7 = QtWidgets.QPushButton(self.frame1)
        self.button7.setGeometry(QtCore.QRect(20, 380, 120, 40))
        self.button7.setObjectName("button7")
        self.button7.clicked.connect(lambda: self.show_section(self.frame7))
        
        # Frame 2 (Continental) - Hidden by default
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(160, 0, 640, 600))
        self.frame2.setStyleSheet("background-color: lightgreen;")
        self.frame2.setObjectName("frame2")
        self.frame2.hide()
        
        # Add buttons and checkboxes for food items under Continental
        self.add_food_buttons(self.frame2, ["Aloo", "Mithai", "Kaju","Kajjjjju"])
        
        # Frame 3 (Veg) - Hidden by default
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(160, 0, 640, 600))
        self.frame3.setStyleSheet("background-color: lightyellow;")
        self.frame3.setObjectName("frame3")
        self.frame3.hide()
        
        # Add buttons and checkboxes for food items under Veg
        self.add_food_buttons(self.frame3, ["Aloo paratha", "Arhar ki daal", "Biryani",  "Butter chicken", "Chaat","Chana masala"])
        
        
        # Frame 4 (Non-Veg) - Hidden by default
        self.frame4 = QtWidgets.QFrame(self.centralwidget)
        self.frame4.setGeometry(QtCore.QRect(160, 0, 640, 600))
        self.frame4.setStyleSheet("background-color: lightpink;")
        self.frame4.setObjectName("frame4")
        self.frame4.hide()
        
        # Add buttons and checkboxes for food items under Non-Veg
        self.add_food_buttons(self.frame4, ["Chicken Biryani", "Butter Chicken", "Mutton Curry", "Fish Fry"])

        # Frame 5 (South Indian) - Hidden by default
        self.frame5 = QtWidgets.QFrame(self.centralwidget)
        self.frame5.setGeometry(QtCore.QRect(160, 0, 640, 600))
        self.frame5.setStyleSheet("background-color: lightcyan;")
        self.frame5.setObjectName("frame5")
        self.frame5.hide()
        
        # Add buttons and checkboxes for food items under South Indian
        self.add_food_buttons(self.frame5, ["Dosa", "Idli", "Vada", "Sambhar", "Uttapam"])

        # Frame 6 (Chinese) - Hidden by default
        self.frame6 = QtWidgets.QFrame(self.centralwidget)
        self.frame6.setGeometry(QtCore.QRect(160, 0, 640, 600))
        self.frame6.setStyleSheet("background-color: lightgray;")
        self.frame6.setObjectName("frame6")
        self.frame6.hide()
        
        # Add buttons and checkboxes for food items under Chinese
        self.add_food_buttons(self.frame6, ["Manchurian", "Fried Rice", "Chowmein", "Spring Rolls", "Chilli Chicken"])

        # Frame 7 (Sweets) - Hidden by default
        self.frame7 = QtWidgets.QFrame(self.centralwidget)
        self.frame7.setGeometry(QtCore.QRect(160, 0, 640, 600))
        self.frame7.setStyleSheet("background-color: lightcoral;")
        self.frame7.setObjectName("frame7")
        self.frame7.hide()
        
        # Add buttons and checkboxes for food items under Sweets
        self.add_food_buttons(self.frame7, ["Rasgulla", "Gulab Jamun", "Jalebi", "Barfi", "Rasmalai"])

        # Order Confirmation Panel
        self.order_panel = QtWidgets.QFrame(self.centralwidget)
        self.order_panel.setGeometry(QtCore.QRect(0, 450, 800, 150))
        self.order_panel.setStyleSheet("background-color: lightgray;")
        self.order_panel.setObjectName("order_panel")
        
        self.order_label = QtWidgets.QLabel(self.order_panel)
        self.order_label.setGeometry(QtCore.QRect(20, 20, 760, 100))
        self.order_label.setObjectName("order_label")
        self.order_label.setText("Selected Items:\n")
        
        self.confirm_button = QtWidgets.QPushButton(self.order_panel)
        self.confirm_button.setGeometry(QtCore.QRect(600, 120, 180, 30))
        self.confirm_button.setObjectName("confirm_button")
        self.confirm_button.setText("Confirm Order")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "ALL"))
        self.button2.setText(_translate("MainWindow", "Continental"))
        self.button3.setText(_translate("MainWindow", "Veg"))
        self.button4.setText(_translate("MainWindow", "Non-Veg"))
        self.button5.setText(_translate("MainWindow", "South Indian"))
        self.button6.setText(_translate("MainWindow", "Chinese"))
        self.button7.setText(_translate("MainWindow", "Sweets"))
        
    def add_food_buttons(self, parent, foods):
        # Add buttons, checkboxes, and quantity selectors for each food item
        y_position = 20
        for food in foods:
            button = QtWidgets.QPushButton(parent)
            button.setGeometry(QtCore.QRect(20, y_position, 80, 40))
            button.setObjectName("button_" + food.lower())  # Set object name
            button.setText(food)
            checkbox = QtWidgets.QCheckBox(parent)
            checkbox.setGeometry(QtCore.QRect(120, y_position, 20, 20))
            checkbox.setObjectName("checkbox_" + food.lower())
            checkbox.stateChanged.connect(self.update_selected_items)
            minus_button = QtWidgets.QPushButton(parent)
            minus_button.setGeometry(QtCore.QRect(150, y_position, 30, 30))
            minus_button.setObjectName("minus_button_" + food.lower())
            minus_button.setText("-")
            minus_button.clicked.connect(lambda _, f=food: self.decrement_quantity(f))
            quantity_label = QtWidgets.QLabel(parent)
            quantity_label.setGeometry(QtCore.QRect(190, y_position, 30, 30))
            quantity_label.setObjectName("quantity_label_" + food.lower())
            quantity_label.setText("1")
            plus_button = QtWidgets.QPushButton(parent)
            plus_button.setGeometry(QtCore.QRect(220, y_position, 30, 30))
            plus_button.setObjectName("plus_button_" + food.lower())
            plus_button.setText("+")
            plus_button.clicked.connect(lambda _, f=food: self.increment_quantity(f))
            y_position += 50

    def increment_quantity(self, food):
        quantity_label = self.centralwidget.findChild(QtWidgets.QLabel, "quantity_label_" + food.lower())
        if quantity_label:
            current_quantity = int(quantity_label.text())
            if current_quantity == 1:
                quantity_label.setText("2")
            elif current_quantity == 2:
                quantity_label.setText("Full")

    def decrement_quantity(self, food):
        quantity_label = self.centralwidget.findChild(QtWidgets.QLabel, "quantity_label_" + food.lower())
        if quantity_label:
            current_quantity = int(quantity_label.text())
            if current_quantity == 2:
                quantity_label.setText("1")
            elif current_quantity == 1:
                quantity_label.setText("0.5")

    def show_section(self, section):
        all_frames = [self.frame2, self.frame3, self.frame4, self.frame5, self.frame6, self.frame7]
        for frame in all_frames:
            if frame == section:
                frame.show()
            else:
                frame.hide()

    def update_selected_items(self, state):
        selected_items = []
        all_frames = [self.frame2, self.frame3, self.frame4, self.frame5, self.frame6, self.frame7]
        for frame in all_frames:
            for child in frame.children():
                if isinstance(child, QtWidgets.QCheckBox):
                    if child.isChecked():
                        selected_items.append(child.objectName().replace("checkbox_", ""))
        self.order_label.setText("Selected Items:\n" + "\n".join(selected_items))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

