def segment(text: str, language: list[str]) -> bool:
    text = cutstring(text, language)
    if len(text) == 0:
        return True
    return False

def cutstring(text: str, language: list[str]) -> str :
    if len(language) > 0 :
        text = text.replace(language.pop(),'')
        return cutstring(text,language)
    return text
# def recursive_input(string:str):
#     pass
def main():
    data = [e.strip().replace('\'','') for e in input("Enter list[str]: ").split(',')]

    print(f"text: str =",f"\'{data[0]}\'")
    print("lang: list[str] =",data[1:])
    print("segment(text, lang) ->",segment(data[0],data[1:]))
if __name__ == "__main__":
    main()