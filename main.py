import random


def hola(selector, text):
    try:
        my_selector = selector
        whole_selector = "texto [selector_" + my_selector + "]"

        if "TEXT" in whole_selector:
            print(whole_selector)
            word = whole_selector.replace("TEXT", text)
            print(word)
        else:
            print("Not a valid selector")
    except "fail":
        print('Element text does not match ', text)
        assert False


hola_txt = "que onda raza " + "TEXT"

if __name__ == "__main__":
    hola(hola_txt, "reemplazo")
