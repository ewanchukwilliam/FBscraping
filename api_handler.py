#!/usr/bin/env python

from urllib.parse import urlencode
import requests
import json
from urllib import parse
from urllib.parse import parse_qs, unquote

from flatten_json import flatten

# DATA_RAW = "av=100080415237651&__aaid=0&__user=100080415237651&__a=1&__req=16&__hs=20454.HCSV2%3Acomet_pkg.2.1...0&dpr=2&__ccg=EXCELLENT&__rev=1031559969&__s=29upx0%3A53bdkw%3Av4pvm1&__hsi=7590494475290140305&__dyn=7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwhUKbgS3q2ibwNw9G2Sawba1DwUx60GE3Qwb-q7oc81EEc87m221Fwgo9oO0n24oaEnxO0Bo7O2l2Utwqo5W1ywiE4u9x-3m1mzXw8W58jwGzEaE5e3ym2SU4i5oe8cEW4-5pUfEe88o4Wm7-2K0-obUG2-azqwt8eo5d08O321LyUaUbGxe6Uak0zU8oC1Hg6C13xecwBwWzUlwEKufxamEbbxG1fBG2-2K0E8461wweW2K3abxG6E2Uw&__csr=grh4I5dhLfeG4NkTfb9YGfktNAAGfjn_ff4GAxcRjcQYy9sDrsABAW4fIXLkyp5qb99t5QvmJ-juHFbXJWj8GGjFkVjlleCilrGq8yBK9VFQ9tejKFoy-qUJa496JCz9qUgXzWxecDGHCDQWxyi4oLyoVz998CE8FV4Fe8Dz8-mbByUlDU4e8Ly8Sui6USuKrG6EtwPK5bzHxS16y-68C8wZwJwge2K78CEC1BDwgpElCzXBU-2aeVo5vwqE6e4oaUbESewSxC7rzEkBGfG4Ve4bwv8G8CBAy84m2G1Mxq321wDx51R0EwhU11E7e22687u2i36ew8a5U1HqwGwd2pyE5KawwzU24wCwjUx5hAm3uQ17wNAmm2Km3d0JKKbwLyrJx21Cwoo02tQw1bG00Rm605IpS08Tw4Sw3JUx0jO02cE0gEw7Gw8hS1-Dg0oGw34E0iPwAwm81xA0oC1XwnU0g6w7cw0DIK08FGSaw3o80Mq03oO09Wz8C07uUpw5Bo0w2&__hsdp=gJ22q41WAayoqcGiaoy48kh8PIzq7GHpakOcxfhaAbP6GwVh38kkmG1mi8IYB4Ex9Ax5cF1d8y6FHAbcF6tqesKzQCwxi7YegjMSx4Ig6G4Ni11cyQzgPpqO99tQgUzCtDrO0BKeyqHDR9pnAQHXPFSOMwipoyap4AmdaWwEyOhqu49oz8gCA7-OUyW49Ec8kp2glaixh9KIiuF0KoGcn8QWODzyZ8qDWdFUGmt6ByZ7Kucy7UhylyFaBopG4oymaohG4C9BFC55wWgSVEWuGrwJxG34iezpHF4gF1emqswWQ4Aq9KGiV4A6kmayrcoUFVsMrzUareaxzK748GVVkQh7Feve4K8ymW4yVBUjxK7cUCgUcK8813yWxJuS4ojxu79EcCdAyry84aFawPCwko8ohwgUC-19g6ifyXxu1gxZ161XK48eQ2h3d0rE98b8y15w7YxAEqw4JAc1iF0Zw5uwxwc6bwgo6a36KU1TE3xw8W1OxS0JU3zwbZ0bm0REK15w4HzU3aw6jw1lq0UU3owf-0ebweG0C82rw4ywtQ0km0Jo36weC1JwnU1d9U1ZU1Wo3Vw20U0iRw26o6W1cwt8&__hblp=0p83KwQw4cxi6EjDz-1rwZU3uCyoao3pwrU3DwkEowcu0hK9xCq2C5emawRwio2HwIwlobUK2a2Sm0g20w89Ec82Nw6ux-0AE4O2qcwtUuwIy8uwCw5owdJ0cC1Gw6_wSwxwcS11whojwcW8w10i0P8mwb-0JEbo7KfwEw5NzU3axO0g-1dxy0ku480yG0XUjwcR0RwaS0AU4i0_UjwxAwo828zE0Bu0E84C3K1sxK1p-4US0Eo20woolgkw9W0Ao2Rwcq1ow921JwnU3Qw_Dw7dw6TwmV83QzE3BwdO36093w4Sw4Fx208eyEfU9HK48eQ1oxG0oS&__sjsp=gJ22q41WAayoqcGIFBEgN94zeOdEuFCiBcz9DVqA-P6GwJbh38kkmG1mi8Jtikiy4CiPkZ5fQy8qQFZ8GApREB7agZd8hfi95sj96MjMSx4Ig6G4Ni11cyQzgPpqO99tyy2epStB83ycG9R9gGjiz6mSaxauayCh95x1eEd8ixem8VOo19bwTy9UyawOK7A7Q59E4G4E8o5K3te2S1cgcE9po5y0OokxG212axp4gFeve58y2q7U0xO0m50p8-bK0iO3J0OQ&__comet_req=15&fb_dtsg=NAfuJhLDTOJX4UTEde-UVZXsea7AvzcE8YjmBtn9PLB704jCHSswsrQ%3A30%3A1766761617&jazoest=25436&lsd=SriiQnL8_bcPCu2zJjRHNb&__spin_r=1031559969&__spin_b=trunk&__spin_t=1767299714&__jssesw=1&__crn=comet.fbweb.CometMarketplaceSearchRoute&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=CometMarketplaceSearchContentPaginationQuery&server_timestamps=true&variables=%7B%22count%22%3A24%2C%22cursor%22%3A%22%7B%5C%22pg%5C%22%3A1%2C%5C%22b2c%5C%22%3A%7B%5C%22br%5C%22%3A%5C%22%5C%22%2C%5C%22it%5C%22%3A0%2C%5C%22hmsr%5C%22%3Afalse%2C%5C%22tbi%5C%22%3A0%7D%2C%5C%22c2c%5C%22%3A%7B%5C%22br%5C%22%3A%5C%22AbpYPOBv-ZyZeqSkMNSW_utxjk7OtZibQ0ITOVnkAjM8x7zd4i4bq2br1JU38rUN1H7XJbyQv5khQQKzXsnZ5xKU77Pn-KYhiC7WpTV8Nx1TBGTENqHM1aI0wWn-H_EQjZkkEWVrMfkFMzufLpe87TYJKgZiBd2KxTRCRmvdt4hcwVAu6rVDqux-PPmuV2K53tHmpEsCKQpHB3Ni2kA9IgnFY79_75BexrPkGytJhP-C3QYOa9agkL_NAtDxY9Bli65J2QhLg43t7uVrH0wIQbwJYUYBZsG2vx4TnDIVh6YLTp6v5xvXQWbztd_rbelnMngKJ13hpHGHRbrI7ZOgwRkZtLQBWsrCWiPzZ8Q1v6T1bqg2xps9dbiZ10PdJHDDesR7HVq80Ci0QWtSX5uXvouvdR47qrjMaSzQtBdpiHUmmtbcnVbSIK6pAD8c4RaF3qKzvM_NW88ssCdtp3dVwnbKJPQ6Yb9EuBhO2XImWUS4tzOEBBPQcd4M-ATr61HCrbx-Hxjn1On72Hrri0PHwJCBaHK7b5ySchx0VrC1IvhaWnqDILChegTG0CJoCFTBp7-FlmbDP4v8yU-2jU4algVNYBTp_xp2KA8inKfBi_uF-q0SjNaZZkisxoFs0Ptg1gsti64dwMRVzwbrHvgHv0haN7LgwXCzAcIwvcM4ThrPkg%5C%22%2C%5C%22it%5C%22%3A18%2C%5C%22rpbr%5C%22%3A%5C%22%5C%22%2C%5C%22rphr%5C%22%3Afalse%2C%5C%22rmhr%5C%22%3Afalse%7D%2C%5C%22ads%5C%22%3A%7B%5C%22items_since_last_ad%5C%22%3A18%2C%5C%22items_retrieved%5C%22%3A18%2C%5C%22ad_index%5C%22%3A0%2C%5C%22ad_slot%5C%22%3A0%2C%5C%22dynamic_gap_rule%5C%22%3A0%2C%5C%22counted_organic_items%5C%22%3A0%2C%5C%22average_organic_score%5C%22%3A0%2C%5C%22is_dynamic_gap_rule_set%5C%22%3Afalse%2C%5C%22first_organic_score%5C%22%3A0%2C%5C%22is_dynamic_initial_gap_set%5C%22%3Afalse%2C%5C%22iterated_organic_items%5C%22%3A0%2C%5C%22top_organic_score%5C%22%3A0%2C%5C%22feed_slice_number%5C%22%3A0%2C%5C%22feed_retrieved_items%5C%22%3A0%2C%5C%22ad_req_id%5C%22%3A386812691%2C%5C%22refresh_ts%5C%22%3A1767299719%2C%5C%22cursor_id%5C%22%3A1878%2C%5C%22mc_id%5C%22%3A0%2C%5C%22ad_index_e2e%5C%22%3A0%2C%5C%22seen_ads%5C%22%3A%7B%5C%22ad_ids%5C%22%3A%5B%5D%2C%5C%22page_ids%5C%22%3A%5B%5D%2C%5C%22campaign_ids%5C%22%3A%5B%5D%7D%2C%5C%22has_ad_index_been_reset%5C%22%3Afalse%2C%5C%22is_reconsideration_ads_dropped%5C%22%3Afalse%7D%2C%5C%22irr%5C%22%3Afalse%2C%5C%22serp_cta%5C%22%3Afalse%2C%5C%22rui%5C%22%3A%5B%5D%2C%5C%22mpid%5C%22%3A%5B%5D%2C%5C%22ubp%5C%22%3Anull%2C%5C%22ncrnd%5C%22%3A1%2C%5C%22irsr%5C%22%3Afalse%2C%5C%22bmpr%5C%22%3A%5B%5D%2C%5C%22bmpeid%5C%22%3A%5B%5D%2C%5C%22nmbmp%5C%22%3Afalse%2C%5C%22skrr%5C%22%3Afalse%2C%5C%22ioour%5C%22%3Afalse%2C%5C%22ise%5C%22%3Afalse%2C%5C%22sms_cursor%5C%22%3A%7B%5C%22page_index%5C%22%3A0%2C%5C%22blended_ad_index%5C%22%3A0%2C%5C%22organics_since_last_ad%5C%22%3A0%2C%5C%22page_organic_count%5C%22%3A0%2C%5C%22blended_organic_index%5C%22%3A0%2C%5C%22returned_ad_index%5C%22%3A0%2C%5C%22total_index%5C%22%3A0%7D%7D%22%2C%22params%22%3A%7B%22bqf%22%3A%7B%22callsite%22%3A%22COMMERCE_MKTPLACE_WWW%22%2C%22query%22%3A%22impreza%20wrx%202009%22%7D%2C%22browse_request_params%22%3A%7B%22commerce_enable_local_pickup%22%3Atrue%2C%22commerce_enable_shipping%22%3Atrue%2C%22commerce_search_and_rp_available%22%3Atrue%2C%22commerce_search_and_rp_category_id%22%3A%5B%5D%2C%22commerce_search_and_rp_condition%22%3Anull%2C%22commerce_search_and_rp_ctime_days%22%3Anull%2C%22filter_location_latitude%22%3A49.2327%2C%22filter_location_longitude%22%3A-123.1207%2C%22filter_price_lower_bound%22%3A0%2C%22filter_price_upper_bound%22%3A214748364700%2C%22filter_radius_km%22%3A40%7D%2C%22custom_request_params%22%3A%7B%22browse_context%22%3Anull%2C%22contextual_filters%22%3A%5B%5D%2C%22referral_code%22%3Anull%2C%22referral_ui_component%22%3Anull%2C%22saved_search_strid%22%3Anull%2C%22search_vertical%22%3A%22C2C%22%2C%22seo_url%22%3Anull%2C%22serp_landing_settings%22%3A%7B%22virtual_category_id%22%3A%22%22%7D%2C%22surface%22%3A%22SEARCH%22%2C%22virtual_contextual_filters%22%3A%5B%5D%7D%7D%2C%22scale%22%3A2%7D&doc_id=25322853750669419"
# {
# 	"Request Cookies": {
# 		"c_user": "100080415237651",
# 		"datr": "gaROadi6gZcpjO07VMeLXqsV",
# 		"dpr": "2",
# 		"fr": "1XyauK4AhKlYtPgAG.AWf--KR-FokqkjFtcV1H8uZb-bO4-LvlbGkUcaKp5Q2EYI9k554.BpWJ4j..AAA.0.0.BpWJ4j.AWfGGr_OqvUcqyQcIcpo5xUmxCY",
# 		"presence": "C{\"t3\":[],\"utc3\":1767415492776,\"v\":1}",
# 		"ps_l": "1",
# 		"ps_n": "1",
# 		"sb": "gaROaVMYEQjevC1JjOLReIal",
# 		"wd": "1720x423",
# 		"xs": "12:XQooS2vDXozqHw:2:1767415328:-1:-1::Acx-lyDOEcHfS0mpY2AlzJs5XdY4rfbU70UXFmSgDg"
# 	}
# }


  

variables = {
    "count": 24,
    "cursor": '{"pg":1,"b2c":{"br":"","it":0,"hmsr":False,"tbi":0},"c2c":{"br":"AbpYPOBv-ZyZeqSkMNSW_utxjk7OtZibQ0ITOVnkAjM8x7zd4i4bq2br1JU38rUN1H7XJbyQv5khQQKzXsnZ5xKU77Pn-KYhiC7WpTV8Nx1TBGTENqHM1aI0wWn-H_EQjZkkEWVrMfkFMzufLpe87TYJKgZiBd2KxTRCRmvdt4hcwVAu6rVDqux-PPmuV2K53tHmpEsCKQpHB3Ni2kA9IgnFY79_75BexrPkGytJhP-C3QYOa9agkL_NAtDxY9Bli65J2QhLg43t7uVrH0wIQbwJYUYBZsG2vx4TnDIVh6YLTp6v5xvXQWbztd_rbelnMngKJ13hpHGHRbrI7ZOgwRkZtLQBWsrCWiPzZ8Q1v6T1bqg2xps9dbiZ10PdJHDDesR7HVq80Ci0QWtSX5uXvouvdR47qrjMaSzQtBdpiHUmmtbcnVbSIK6pAD8c4RaF3qKzvM_NW88ssCdtp3dVwnbKJPQ6Yb9EuBhO2XImWUS4tzOEBBPQcd4M-ATr61HCrbx-Hxjn1On72Hrri0PHwJCBaHK7b5ySchx0VrC1IvhaWnqDILChegTG0CJoCFTBp7-FlmbDP4v8yU-2jU4algVNYBTp_xp2KA8inKfBi_uF-q0SjNaZZkisxoFs0Ptg1gsti64dwMRVzwbrHvgHv0haN7LgwXCzAcIwvcM4ThrPkg","it":18,"rpbr":"","rphr":false,"rmhr":false},"ads":{"items_since_last_ad":18,"items_retrieved":18,"ad_index":0,"ad_slot":0,"dynamic_gap_rule":0,"counted_organic_items":0,"average_organic_score":0,"is_dynamic_gap_rule_set":false,"first_organic_score":0,"is_dynamic_initial_gap_set":false,"iterated_organic_items":0,"top_organic_score":0,"feed_slice_number":0,"feed_retrieved_items":0,"ad_req_id":386812691,"refresh_ts":1767299719,"cursor_id":1878,"mc_id":0,"ad_index_e2e":0,"seen_ads":{"ad_ids":[],"page_ids":[],"campaign_ids":[]},"has_ad_index_been_reset":false,"is_reconsideration_ads_dropped":false},"irr":false,"serp_cta":false,"rui":[],"mpid":[],"ubp":None,"ncrnd":1,"irsr":false,"bmpr":[],"bmpeid":[],"nmbmp":false,"skrr":false,"ioour":false,"ise":false,"sms_cursor":{"page_index":0,"blended_ad_index":0,"organics_since_last_ad":0,"page_organic_count":0,"blended_organic_index":0,"returned_ad_index":0,"total_index":0}}',
    "params": {
        "bqf": {"callsite": "COMMERCE_MKTPLACE_WWW", "query": "impreza wrx 2009"},
        "browse_request_params": {
            "commerce_enable_local_pickup": True,
            "commerce_enable_shipping": True,
            "commerce_search_and_rp_available": True,
            "commerce_search_and_rp_category_id": [],
            "commerce_search_and_rp_condition": None,
            "commerce_search_and_rp_ctime_days": None,
            "filter_location_latitude": 49.2327,
            "filter_location_longitude": -123.1207,
            "filter_price_lower_bound": 0,
            "filter_price_upper_bound": 214748364700,
            "filter_radius_km": 40,
        },
        "custom_request_params": {
            "browse_context": None,
            "contextual_filters": [],
            "referral_code": None,
            "referral_ui_component": None,
            "saved_search_strid": None,
            "search_vertical": "C2C",
            "seo_url": None,
            "serp_landing_settings": {"virtual_category_id": ""},
            "surface": "SEARCH",
            "virtual_contextual_filters": [],
        },
    },
    "scale": 2,
}

COOKIE = "datr=gaROadi6gZcpjO07VMeLXqsV; sb=gaROaVMYEQjevC1JjOLReIal; wd=1720x423; fr=1XyauK4AhKlYtPgAG.AWf--KR-FokqkjFtcV1H8uZb-bO4-LvlbGkUcaKp5Q2EYI9k554.BpWJ4j..AAA.0.0.BpWJ4j.AWfGGr_OqvUcqyQcIcpo5xUmxCY; dpr=2; ps_l=1; ps_n=1; c_user=100080415237651; xs=12%3AXQooS2vDXozqHw%3A2%3A1767415328%3A-1%3A-1%3A%3AAcx-lyDOEcHfS0mpY2AlzJs5XdY4rfbU70UXFmSgDg; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1767416131624%2C%22v%22%3A1%7D"
HEADERS={
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
  "Accept": "*/*",
  "Accept-Language": "en-US,en;q=0.5" ,
  "Accept-Encoding": "gzip, deflate" ,
  "Content-Type": "application/x-www-form-urlencoded" ,
  "X-FB-Friendly-Name": "CometMarketplaceSearchContentPaginationQuery" ,
  "X-FB-LSD": "qeHmuLmAf-bQna3QVcY7Zh" ,
  "X-ASBD-ID": "359341" ,
  "Origin": "https://www.facebook.com" ,
  "Sec-GPC": "1" ,
  "Alt-Used": "www.facebook.com" ,
  "Connection": "keep-alive" ,
  "Referer": "https://www.facebook.com/marketplace/edmonton/search?query=impreza%20" ,
  "Cookie": COOKIE ,
  "Sec-Fetch-Dest": "empty" ,
  "Sec-Fetch-Mode": "cors" ,
  "Sec-Fetch-Site": "same-origin" ,
  "DNT": "1" ,
}

DATA_RAW='av=100080415237651&__aaid=0&__user=100080415237651&__a=1&__req=k&__hs=20456.HCSV2%3Acomet_pkg.2.1...0&dpr=2&__ccg=EXCELLENT&__rev=1031595954&__s=6y6d3w%3A53bdkw%3Avbykap&__hsi=7590994478144883327&__dyn=7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwhUKbgS3q2ibwNw9G2Sawba1DwUx60GE3Qwb-q7oc81EEc87m221Fwgo9oO0n24oaEnxO0Bo7O2l2Utwqo5W1ywiE4u9x-3m1mzXw8W58jwGzEaE5e3ym2SU4i5oe8cEW4-5pUfEe88o4Wm7-2K0-obUG2-azqwt8eo5d08O321LyUaUbGxe6Uak0zU8oC1Hg6C13xecwBwWzUlwEKufxamEbbxG1fBG2-2K0E8461wweW2K3abxG6E2Uw&__csr=gphYY6caH2G8x75i9R4PRq8ziGTtT9Fn9JQzi9RqiFnFFdtJOFlWqHhndPYtkNJZQnymluZ8BQJfiVmtutuCnACGnDmajGFrDV_-iEjHyk9DhFaXx3GECdBgKmcVEOiUSVopzngXCz4i4VoOm-48DzWy8GUWidKEnChGxiaxO6VEgxe1Mxi3fwBhoB3Ey2OEKmiu323idx51q3mcw-J3FUeFUd8886u8wFzo-7-5Usxe1ozpUG4rzKEG2m6UaV8eo9u1gg5ydxe2y3m210xDwUwt9k0PEcobo460AopxiQu7-5o4m5K7Uy1lx60JV8dE1AE6u3S1pwWw7FwPyUO486K1lw86K10wsrwok1sxOlXAg5t0_iyy0s82nxu8gfk8wt9EixW3G9wkVWDw098G0oS00WKU2Rw2M60fOy5w136i0BA6pi01ae08FAa0ii060o08AU0VoM0iew5sw0I4K08BwwEw1Vo1To0fNm0G81WE0tbg1t8Dw30o&__hsdp=gJ22qe69GgOu6z4qEyiq5ENbeWeWi69eGqW78PWGiz8Ksfd6bEb48wjG8IZjGhF4c8J8J9MKGa84FpAzeAF5p1n79NRMlq3AnI4u6yiPOmw_4Old2MCTkjC8A8LaqAda6WBg-exqACWDQgxadv6Rz9k9Xhpt22eEcagGcOj8wBG8x5CF58bESaW4aFGf2QxF4MkA6aGgAovsdZ3oFtpjGmzIplkgxOeeKAi8-hemiq4K4aKEKqFEKbzWyuezbjK5UkFxy8yAkk5oKQQl3F94q1fxOfy9aeXCBCGqmVy5Az8gzkQCuWiyEhjSQ94kq4EgxbCCkM9UkykukSmFUC6dG9j4xeEyF9FpoW8KUJ8g59FJ0DAccByEIMqzEk8u6U8WxO2EyobUnAzEyE5etaaCyqxOUlwlEfohyS7p-1nxa8g6KU4m2Z0hAewEzS3C0Nk6UG4o6O19w2qEChUaE2ObUdaU-0RU881qE4u6Za7U2ow6xw4Gwee1awDwfC0H84y0mG0Io3CwGwUw7qwAw5fw7FAw4Lw7mw6dw72w3PEpwFw3681aE1AU7-3S0Oo3pw43wfC0Fo3Fwca0c4waS06Fo5G0om3-0lK0RE&__hblp=0pE3IwOw4dy9FEb9_wh86G0RUyEaE3wwsE3Cwjohwt81zEKFo998mUoxq1UwqEtDwto6a58ozEe81bU7a2y0M816E4m1Twi8eU35xOawSwPxe19w4iw5cwhK0Jo19E882Iwem1xxW1sxqm048U3qwcK3a5o3Zwr8O0F814o1bUa82WwAwpE2PxK0kedxK0B981bU2Mw8C0x8mCw66wcS0Z83AwnE1FE3zxCu261Fw5IAGU1do8E11U18o761_wZwcC0So21wMwk83QAwam5U3hwca0kG0QU3BwaS0hi0aKweO1Tw4cwhoao5G0RUgxG3e3h1u7o34wGw8S1Ywmo4m&__sjsp=gJ22qe69GgOu6z4jEyjifqciPKzKAxyAGCKxMLBAGAOVMLcQoKwIgy1eEyRRkWAjh32bLt9E8Oahy6y9pAzeWAlAkLNPkts8iY8W3AnI4u6yiPOmw_4Old2MCXlcCoygyYFGgUw943CiUqGu4Bxe9Xhpt2XG3d1uEqwFC80S8a8c8hxO4EjyVo88jxC36cwyw9y2ih6wr8owIz86S1WDwjk59oG9xyAEBci4U889o1UE1qk1_xa8g3CwhA17o&__comet_req=15&fb_dtsg=NAfsOmq8iqDWkF5ejgh1ntnBzneWjraeh2-q7hTQZvtux7O5fJ_1CkQ%3A12%3A1767415328&jazoest=25721&lsd=qeHmuLmAf-bQna3QVcY7Zh&__spin_r=1031595954&__spin_b=trunk&__spin_t=1767416130&__jssesw=1&__crn=comet.fbweb.CometMarketplaceSearchRoute&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=CometMarketplaceSearchContentPaginationQuery&server_timestamps=true&variables=%7B%22count%22%3A24%2C%22cursor%22%3A%22%7B%5C%22pg%5C%22%3A1%2C%5C%22b2c%5C%22%3A%7B%5C%22br%5C%22%3A%5C%22%5C%22%2C%5C%22it%5C%22%3A0%2C%5C%22hmsr%5C%22%3Afalse%2C%5C%22tbi%5C%22%3A0%7D%2C%5C%22c2c%5C%22%3A%7B%5C%22br%5C%22%3A%5C%22AbqHZTDmha4fKt4Wi-X4ZFdAPMX4ptwXo_F2xUdRPHLbODRVOVDNTr_Toaq-JR4j6yzQjLgV7OP2ZSEDLizarajQbbNluPp50jeg1-ek1jG4g_JFfjCQ1Y95wYXk6v-SWf0GYayODnk0Y0lx-2pBjwQCqtjpoXMxtW7b56Q7JKI8EgfNvybNFxRvGgIhTCzV64Hz46R3baZNj3m2GGemipbXXAjaFRVYMAfBQw8UkfA4-NX2iVxecdWmsxbmR_DykhuxFjO6ZFT7FywU5ENkl8FdQ4nPrhA7JtnXTmgy2bXbXLt8Yf7f1iOMvaG4Q-a0XF8Tm9jrqlZEuxaGBLc59-TVWtyOhC6oBlEyxT34EPVc5bidD4DArrolSe_PKtSueVmtGC78PhIsYCecQBiz0mfX_5BU3scC7p_tzWoePxQhhNaoB7wx-UNTTELGC8wP7DUNDTgReyy6hJVpSPSN3QIndG92RvvM69PTxnwtYkn6k_uHUCEpPJnlExpBHuq6GPymbT3oTvB2gBWjpD8INFRsmJ8Y2Y7Dtb56ghrjvfmdh8nULJVt-MLZ5ax2SR5haFFrx336pq6lA-2sq4qkPuJNev_ptLQNGXgw3FyaeIjGU92yoSVOZVZH9PrGBQmtrCfrACKRiMK_yTH-QTG06Bh4oYr7hsuk9qwgVxTzxA_cyA%5C%22%2C%5C%22it%5C%22%3A19%2C%5C%22rpbr%5C%22%3A%5C%22%5C%22%2C%5C%22rphr%5C%22%3Afalse%2C%5C%22rmhr%5C%22%3Afalse%7D%2C%5C%22ads%5C%22%3A%7B%5C%22items_since_last_ad%5C%22%3A19%2C%5C%22items_retrieved%5C%22%3A19%2C%5C%22ad_index%5C%22%3A0%2C%5C%22ad_slot%5C%22%3A0%2C%5C%22dynamic_gap_rule%5C%22%3A0%2C%5C%22counted_organic_items%5C%22%3A0%2C%5C%22average_organic_score%5C%22%3A0%2C%5C%22is_dynamic_gap_rule_set%5C%22%3Afalse%2C%5C%22first_organic_score%5C%22%3A0%2C%5C%22is_dynamic_initial_gap_set%5C%22%3Afalse%2C%5C%22iterated_organic_items%5C%22%3A0%2C%5C%22top_organic_score%5C%22%3A0%2C%5C%22feed_slice_number%5C%22%3A0%2C%5C%22feed_retrieved_items%5C%22%3A0%2C%5C%22ad_req_id%5C%22%3A2108433429%2C%5C%22refresh_ts%5C%22%3A1767416131%2C%5C%22cursor_id%5C%22%3A41535%2C%5C%22mc_id%5C%22%3A0%2C%5C%22ad_index_e2e%5C%22%3A0%2C%5C%22seen_ads%5C%22%3A%7B%5C%22ad_ids%5C%22%3A%5B%5D%2C%5C%22page_ids%5C%22%3A%5B%5D%2C%5C%22campaign_ids%5C%22%3A%5B%5D%7D%2C%5C%22has_ad_index_been_reset%5C%22%3Afalse%2C%5C%22is_reconsideration_ads_dropped%5C%22%3Afalse%7D%2C%5C%22irr%5C%22%3Afalse%2C%5C%22serp_cta%5C%22%3Afalse%2C%5C%22rui%5C%22%3A%5B%5D%2C%5C%22mpid%5C%22%3A%5B%5D%2C%5C%22ubp%5C%22%3Anull%2C%5C%22ncrnd%5C%22%3A1%2C%5C%22irsr%5C%22%3Afalse%2C%5C%22bmpr%5C%22%3A%5B%5D%2C%5C%22bmpeid%5C%22%3A%5B%5D%2C%5C%22nmbmp%5C%22%3Afalse%2C%5C%22skrr%5C%22%3Afalse%2C%5C%22ioour%5C%22%3Afalse%2C%5C%22ise%5C%22%3Afalse%2C%5C%22sms_cursor%5C%22%3A%7B%5C%22page_index%5C%22%3A0%2C%5C%22blended_ad_index%5C%22%3A0%2C%5C%22organics_since_last_ad%5C%22%3A0%2C%5C%22page_organic_count%5C%22%3A0%2C%5C%22blended_organic_index%5C%22%3A0%2C%5C%22returned_ad_index%5C%22%3A0%2C%5C%22total_index%5C%22%3A0%7D%7D%22%2C%22params%22%3A%7B%22bqf%22%3A%7B%22callsite%22%3A%22COMMERCE_MKTPLACE_WWW%22%2C%22query%22%3A%22impreza%20%22%7D%2C%22browse_request_params%22%3A%7B%22commerce_enable_local_pickup%22%3Atrue%2C%22commerce_enable_shipping%22%3Atrue%2C%22commerce_search_and_rp_available%22%3Atrue%2C%22commerce_search_and_rp_category_id%22%3A%5B%5D%2C%22commerce_search_and_rp_condition%22%3Anull%2C%22commerce_search_and_rp_ctime_days%22%3Anull%2C%22filter_location_latitude%22%3A53.54158%2C%22filter_location_longitude%22%3A-113.50129%2C%22filter_price_lower_bound%22%3A0%2C%22filter_price_upper_bound%22%3A214748364700%2C%22filter_radius_km%22%3A40%7D%2C%22custom_request_params%22%3A%7B%22browse_context%22%3Anull%2C%22contextual_filters%22%3A%5B%5D%2C%22referral_code%22%3Anull%2C%22referral_ui_component%22%3Anull%2C%22saved_search_strid%22%3Anull%2C%22search_vertical%22%3A%22C2C%22%2C%22seo_url%22%3Anull%2C%22serp_landing_settings%22%3A%7B%22virtual_category_id%22%3A%22%22%7D%2C%22surface%22%3A%22SEARCH%22%2C%22virtual_contextual_filters%22%3A%5B%5D%7D%7D%2C%22scale%22%3A2%7D&doc_id=25322853750669419'

# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
#     "Accept": "*/*",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "X-FB-Friendly-Name": "CometMarketplaceSearchContentPaginationQuery",
#     "X-FB-LSD": "-8AdasLWZPXcFduZyunP-Z",
#     "X-ASBD-ID": "359341",
#     "Origin": "https://www.facebook.com",
#     "Sec-GPC": "1",
#     "Alt-Used": "www.facebook.com",
#     "Connection": "keep-alive",
#     "Referer": "https://www.facebook.com/marketplace/edmonton/search?query=impreza%20wrx%202009",
#     "Cookie": COOKIE,
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "DNT": "1",
# }


class debuggingMarketplaceQuery:
    def __init__(self):
        self.url = "https://www.facebook.com/api/graphql/"
        self.headers = HEADERS
        self.cookie = COOKIE
        self.response = None
        self.response_text = None
        self._variables = None
        self._raw_data = DATA_RAW
        self._json_raw_data = self._raw_data_tojson()
        self.responseListingData = None

    def fetchRequest(self):
        response = requests.post(self.url, headers=self.headers, data=self._raw_data)
        self.response = response
        self.response_text = response.text
        return response

    def printResponseListingTitles(self):
        first_json_line = self.response_text.split('\n')[0]
        json_response = json.loads(first_json_line)

        listings = json_response["data"]['marketplace_search']["feed_units"]['edges']
        self.responseListingData = listings
        listing_single = listings[0]["node"]["listing"]
        for key, value in listing_single.items():
            print(key, value)

        

        for listing in listings:
            if "listing" in listing["node"]:
                title : str= listing["node"]["listing"]['marketplace_listing_title']
                if "5070" in title:
                    continue
                    # print(title)

    def printResponseJson(self):
        print(self.response_text)

    def raw_data_todict(self):
        data = parse_qs(self._raw_data)
        data = {k: v[0] for k, v in data.items()}
        return data

    def extract_variables(self):
        params = self.raw_data_todict()
        self._variables = params["variables"]
        return self._variables

    def _raw_data_tojson(self):
        data = parse_qs(self._raw_data)
        data = {k: v[0] for k, v in data.items()}
        self._raw_json_data = data
        if "variables" in data:
            self._variables = json.loads(data["variables"])
        else:
            print("No variables found in data")

    def _json_data_toraw(self):
        self._raw_json_data["variables"] = json.dumps(self._variables)
        self._raw_data = urlencode(self._raw_json_data)

    def change_location(self, lat, lng):
        self._variables["params"]["browse_request_params"]["filter_location_latitude"] = lat
        self._variables["params"]["browse_request_params"]["filter_location_longitude"] = lng
        self._json_data_toraw()

    def change_query(self, query):
        self._variables["params"]["bqf"]["query"] = query
        self._json_data_toraw()


def main():
    qe = debuggingMarketplaceQuery()
    qe.change_query("Nvidia GPU 5070")
    # qe.change_location(49.2327, -123.1207) # Vancouver
    qe.fetchRequest()
    qe.printResponseListingTitles()


if __name__ == "__main__":
    main()
