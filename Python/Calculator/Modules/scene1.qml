import QtQuick 
import QtQuick.Layouts
import QtQuick.Controls 
import QtQuick.Window 
import QtQuick.Controls.Material 
// importing bridge class for use in qml (was exposed with @QmlElement decorator)

ApplicationWindow {
    id: root
    visible: true
    // combine flags, this component behaves as a window, we apply or operator to flags to combine with frameless
    visibility: Window.Maximized

    RowLayout {
        id: containerV
        Layout.fillHeight: true
        Layout.fillWidth: true

        Rectangle {
            id: screen
            
            Layout.fillWidth: true
            implicitHeight: RowLayout.implicitHeight
            implicitWidth: RowLayout.implicitWidth
            height:80
            color:color()
            radius: 20.0

            Label{
                id: screenTxt
                text: "..."

            }
        }


    }
}