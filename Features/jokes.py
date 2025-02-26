import pyjokes

def jokes():
    try:
        my_joke = pyjokes.get_joke(language="en", category="neutral") 
        return my_joke
    except:
        return "Unable to get any jokes at the moment"
