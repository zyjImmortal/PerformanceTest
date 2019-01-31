badResponse = 0
headers = {}
headers["Content-Type"]="application/json"
function request()
    -- body
    refresh = math.random(0,1)
    body = '{"is_refresh":'..refresh..'}'
    return wrk.format("POST", nil, headers, body)
end
-- wrk -t1 -c5 -d2s --script=templatelist.lua https://t-www.meipian.cn/promo/music_cards/api/templates

function response(status, headers, body)
    -- body
    print(body)
    if status ~= 200 then
        -- body
        badResponse = badResponse + 1
    end
end

function done(summary, latency, requests)
    -- body
    print(badResponse)
end