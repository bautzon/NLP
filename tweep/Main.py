from Scraper import *
from Cleaner import*
from Stemmer import *

debug=False


choose_method()   #scraper
cleaned_text_list=cleaner(data['title'])[0]
cleaned_text_string=cleaner(data['title'])[1]
       



if debug:
    print(f"""

    Data Dictionary: {data}


    ________________

    Cleaned Text List: {cleaned_text_list}

    """)




