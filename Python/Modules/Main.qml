
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

# creando la misma ventana con QtQuick QML (XML like)

Window {
    width: 300
    height: 200
    visible: true
    title: "Hello World"
    
    readonly property list<string> texts: ["Hallo Welt", "Hei maailma",
                                           "Hola Mundo", "Привет мир"]

    function setText() {
        var i = Math.round(Math.random() * 3) 
        text.text = texts[i]
    }

    ColumnLayout {
        anchors.fill: parent

        Text {
            id: tetx
            text: "Hello World"
            Layout.alignment: Qt.AlignHCenter
        }

        Button {
            text: "Click me"
            Layout.alignment: Qt.QtAlignCenter
            onClicked: setText()
        }
    }
}

    
    
