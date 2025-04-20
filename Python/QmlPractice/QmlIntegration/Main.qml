// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause


import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1
// importing bridge class for use in qml (was exposed with @QmlElement decorator)
import io.qt.textproperties 1.0 

ApplicationWindow {
    id: page
    width: 800
    height: 400
    visible: true
    Material.theme: Material.Dark
    Material.accent: Material.Red
    // instance of bridge object that contains all slots (logic) to be used
    // Since this is qml it's only a declaration of a component to be instanciated
    Bridge { 
        id: bridge
    }

    GridLayout {
        id: grid
        columns: 2
        rows: 3

        ColumnLayout {
            spacing: 2
            Layout.columnSpan: 1
            Layout.preferredWidth: 400

            Text {
                id: leftlabel
                Layout.alignment: Qt.AlignHCenter
                color: "white"
                font.pointSize: 16
                text: "Qt for Python"
                Layout.preferredHeight: 100
                Material.accent: Material.Green
            }

            RadioButton {
                id: italic
                Layout.alignment: Qt.AlignLeft
                text: "Italic"
                // on toggled signal
                onToggled: {
                    // sets leftlabel italic property to true if toggled
                    leftlabel.font.italic = bridge.getItalic(italic.text) 
                    leftlabel.font.bold = bridge.getBold(italic.text)
                    leftlabel.font.underline = bridge.getUnderline(italic.text)

                }
            }
            RadioButton {
                id: bold
                Layout.alignment: Qt.AlignLeft
                text: "Bold"
                onToggled: {
                    leftlabel.font.italic = bridge.getItalic(bold.text)
                    leftlabel.font.bold = bridge.getBold(bold.text)
                    leftlabel.font.underline = bridge.getUnderline(bold.text)
                }
            }
            RadioButton {
                id: underline
                Layout.alignment: Qt.AlignLeft
                text: "Underline"
                onToggled: {
                    leftlabel.font.italic = bridge.getItalic(underline.text)
                    leftlabel.font.bold = bridge.getBold(underline.text)
                    leftlabel.font.underline = bridge.getUnderline(underline.text)
                }
            }
            RadioButton {
                id: noneradio
                Layout.alignment: Qt.AlignLeft
                text: "None"
                //cheked by default
                checked: true 
                onToggled: {
                    leftlabel.font.italic = bridge.getItalic(noneradio.text)
                    leftlabel.font.bold = bridge.getBold(noneradio.text)
                    leftlabel.font.underline = bridge.getUnderline(noneradio.text)
                }
            }
        }

        ColumnLayout {
            id: rightcolumn
            spacing: 2
            Layout.columnSpan: 1
            Layout.preferredWidth: 400
            Layout.preferredHeight: 400
            Layout.fillWidth: true

            RowLayout {
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter


                Button {
                    id: red
                    text: "Red"
                    highlighted: true
                    Material.accent: Material.Red
                    // on clicked signal
                    onClicked: {
                        // set leftlabel color to the hex value returned by the slot getColor in bridge
                        leftlabel.color = bridge.getColor(red.text)
                    }
                }
                Button {
                    id: green
                    text: "Green"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        leftlabel.color = bridge.getColor(green.text)
                    }
                }
                Button {
                    id: blue
                    text: "Blue"
                    highlighted: true
                    Material.accent: Material.Blue
                    onClicked: {
                        leftlabel.color = bridge.getColor(blue.text)
                    }
                }
                Button {
                    id: nonebutton
                    text: "None"
                    highlighted: true
                    Material.accent: Material.BlueGrey
                    onClicked: {
                        leftlabel.color = bridge.getColor(nonebutton.text)
                    }
                }
            }
            //second colum element
            RowLayout {
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                Text {
                    id: rightlabel
                    color: "white"
                    Layout.alignment: Qt.AlignLeft
                    text: "Font size"
                    Material.accent: Material.White
                }
                Slider {
                    // 60% of the actual column width
                    width: rightcolumn.width*0.6
                    Layout.alignment: Qt.AlignRight
                    id: slider
                    value: 0.5
                    // value of the slider, from 0 to 1
                    // on value changed signal
                    onValueChanged: {
                        // change leftlabel point size to the value returned by the getSize slot
                        // get size returns a value with a maximum of 34, 
                        leftlabel.font.pointSize = bridge.getSize(value)
                    }
                }
            }
        }
    }
}
