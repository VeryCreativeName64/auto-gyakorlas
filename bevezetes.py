def auto_adat():
    auto=input("Add meg az auto nevét: ")
    gyarev=input("Add meg az auto gyártási évét: ")

    print(f"Autó neve: {auto}")
    print(f"Gyártási dátuma: {gyarev}")

    return gyarev

def auto_eredmeny():
    eredmeny=auto_adat()
    if (eredmeny<=2000):
        print("öreg auto")
    elif(eredmeny==2024):
        print("friss gyártás")
    else:
        print("áltagos korú")

