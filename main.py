while True:
    print("Sound Level:" + input.sound_level())
    if input.sound_level() > 250 + 16.2:
        light.set_all(color.rgb(234,200,240))
    elif input.sound_level() > 200 + 16.2:
        light.set_all(color.rgb(106, 202, 175))
    elif input.sound_level() > 150 + 16.2:
        light.set_all(color.rgb(206,223,58))
    elif input.sound_level() > 100 + 16.2:
        light.set_all(color.rgb(195,58,223)
    else:
        light.clear()