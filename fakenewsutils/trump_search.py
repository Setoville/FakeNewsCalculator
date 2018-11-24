
def num_trumps(article, search_word):
    num = 0
    g = article.split(" ")
    for word in g:
        if (word == search_word):
            num = num+1

    return num


x = num_trumps("Washington (CNN)Treasury Secretary Steve Mnuchin is the latest member of Donald Trump's Cabinet to be the focus of the President's ire, the Wall Street Journal reported Friday, citing people familiar with the matter.Trump is blaming Mnuchin for the recently volatile markets and the Federal Reserve's decisions to raise interest rates, those people told The Wall Street Journal.The Fed has been gradually raising rates for three years -- a move to restore levels following the financial crisis. However, Trump has been vocally opposed to the Fed's raises and has called the central bank his biggest threat. People close to the White House told the Journal that Trump chose Jerome Powell to run the Fed in part on Mnuchin's recommendation. According to The Wall Street Journal's report, Trump has been concerned that rising interest rates will stunt economic progress ahead of the 2020 election. The paper also reported that Trump has blamed Mnuchin for the market's latest turbulence. If he's so good, why is this happening? a person familiar with the matter told the Journal. Trump, apparently responding to the report, publicly voiced support for Mnuchin on Twitter Friday evening. I am extremely happy and proud of the job being done by @USTreasury Secretary @StevenMnuchin1. The FAKE NEWS likes to write stories to the contrary, quoting phony sources or jealous people, but they aren't true. They never like to ask me for a quote b/c it would kill their story, Trump wrote. The report comes as Trump has considered shuffling his Cabinet. CNN reported earlier this month that multiple sources inside and outside the Trump administration said that an all-but-certain shakeup is quietly underway at the White House. In particular, chief of staff John Kelly and Department of Homeland Security Secretary Kirstjen Nielsen could be replaced in the near future.Trump acknowledged possible changes earlier this month. Administrations makes changes, usually, after midterms. And probably we'll be right in that category as well, Trump said at the time. I think it's very customary.", "Trump")
print (x)
