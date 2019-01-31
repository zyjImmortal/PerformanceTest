
util = require("util")
user = util.readUser()
cjson = require("cjson")
-- function init( thread )
--     -- body

-- end
-- wrk -t1 -c5 -d2s --script=templatelist.lua https://t-www.meipian.cn/promo/music_cards/api/mycards
badResponse = 0
local  headers = {}
headers["Content-Type"] = "application/x-www-form-urlencoded"
length = #user

function request( )
    -- body
    position = math.random(1, length)
    body = "user_id="..user[position]
    return wrk.format("POST",nil, headers, body)   
end

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