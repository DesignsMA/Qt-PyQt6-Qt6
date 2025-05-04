import QtQuick 
import QtQuick.Controls 
// For PySide6 (Qt 6.x)
import Qt5Compat.GraphicalEffects

ApplicationWindow {
    id: window
    width: 400
    height: 300
    visible: true
    color: "#161616" // Fondo oscuro

    // Botón personalizado
    Button {
        id: customButton
        anchors.centerIn: parent
        width: 150
        height: 50
        text: "Hazme hover"
        
        // Eliminar el estilo por defecto
        background: Rectangle {
            id: btnBackground
            color: "transparent"
            radius: 8 // Bordes redondeados
            border.color: "#ff0000" // Borde rojo
            border.width: 3 // Grosor del borde
            
            // Sombra/glow que solo se muestra en hover
            layer.enabled: customButton.hovered
            layer.effect: Glow {
                samples: 15 // Calidad del efecto glow
                color: "#ff3333" // Color rojo más claro
                spread: 0.4 // Intensidad del glow
            }
        }

        // Estilo del texto
        contentItem: Text {
            text: customButton.text
            font.pixelSize: 16
            color: "white"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        // Efecto de escala al hacer hover
        Behavior on scale {
            NumberAnimation { duration: 100 }
        }

        // Animación al pasar el mouse
        onHoveredChanged: {
            if (hovered) {
                scale = 1.05
            } else {
                scale = 1.0
            }
        }
    }
}