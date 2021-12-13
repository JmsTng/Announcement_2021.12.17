from colorama import init, Fore, Back, Style

class TextForms:
    def header(self, text):
        return f"{Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK + text.upper()}"
    
    def accent(self, before, text, after):
        return f"{Style.NORMAL + Fore.CYAN + Back.BLACK + before} {Style.BRIGHT + Fore.RED + text.upper()} {Style.NORMAL + Fore.CYAN + Back.BLACK + after}"

init()
forms = TextForms()

print(
    f"""
    {forms.header("180 mosquito computer programming team")}
    

    {forms.accent("Here is some information about the", "brand-new", forms.accent("180 Mosquito", "Computer Programming", "team:"))}

     - {forms.accent("Every", "tuesday", forms.accent("from", "1900 - 2100hrs,", "come join us!"))}
     - {forms.accent("We'll be learning", "python", "this year.")}
    
    {Fore.CYAN + "Reasons to join:"}
     - {forms.accent("The ability to", "communitcate", forms.accent("with", "computers", ""))}
     - {forms.accent("Showing off to friends and calling yourself a", "hacker", "(coding is not actually hacking, please don't mix that up)")}
     - {forms.accent("The ability to understand", "programming memes", "")}
     - {forms.accent("The power to create (almost) anything, including", "games, websites, calculators, bots, machine learning, etc.", "")}
    """
)
