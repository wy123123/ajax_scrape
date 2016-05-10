#example:
#use oanda currency converter
import json
import requests
import datetime

BASE_CURRENCY = "SGD"
QUOTE_CURRENCY = "CNY"

def construct_ajax_url(basecurrency,quotecurrency,date=None):
    if not date:
        date = str(datetime.date.today())
    return "https://www.oanda.com/currency/converter/update?base_currency_0="+BASE_CURRENCY+"&quote_currency="+QUOTE_CURRENCY+"&end_date="+date+"&view=details&id=1&action=C&"
    
header = {
"authority":"www.oanda.com",
#"method":"GET",
"scheme":"https",
"accept":"text/javascript, text/html, application/xml, text/xml, */*",
"accept-encoding":"gzip, deflate, sdch",
"accept-language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
#"cookie":"mru_quote=CNY%2CUSD%2CEUR%2CSGD%2CGBP; base_currency_0=SGD; quote_currency=CNY; mru_base0=SGD%2CUSD%2CEUR%2CCNY%2CGBP; __cfduid=dffd41249c3e4b7374952dbd403d9d82d1460699978; opc_id=3D4FF01E-02CF-11E6-92D8-EE685C335BE4; saw-ccc=1; optimizelyEndUserId=oeu1460699990291r0.09164953001883647; optimizelySegments=%7B%22225865993%22%3A%22gc%22%2C%22227082520%22%3A%22direct%22%2C%22227082521%22%3A%22false%22%2C%222289461220%22%3A%22none%22%7D; optimizelyBuckets=%7B%223701302901%22%3A%223690591218%22%2C%225399393182%22%3A%225414560368%22%7D; _ceg.s=o5nvn5; _ceg.u=o5nvn5; tc=1; _gat=1; oanda-login-redirect=true; ncc_session=b9f2920d68cdc62547a27e227427914ce191361f; mmapi.store.p.0=%7B%22mmparams.d%22%3A%7B%7D%2C%22mmparams.p%22%3A%7B%22mmid%22%3A%221494406532032%7C%5C%22-877274700%7CDgAAAArAI34pQA0AAA%3D%3D%5C%22%22%2C%22pd%22%3A%221494406532037%7C%5C%22-2069056635%7CDgAAAAoBQsAjfilADf0WLE8DAMA6yteweNNIDwAAACNd6inzZNNIAAAAAJkAAAD%2F%2F%2F%2F%2FABF3d3cuZ29vZ2xlLmNvbS5zZwRZDQIAAAAAAAAAAAAA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAABRQ%3D%3D%5C%22%22%2C%22srv%22%3A%221494406532042%7C%5C%22lvsvwcgus07%5C%22%22%7D%7D; mmapi.store.s.0=%7B%22mmparams.d%22%3A%7B%7D%2C%22mmparams.p%22%3A%7B%7D%7D; _ga=GA1.2.1380517591.1460699980; opc=3EF1B498-02CF-11E6-B83F-9ED6C8685298",
#"referer":"https://www.oanda.com/currency/converter/",
"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36",
"x-prototype-version":"1.7",
"x-requested-with":"XMLHttpRequest"   
}

s = requests.session()
r = s.get(url=construct_ajax_url(BASE_CURRENCY,QUOTE_CURRENCY),headers=header)
r.status_code
r.json()['data']['bid_ask_data']['bid']
