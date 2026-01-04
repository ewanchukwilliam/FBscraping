#!/usr/bin/env python

import datetime
from urllib.parse import urlencode
import requests
import json
from urllib import parse
from urllib.parse import parse_qs, unquote

from flatten_json import flatten
COOKIE="datr=gaROadi6gZcpjO07VMeLXqsV; sb=gaROaVMYEQjevC1JjOLReIal; wd=1720x423; fr=1I2ss2vNY3vHwNpO6.AWe39ALUDj-mwHev-cvW0rSDBDCZVAzrg6gF1e74j9mTyHOVYR0.BpWbS4..AAA.0.0.BpWbS4.AWdR3TSXjQFSbiae3Bbfqpg0mjU; dpr=2; ps_l=1; ps_n=1; c_user=100080415237651; xs=39%3AcYa8gpOh7E6F9w%3A2%3A1767486645%3A-1%3A-1%3A%3AAcyTXAabHuG561i8Nia0B8nt8DbQUmXKugCfTAZgQA; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1767486684552%2C%22v%22%3A1%7D"
DATA_RAW="av=100080415237651&__aaid=0&__user=100080415237651&__a=1&__req=1q&__hs=20457.HCSV2%3Acomet_pkg.2.1...0&dpr=2&__ccg=EXCELLENT&__rev=1031606504&__s=v0zkwk%3A53bdkw%3A60qhpb&__hsi=7591297501433393937&__dyn=7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwhUKbgS3q2ibwNw9G2Sawba1DwUx60GE3Qwb-q7oc81EEc87m221Fwgo9oO0n24oaEnxO0Bo7O2l2Utwqo5W1ywiE4u9x-3m1mzXw8W58jwGzEaE5e3ym2SU4i5oe8cEW4-5pUfEe88o4Wm7-2K0-obUG2-azqwt8eo5d08O321LyUaUbGxe6Uak0zU8oC1Hg6C13xecwBwWzUlwEKufxamEbbxG1fBG2-2K0E8461wweW2K3abxG6E2Uw&__csr=g9Av2AgIn2YlsnO8CJOcpeRQxchfbO8Feyn94_9FOHXb5mBiey9iNd4qvRirR-iFHFdQlQqaIRFyajmCkJ16dummbCBQlQHqQFkqJqhXxfioWfAVbVFaooyuZpWBVAbgnABxWmu9DzFp8mUKdJ2XKbzu5oG48CqEeU84ayrAKq6U9ocoG4EvwAzu6pUnx-2KexG4VFoaHwKx22Wq5ojyouxG8xm1Rxm8wxgvxe2q6Ea448nxqAeKm8xO3-4ovDwkF8eEmwm8-489onwKwh8rwRx-1Jxy8xJ0Xwj84m2K0SUeUjwt9u5UaU4Wi2C1Dwto9A3TyUy1bw6qXDw7WEUzgow5fxGfBK1vwSCmmuAiimXwqUqCAwc10mECWzolwVxi01Ugw5Kw043cwTG0T2043o0m9Aa049XwpEC9wQCoeo5MU09yo0dsE0iMw6Pw0SKg5KU0Aay2o0WC0bww0Fnw42w2oU0gSwuC04v8x02uo0iFG5E&__hsdp=gL7Eye794ayopbp248gO5A8yWEyi59GyaOaHq2ai8zJ76uCAy8mW556941uF9AIBlah8ih24hhi92aFaBpj8VmVylpuyhAY9bk4Ajgl2GNx0hAkv919fiq32qhSBOT8y3kTa8y35xJeqdgIzARmnSBCJshWROIuqh7CQ9qh98y_84ouhVACf5Cq8EZBgqiO5Q846y4M_mRR1d6eFVakgkhMES9QGBaUHdAMBWnCaZS4muHyAiWgGchkqeDhpUB4UqGm8yEiCRxq4d28G9Dhhg8FozgBah7K484K798OsWqx6bGhK8AyG8q4oiWBhBCjBbIjxqQdxWaG8BjEMhgW4UrgwPByp9UxAh1gtGujGmrx244gg4e296J1DcdzUlV31e7UiEwfXG2Bdm3maWx-m4E4Sqmt12by984C1lV4UtwHK8g8Vk0Caws9EijwwDmi1IwaW3Kh0iE6ibw2z8jBnxO0DjwhkE981bE2Xw9WuA-0-WwuE18o2lw9W1Ew59xu0me8wau320Zomw52zE7a0ZU0Vu08Lw5vw1ba0iO1DwHwNw4BwnEuw_wIwam1twbu0iG0gK0ga09aw4Pw2CoG09Zw1UO1dwbi2i&__hblp=0p83DwTw4axmK2O744o4i1wwbZ122S0P85a0gC1mzE6W0oG48Cbx-bGiE5S13wg85yewhU2iAxGU7a0ZUK0Vo5m0iG1Txa2W1PwaW3Km19G1yyU3iw5Cw8R0a20q20KVo2RwlE6q3aE-1DG042o3-wv8y0CEO09qwByHxi1twfu1bw77Bwdq1AwAxO08Lwe-1lxC0i60QE1GU5e0Lo1b8aE98nwHwNwcqaKHy8fawxwYxW3-2O0wU8ofEuwbu0iG0Lo9o9U10E3Cw5zw5ew-wzw5cwzw822CayU2Gw4bwjo6O0aJwro3Ew3qUrwYzbwbidxq1fw&__sjsp=gL7Eye794ayopbpmgxiEIF28KG8AxiqExyaHq62a8Pd7ieKCAy8hjEkkoAg5WACiF9lah8-h24hbey885iLgwyelKrlmnEAIGf6iHk8ONAjglMCIog4p57OgijQCwMCAtFsHVi3kTa8y30CCzoNAARm9ppEAx9eEuzpJ2mAii8LUkxWfguySU19GwXBxiQ3iWxCl1W5U8EhwAw8W7Abx21EAwywwCwp87OfxS2e78hxiu8p4gk22u1qw6-w5eg5G2il04cxB0Im&__comet_req=15&fb_dtsg=NAftOInsQB11ti_GdgaAFHUFzJra7DatJ0lfwdovIyIPCSOD66LAJHQ%3A39%3A1767486645&jazoest=25433&lsd=Iecry-uCbqgTHOavjWHsdm&__spin_r=1031606504&__spin_b=trunk&__spin_t=1767486683&__jssesw=1&__crn=comet.fbweb.CometMarketplaceSearchRoute&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=CometMarketplaceSearchContentPaginationQuery&server_timestamps=true&variables=%7B%22count%22%3A24%2C%22cursor%22%3A%22%7B%5C%22pg%5C%22%3A1%2C%5C%22b2c%5C%22%3A%7B%5C%22br%5C%22%3A%5C%22%5C%22%2C%5C%22it%5C%22%3A0%2C%5C%22hmsr%5C%22%3Afalse%2C%5C%22tbi%5C%22%3A0%7D%2C%5C%22c2c%5C%22%3A%7B%5C%22br%5C%22%3A%5C%22Abrcw2qF3uEObC2N-Rzo-w3UutbaKU0WQhPhFqAZSSknlnewMYBnMihYBknh1hPRQlF3FpbRciq4-0Dky3WtUpHFxcZenVEiJ_4VAtjyw2qOmT6SaJrRdQvMXSNYSveVrH5iplpjJwKTE74QA0wsABl0oP1C7J1UXfqHtppKakFIdBvC6lL9P65e-tjD8za-n4QKSmEb27k68p3waGF4Oi6vDwF___Pv5csDjFzjHfA5r52Hx01e9V1bYdjR1Kub_b-k1BrGqrZYBDbzn2DKNn68MpiLjLmof792p51nGUPr1CDi3VITjXBtVbIlwZu1F6N_15IcXr9ujtEn7R9vZGmJ0jF3qIEO1MaAgtxNY48m5sCd4k4Iwz9qMep2a_Pn_vZpX3_BT-6P0qr2Z8ACW9Yk4PvZNccJ1dj2gd1di4kMFU4K8runTzJTAsAPjEBUlmNuKt7PjpJeVn6aM7qPW-K-ZZdfvAsXppD7qIpalVEowG-UGbRTwx56OY76xRLhSmlRpvLOTkKdKBKpf2lvdiXfM3E9xAwk3yGv3sGTE7dNk1zViu8wFLZ9bca48mgSLeAD079tvQjsxSsOFRx5q-KRyJV8ffSV7bx_ImnetLlUqLcLjuPxOU1ZkF6qQ3bwXGZ1afTah2pxJB3tDQAcjNjrJNOx3OQxOIbx7uZMXYnAbQ%5C%22%2C%5C%22it%5C%22%3A19%2C%5C%22rpbr%5C%22%3A%5C%22%5C%22%2C%5C%22rphr%5C%22%3Afalse%2C%5C%22rmhr%5C%22%3Afalse%7D%2C%5C%22ads%5C%22%3A%7B%5C%22items_since_last_ad%5C%22%3A19%2C%5C%22items_retrieved%5C%22%3A19%2C%5C%22ad_index%5C%22%3A0%2C%5C%22ad_slot%5C%22%3A0%2C%5C%22dynamic_gap_rule%5C%22%3A0%2C%5C%22counted_organic_items%5C%22%3A0%2C%5C%22average_organic_score%5C%22%3A0%2C%5C%22is_dynamic_gap_rule_set%5C%22%3Afalse%2C%5C%22first_organic_score%5C%22%3A0%2C%5C%22is_dynamic_initial_gap_set%5C%22%3Afalse%2C%5C%22iterated_organic_items%5C%22%3A0%2C%5C%22top_organic_score%5C%22%3A0%2C%5C%22feed_slice_number%5C%22%3A0%2C%5C%22feed_retrieved_items%5C%22%3A0%2C%5C%22ad_req_id%5C%22%3A827249532%2C%5C%22refresh_ts%5C%22%3A1767486730%2C%5C%22cursor_id%5C%22%3A43260%2C%5C%22mc_id%5C%22%3A0%2C%5C%22ad_index_e2e%5C%22%3A0%2C%5C%22seen_ads%5C%22%3A%7B%5C%22ad_ids%5C%22%3A%5B%5D%2C%5C%22page_ids%5C%22%3A%5B%5D%2C%5C%22campaign_ids%5C%22%3A%5B%5D%7D%2C%5C%22has_ad_index_been_reset%5C%22%3Afalse%2C%5C%22is_reconsideration_ads_dropped%5C%22%3Afalse%7D%2C%5C%22irr%5C%22%3Afalse%2C%5C%22serp_cta%5C%22%3Afalse%2C%5C%22rui%5C%22%3A%5B%5D%2C%5C%22mpid%5C%22%3A%5B%5D%2C%5C%22ubp%5C%22%3Anull%2C%5C%22ncrnd%5C%22%3A1%2C%5C%22irsr%5C%22%3Afalse%2C%5C%22bmpr%5C%22%3A%5B%5D%2C%5C%22bmpeid%5C%22%3A%5B%5D%2C%5C%22nmbmp%5C%22%3Afalse%2C%5C%22skrr%5C%22%3Afalse%2C%5C%22ioour%5C%22%3Afalse%2C%5C%22ise%5C%22%3Afalse%2C%5C%22sms_cursor%5C%22%3A%7B%5C%22page_index%5C%22%3A0%2C%5C%22blended_ad_index%5C%22%3A0%2C%5C%22organics_since_last_ad%5C%22%3A0%2C%5C%22page_organic_count%5C%22%3A0%2C%5C%22blended_organic_index%5C%22%3A0%2C%5C%22returned_ad_index%5C%22%3A0%2C%5C%22total_index%5C%22%3A0%7D%7D%22%2C%22params%22%3A%7B%22bqf%22%3A%7B%22callsite%22%3A%22COMMERCE_MKTPLACE_WWW%22%2C%22query%22%3A%22%20wrx%202009%22%7D%2C%22browse_request_params%22%3A%7B%22commerce_enable_local_pickup%22%3Atrue%2C%22commerce_enable_shipping%22%3Atrue%2C%22commerce_search_and_rp_available%22%3Atrue%2C%22commerce_search_and_rp_category_id%22%3A%5B%5D%2C%22commerce_search_and_rp_condition%22%3Anull%2C%22commerce_search_and_rp_ctime_days%22%3Anull%2C%22filter_location_latitude%22%3A53.54158%2C%22filter_location_longitude%22%3A-113.50129%2C%22filter_price_lower_bound%22%3A0%2C%22filter_price_upper_bound%22%3A214748364700%2C%22filter_radius_km%22%3A40%7D%2C%22custom_request_params%22%3A%7B%22browse_context%22%3Anull%2C%22contextual_filters%22%3A%5B%5D%2C%22referral_code%22%3Anull%2C%22referral_ui_component%22%3Anull%2C%22saved_search_strid%22%3Anull%2C%22search_vertical%22%3A%22C2C%22%2C%22seo_url%22%3Anull%2C%22serp_landing_settings%22%3A%7B%22virtual_category_id%22%3A%22%22%7D%2C%22surface%22%3A%22SEARCH%22%2C%22virtual_contextual_filters%22%3A%5B%5D%7D%7D%2C%22scale%22%3A2%7D&doc_id=25322853750669419"
{
	"Request Cookies": {
		"c_user": "100080415237651",
		"datr": "gaROadi6gZcpjO07VMeLXqsV",
		"dpr": "2",
		"fr": "1EwM1xrSukCWRTIuR.AWdDsa1RC1hCkv1TizyJyFcwESgPi7AnSJNj-U2--w5WN3_T2KM.BpWn_K..AAA.0.0.BpWn_K.AWccigOWj-w6ONP5gs0s5d8ugvM",
		"presence": "C{\"t3\":[],\"utc3\":1767538651566,\"v\":1}",
		"ps_l": "1",
		"ps_n": "1",
		"sb": "gaROaVMYEQjevC1JjOLReIal",
		"wd": "1720x423",
		"xs": "28:wgcewL0u37ZOXw:2:1767538631:-1:-1::Acwa9fX3SOXHsKfrhYaq1yhXVGBXpENKsxxAmvaOBQ"
	}
}
HEADERS={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-FB-Friendly-Name": "CometMarketplaceSearchContentPaginationQuery",
        "X-FB-LSD": "Iecry-uCbqgTHOavjWHsdm",
        "X-ASBD-ID": "359341",
        "Origin": "https://www.facebook.com",
        "Sec-GPC": "1",
        "Alt-Used": "www.facebook.com",
        "Connection": "keep-alive",
        "Referer": "https://www.facebook.com/marketplace/edmonton/search?query=impreza%20wrx%202009",
        "Cookie": COOKIE,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "DNT": "1",
}
  

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
        if response is None:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error fetching data from facebook marketplace. Response is None")
        if response.status_code != 200:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error fetching data from facebook marketplace. Response code: {response.status_code}")
        if response.text is None:
            raise Exception(f"{datetime.datetime.now()} WARN: Error fetching data from facebook marketplace. Response text is None")

        self.response = response
        self.response_text = response.text
        first_json_line = self.response_text.split('\n')[0]
        try:
            self.response_json = json.loads(first_json_line)
        except Exception as e:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error fetching data from facebook marketplace. Response json is malformed: {e}")
        json_response = json.loads(first_json_line)
        listings = json_response["data"]['marketplace_search']["feed_units"]['edges']
        self.responseListingData = listings
        return response

    def printResponseListingTitles(self):
        if self.responseListingData is None:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error printing response listing titles. Response listing data is None")

        if self.responseListingData['node'] is None:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error printing response listing titles. response data is malformed")
        if self.responseListingData['node']['listing'] is None:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error printing response listing titles. response data is malformed")

        listing_single = self.responseListingData[0]["node"]["listing"]
        for key, value in listing_single.items():
            print(key, value)
        for listing in self.responseListingData:
            if "listing" in listing["node"]:
                title : str= listing["node"]["listing"]['marketplace_listing_title']
                if "5070" in title:
                    continue
                    # print(title)

    def printResponseJson(self):
        if self.response_text is None:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error printing response json. Response text is None")
        print(self.response_text)

    def raw_data_todict(self):
        if self._raw_data is None:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error converting raw data to dict. Raw data is None")
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
        try:
            self._variables = json.loads(data["variables"])
        except Exception as e:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error converting raw data to json. Variables is malformed")


    def _json_data_toraw(self):
        if self._variables is None:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error converting json data to raw. Variables is None")
        try:
            self._raw_json_data["variables"] = json.dumps(self._variables)
        except Exception as e:
            raise Exception(f"{datetime.datetime.now()} ERROR: Error converting json data to raw. Variables is malformed: {e}")
        self._raw_data = urlencode(self._raw_json_data)

    def change_location(self, lat, lng):
        if (self._variables is None and self._variables["params"].get("browse_request_params") is None):
            raise Exception(f"{datetime.datetime.now()} ERROR: Error changing location. Variables is None")

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
