while (true) {
    console.log("Sound Level:" + input.soundLevel())
    if (input.soundLevel() > 200 + 16.2) {
        light.setAll(color.rgb(106, 202, 175))
    } else if (input.soundLevel() > 150 + 16.2) {
        light.setAll(color.rgb(206, 223, 58))
    } else {
        light.clear()
    }
    
}
