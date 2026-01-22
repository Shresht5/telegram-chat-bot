import re 
def markdowwn_to_html_format(str):
    str=re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", str)
    str=re.sub(r"\*(.*?)\*", r"<b>\1</b>", str)
    return str
            