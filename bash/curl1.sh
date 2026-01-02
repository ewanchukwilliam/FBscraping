#!/bin/bash

curl 'https://www.facebook.com/ajax/bulk-route-definitions/' \
  --compressed \
  -X POST \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-FB-LSD: _Ou7FKUJAmog1wfwQcwalr' \
  -H 'X-ASBD-ID: 359341' \
  -H 'Origin: https://www.facebook.com' \
  -H 'Sec-GPC: 1' \
  -H 'Alt-Used: www.facebook.com' \
  -H 'Connection: keep-alive' \
  -H 'Referer: https://www.facebook.com/marketplace/edmonton/search?query=impreza%20wrx%202008' \
  -H 'Cookie: datr=gaROadi6gZcpjO07VMeLXqsV; sb=gaROaVMYEQjevC1JjOLReIal; wd=1719x270; c_user=100080415237651; fr=1p6gsxDU7rlFf3E6g.AWfhqWzZABLGe-zVKe9VcgcwvZD3e3wzbLZyVvfVbHJHuRYH2Zw.BpT76m..AAA.0.0.BpT76m.AWcal5m50e8pVXjFXjjnXeJ2JAQ; xs=30%3A8I_E4oj02oEbxw%3A2%3A1766761617%3A-1%3A-1%3A%3AAcyq6b2NxHLUCJqclAmU8Gx74BNAcoawXpdH6_ek2FQ; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1766833831385%2C%22v%22%3A1%7D; dpr=1; ps_l=1; ps_n=1' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'DNT: 1' \
  --data-raw 'route_urls[0]=%2Fmarketplace%2Fedmonton%2Fsearch%3Fquery%3Dimpreza%2520wrx%25202008&routing_namespace=fb_comet&__aaid=0&__user=100080415237651&__a=1&__req=2&__hs=20449.HCSV2%3Acomet_pkg.2.1...0&dpr=1&__ccg=EXCELLENT&__rev=1031491866&__s=0vt150%3A53bdkw%3Aextjsk&__hsi=7588493536219095702&__dyn=7xe5WK1ixt0mUyEqxemh0no6u5U4e1NyUJ3odE98K360O8G0IE6u3y4o2Gwfi0LVE4W0qa321Rw8G11wBz81s8hwGwQw9m0EA2C0iK0D8vwRwpHw8W58jwGzEaE2iwJK14xm3y3aexfxm16wUwxwt819UbUG2-azo7u0zE2cwMwrUdUbGxe6Uak0KU6O1FwlU6Sfxm2yVU-4FqwIK6E4-mEbUaU3ywo83KwHwOwCxG&__csr=gB2V14gGfb4h799A2lRdfvELQTW-BFuKB4hd9O9PPmyT-FyqKF54VkARBAGGFtIyQAQBZmFOkWCHuAGEx4EDAWAjWhi2tuByryaKq49EDhuVUlKfGUGqaGGHUsy-EizUym9AHxxpomgSmuESibx2bKVueK4ErwDVEy3PUiCCxCUuxu3C7oKfwQwi8eocUcEkwiE4mq3i2G482kDxu4EkwCxaUvG6UaFUO1Ixy8wvE6uq8z8eVUgh8nwPwj8Kbwgo9GzrwxzUf8661pBwvE6O0zku0KE2Zw2C5w2nA1qogwh8vwdq0k23W7oe8yax27EaaU98eo8EvwDAwsE07LmU08CAjyoJw0e622h02IS08sw2Dz03lm10wc_o3iw0w8c04-U0mrC9w0N7w0MLK098a9yE0gZw7aw1Au5U0v0w1ang0t1w&__hsdp=l5Ob22ic7EB126zAF9FFERRhQ-t21qVu8Jlp9ckuJq4cpHAF4Xaibc988jgmx65J5iHly5jVJkz9lcKmGHlCVHXGbKjuildEgBuGAvBptd7Hi88OAm2aFkGyABna8RklAMg5QXXjGh6Ki9AJfoowAxm9Az9o8omyVFF8yfykrDh8qocVEmKrn89yFGyJUoINUqGDTimBO8GHiRqbdbkNR55mkkacO8ayUGkMHmFYMisxGFaA9UWqcmaDBzpoWi4KeqwSG9V5LzU9t2-dHB50Ax1Q6ohho564UighDyEkDBwg8yEtgeomxGexe58469GKu22WgP66hFV8K54sBkEsAg4-0CUy2u3y15xu6Uc8C8wu82Dwyg4W26rwqo7-cCDg860OUW0fbw4zw7twrE6Odjg1_819U2Gw5kw9u0_oy0ue0A81qo2Bwf204SUqw12K1Qw11u0E85S0_E22wjU3awg80zO0nS0u20a_w19-09ow7Sw6rw&__hblp=02Ao4-0oS09Vwm81ZopyE8U1hUlwci087w8i0q-0z8W260PoW08yw6pzk0ftw2780Xe0_oy0P83jw5sw66wf208NwaiE660p-6E1fU18o3azU3Kwt84G0bJwdW0E8fovwfW0wEtwNwcG10w2f82VUcFo28w5zwDxS2a4U11E1y8bU0ivw9K0lG1xw7fwCw6rw&__sjsp=l5Ob22ic7EB126zyaqXidZk8K9gwjABUyQhAAOz95IXqejAGuSq6y24Q5Ead5hqUR5yXVEWmdxuWwIB88AGh-nDjgSm8OAm2aFkGyABn8egOiw-te-QWAhHAyp8y784i1sCCzo-4Uy0F818U462m3y6oa85vBwcm4km1BwBwDzo6G1IzE6G9BUabF3f4zU5-0dtg4W26rweC6Q21w&__comet_req=15&fb_dtsg=NAfu7uY0ApGAG3mRve8RqD6g7NRQmAlDMwD0Wlfip9gGPINS8DWv-aQ%3A30%3A1766761617&jazoest=25304&lsd=_Ou7FKUJAmog1wfwQcwalr&__spin_r=1031491866&__spin_b=trunk&__spin_t=1766833834&__crn=comet.fbweb.CometMarketplaceSearchRoute' \
  > output1.json
