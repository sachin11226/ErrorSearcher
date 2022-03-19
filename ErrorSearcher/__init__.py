import webbrowser
def detect(path):
    try:
        if __file__!=path:
            exec(open(path).read())
            
    except Exception as e:
        a = type(e).__name__
        error = f"{str(a)}: {e}"
        error =f"https://www.google.com/search?q={error} stack overflow"
        webbrowser.open(error)