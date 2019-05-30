util = require("util")
user = util.readUser()
length = #user

function request(  )
    position = math.random(1, length)
    local headers = {}
    local template_id = math.random(1,7)
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    body = "user_id="..user[position].."&template_id="..template_id.."&material=http://ss2.meipian.me/music_card/2019/1/31/154890408444279ea9c2496877ae975247a5cda71428f.png"
    return wrk.format("POST",nil,headers,body)
end
function response(status, headers, body)
    if status ~= 200 then
        print(body)
    end
end

-- function done( summary, latency, requests )
--     -- body
--     print()
-- end