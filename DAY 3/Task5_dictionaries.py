default_settings={"theme":"light","language":"English","notifications":True}


user_setting={
    "theme":"dark","notifications":True
}
final_settings=default_settings.copy()
final_settings.update(user_setting)

print(final_settings)
